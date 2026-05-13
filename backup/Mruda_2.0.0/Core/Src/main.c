/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2026 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

#include "math.h"
#include "tm1637.h"
#include <stdio.h>


/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
ADC_HandleTypeDef hadc1;
DMA_HandleTypeDef hdma_adc1;

I2S_HandleTypeDef hi2s2;
DMA_HandleTypeDef hdma_spi2_tx;

TIM_HandleTypeDef htim2;
TIM_HandleTypeDef htim3;
TIM_HandleTypeDef htim4;

/* USER CODE BEGIN PV */


#define SAMPLE_RATE 32000  // Sample rate (Hz)
#define TWOPI       360.0f
#define BUFFER_SIZE 512

#define S0_pin GPIO_PIN_2
#define S0_port GPIOB

#define S1_pin GPIO_PIN_1
#define S1_port GPIOB

#define S2_pin GPIO_PIN_0
#define S2_port GPIOB

#define S3_pin GPIO_PIN_7
#define S3_port GPIOA

#define poly_phony 3

#define phase_v (TWOPI/SAMPLE_RATE)
#define SINE_TABLE_LEN 1800 // +1 required

#define ADC_DMA_LEN 16  // must be factor of 4


#define POS_THRESH   1.90f
#define AMP_ON       410.0f
#define AMP_OFF      300.0f
#define SMOOTH_ALPHA 0.9f   // 0 = no update, 1 = no smoothing


int16_t buffer0[BUFFER_SIZE];
int8_t data_ready_flag=0;
float vol_smooth[5], p[5], PHASE_INC[5];


int16_t adc_dma_buffer[ADC_DMA_LEN], adc_val[ADC_DMA_LEN];

int16_t Sine_table_main[SINE_TABLE_LEN+1];
int16_t Sine_table_tanpura[SINE_TABLE_LEN+1];

float touch[48];
float touch_cal[48];
float touch_p[48], touch_p1[48], touch_p2[48]; // current , previous, 2nd previous
float vol_knob;
uint8_t mux_dir, mux_sel;
long t1,t2,dt;

uint32_t last_count=0;
uint32_t now=0;


uint16_t drone_t=0;
float drone_sa=0;
float drone_pa=0;
float drone_vol=0.04;
int8_t drone_vol_level=5;
float drone_vol_raw=0.0;
float drone_sa_key=27;
float drone_pa_key=22;

float drone_sa_freq=0;
float drone_pa_freq=0;


uint8_t peak[3];
float peak_amp[3];
float peak_pos[3];
float peak_pos_old[3];
float peak_pos_track[3];
float peak_amp_track[3];
float touch_position[poly_phony],touch_position_old[poly_phony];
float touch_amp[poly_phony],touch_amp_old[poly_phony];
int8_t touch_flag[poly_phony], touch_flag_old[poly_phony], release_flag[poly_phony];
float p_expo= 1.35;

float vol[5], vol_old[5], vol_smooth[5], vol_smooth_old[5];


float key[poly_phony], key_refined[poly_phony],key_snap[poly_phony],key_snap_pos[poly_phony];
float key_freq[poly_phony], key_diff[poly_phony], key_play[poly_phony],key_play_old[poly_phony], key_play_freq[poly_phony];
float key_trans[poly_phony];
float key_out[poly_phony];
float transpose=0;
float f_tune=0;
float octave=0;


float snap_flag_val[5]={0,0.002,0.005,0.01,0.02};
float snap_flag_multiplier;
float smoothed_play[3] = {0};
float key_error[3];
uint8_t snap_flag=0;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_DMA_Init(void);
static void MX_ADC1_Init(void);
static void MX_I2S2_Init(void);
static void MX_TIM2_Init(void);
static void MX_TIM3_Init(void);
static void MX_TIM4_Init(void);
/* USER CODE BEGIN PFP */



void set_mux(uint8_t ch) {
    if (ch > 15) return;

    HAL_GPIO_WritePin(S0_port, S0_pin, (ch >> 0) & 0x01);
    HAL_GPIO_WritePin(S1_port, S1_pin, (ch >> 1) & 0x01);
    HAL_GPIO_WritePin(S2_port, S2_pin, (ch >> 2) & 0x01);
    HAL_GPIO_WritePin(S3_port, S3_pin, (ch >> 3) & 0x01);
}


float sine(float angle)
{
    // assuming sine_data[] has 720 points for 0–360° (0.5° step)
    // i.e., one table entry per 0.5°
    angle *= 5.0f;  // convert degrees → 0.5° index scale

    int angle_int = (int)angle;
    float frac = angle - angle_int;          // fractional part
    int next_index = angle_int + 1;

    if (next_index >= SINE_TABLE_LEN)
        next_index = 0;

    // linear interpolation
    float y0 = Sine_table_main[angle_int];
    float y1 = Sine_table_main[next_index];
    return y0 + frac * (y1 - y0);
}


float sine_t(float angle)
{
    // assuming sine_data[] has 720 points for 0–360° (0.5° step)
    // i.e., one table entry per 0.5°
    angle *= 5.0f;  // convert degrees → 0.5° index scale

    int angle_int = (int)angle;
    float frac = angle - angle_int;          // fractional part
    int next_index = angle_int + 1;

    if (next_index >= SINE_TABLE_LEN)
        next_index = 0;

    // linear interpolation
    float y0 = Sine_table_tanpura[angle_int];
    float y1 = Sine_table_tanpura[next_index];
    return y0 + frac * (y1 - y0);
}


void Create_sine_table(int16_t *sine_table){
	float step= 6.28318530718/SINE_TABLE_LEN;
	float current_value;
	for(int i=0; i< SINE_TABLE_LEN; i++){
		current_value = 32000.0f*sin(i*step);
		sine_table[i]=(int) current_value;
	}
	sine_table[SINE_TABLE_LEN+1]=sine_table[0];
}



void fill_buffer0(int16_t *buff, uint16_t size){


    for (int i=0; i < size; i+=2) {

    	for(uint8_t i=0;i<3;i++){
    		vol[i]=0.1f*vol[i]+0.9f*vol_old[i];
    		vol_old[i]=vol[i];

    		vol_smooth[i]=0.1f*vol[i]+0.9f*vol_smooth_old[i];
    		vol_smooth_old[i]=vol_smooth[i];
    	}

    	vol[3]=0.004f*vol[3]+0.996f*vol_old[3];
    	vol_old[3]=vol[3];
		vol_smooth[3]=0.15f*vol[3]+0.85f*vol_smooth_old[3];
		vol_smooth_old[3]=vol_smooth[3];

    	vol[4]=0.004f*vol[4]+0.996f*vol_old[4];
    	vol_old[4]=vol[4];
		vol_smooth[4]=0.15f*vol[4]+0.85f*vol_smooth_old[4];
		vol_smooth_old[4]=vol_smooth[4];

	   float t_samp_rev=   vol_smooth[0]*sine(p[0])+
			   	   	   	   vol_smooth[1]*sine(p[1])+
						   vol_smooth[2]*sine(p[2]);

	   float t_samp=	t_samp_rev+
						   vol_smooth[3]*sine_t(p[3])+
						   vol_smooth[4]*sine_t(p[4]);

        // Increment and wrap phase
        p[0] += PHASE_INC[0];
			if (p[0] >= TWOPI)
				p[0] -= TWOPI;

        p[1] += PHASE_INC[1];
            if (p[1] >= TWOPI)
            	p[1] -= TWOPI;

        p[2] += PHASE_INC[2];
            if (p[2] >= TWOPI)
            	p[2] -= TWOPI;

        p[3] += PHASE_INC[3];
            if (p[3] >= TWOPI)
                p[3] -= TWOPI;

        p[4] += PHASE_INC[4];
            if (p[4] >= TWOPI)
                p[4] -= TWOPI;

            buff[i] = (int16_t)t_samp;
            buff[i+1] = buff[i];

    }
}


void HAL_I2S_TxHalfCpltCallback(I2S_HandleTypeDef *hi2s) {

    fill_buffer0(buffer0, BUFFER_SIZE / 2);  // Fill first half
}

void HAL_I2S_TxCpltCallback(I2S_HandleTypeDef *hi2s) {
    fill_buffer0(buffer0 + BUFFER_SIZE/2, BUFFER_SIZE / 2);  // Fill second half
}

void HAL_ADC_ConvCpltCallback(ADC_HandleTypeDef* hadc){

	for(int i=0;i<ADC_DMA_LEN;i++){
	adc_val[i]=(float)adc_dma_buffer[i];
	}
}


float parabolic_fit(uint8_t index)
{
    // Boundary handling: linear interpolation
    if (index == 0)
    {
        float y0 = touch_p[0];
        float y1 = touch_p[1];

        // Weighted linear centroid between 0 and 1
        if ((y0 + y1) > 0.0f)
            return (0.0f * y0 + 1.0f * y1) / (y0 + y1);
        else
            return 0.0f;
    }
    else if (index == 47)
    {
        float y0 = touch_p[46];
        float y1 = touch_p[47];

        if ((y0 + y1) > 0.0f)
            return (46.0f * y0 + 47.0f * y1) / (y0 + y1);
        else
            return 47.0f;
    }

    // Interior points: parabolic interpolation
    float y0 = touch_p[index - 1];
    float y1 = touch_p[index];
    float y2 = touch_p[index + 1];

    touch_amp[0] = y0 + y1 + y2;

    float denominator = 2.0f * (y0 - 2.0f * y1 + y2);

    // Safety check (flat or noisy peak)
    if (denominator == 0.0f)
        return (float)index;

    float delta = (y0 - y2) / denominator;
    return delta + (float)index;
}



void touch_estimate(){

	//identify the peaks over the array
	uint8_t temp_indice=0;
	float threshold = 900;
	for(uint8_t i=0;i<48;i++){
		if(
				( touch_p[i-1] <touch_p[i]  && touch_p[i+1] <touch_p[i]  && (touch_p[i] +touch_p[i+1] +touch_p[i-1]) >threshold )
			// && ( touch_p1[i-1]<touch_p1[i] && touch_p1[i+1]<touch_p1[i] && (touch_p1[i]+touch_p1[i+1]+touch_p1[i-1])>threshold )
			)
		{

			peak[temp_indice]=i;
			peak_amp[temp_indice]=touch_p[i]+touch_p[i-1]+touch_p[i+1];
			peak_pos[temp_indice]=parabolic_fit(i);
			temp_indice++;
			if(temp_indice==3){break;}
		}
	}

	// fill zeros if its there are les than 3 peaks
	for (uint8_t k = temp_indice; k < 3; k++) {
	    peak_pos[k] = 0;
	    peak_amp[k] = 0;
	}


	uint8_t used_new[3] = {0};
	uint8_t used_old[3] = {0};
	for (uint8_t i = 0; i < 3; i++) {
	    for (uint8_t j = 0; j < 3; j++) {
	        float diff = fabsf(peak_pos_old[i] - peak_pos[j]);
	        if (diff < 1.25f && !used_old[i] && !used_new[j]) {
	            peak_pos_track[i] = peak_pos[j];
	            peak_amp_track[i] = peak_amp[j];
	            used_old[i] = 1;
	            used_new[j] = 1;
	            break;
	        }
	    }
	}

	// Second pass: Fill in unmatched old indices with any unused new values
	for (uint8_t i = 0; i < 3; i++) {
	    if (!used_old[i]) {
	        for (uint8_t j = 0; j < 3; j++) {
	            if (!used_new[j]) {
	                peak_pos_track[i] = peak_pos[j];
	                peak_amp_track[i] = peak_amp[j];
	                used_old[i] = 1;
	                used_new[j] = 1;
	                break;
	            }
	        }
	    }
	}

	// Update peak_pos and peak_pos_old for next frame
	for (uint8_t i = 0; i < 3; i++) {
	    peak_pos[i] = peak_pos_track[i];
	    peak_amp[i] = peak_amp_track[i];
	    peak_pos_old[i] = peak_pos[i];

	    touch_flag_old[i]=touch_flag[i];
	    if(peak_pos[i]!=0){touch_flag[i]=1;}
	    else {touch_flag[i]=0;}
	}

	for(int i=0;i<3;i++){

		peak_pos[i]=0.5*peak_pos[i];

		//touch amplitude
		    touch_amp[i]=touch_amp[i]*vol_knob*0.00008;
		    if(touch_amp[i]<0){touch_amp[i]=0;}
		    touch_amp[i]=powf(touch_amp[i],p_expo);

		    //filter
		    touch_amp[i]=0.75*touch_amp[i]+0.25*touch_amp_old[i];
		    vol[i]=touch_amp[i];

		    touch_amp_old[i]=touch_amp[i];

	}


	//HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, !(touch_flag[0] || touch_flag[1] || touch_flag[2]));


}


void set_freq(){


	for(uint8_t i=0;i<3;i++){
		if(touch_flag[i]==1 && snap_flag>0){
			key[i]=peak_pos[i]+21-0.5; //sensing plate not on senter so 0.5
			key_trans[i]=key[i]+f_tune+transpose+octave;

			if(touch_flag_old[i]==0){
				key_snap[i]=round(key[i]); // only for functions
				smoothed_play[i]=0;
				key_error[i]=0;
			}

			//auto correct
			//if(smoothed_play[i]>0.5){smoothed_play[i]=0.5;}
			key_play[i]=key_trans[i]+smoothed_play[i];
			key_error[i]=key_play[i]-round(key_trans[i]);
			smoothed_play[i]-=snap_flag_multiplier*key_error[i];
			//if(key_error[i]<0.01){key_error[i]=0;}

			key_play[i]=0.9*key_play[i]+0.1*key_play_old[i];
			key_play_old[i]=key_play[i];


			key_play[i] = 440.0f * powf(1.0594630f, (key_play[i] - 48));
			PHASE_INC[i] =phase_v * key_play[i];
		}


		if(touch_flag[i]==1 && snap_flag==0){
					key_snap[i]=round(key[i]); // for function detect
					key[i]=peak_pos[i]+21-0.5; //sensing plate not on senter so 0.5

					key_play[i]=key[i]+f_tune+transpose+octave;
					//key_play[i]=key_play[i]*(1+0.001*rand_float());

					key_out[i]=key_play[i];
					key_play[i]=0.9*key_play[i]+0.1*key_play_old[i];

					key_play_old[i]=key_play[i];

					key_play[i] = 440.0f * powf(1.0594630f, (key_play[i] - 48));
					PHASE_INC[i] =phase_v * key_play[i];
				}
	}
}




/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */

/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{

  /* USER CODE BEGIN 1 */


	Create_sine_table(Sine_table_main);
	Create_sine_table(Sine_table_tanpura);


  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_DMA_Init();
  MX_ADC1_Init();
  MX_I2S2_Init();
  MX_TIM2_Init();
  MX_TIM3_Init();
  MX_TIM4_Init();
  /* USER CODE BEGIN 2 */




  TM1637_Init();
  TM1637_DisplayString("CAL-");
  HAL_Delay(50);
  HAL_TIM_PWM_Start(&htim4, TIM_CHANNEL_2);
  HAL_TIM_PWM_Start(&htim4, TIM_CHANNEL_1);
  __HAL_TIM_SET_COMPARE(&htim4, TIM_CHANNEL_1, 0);

  HAL_TIM_Base_Start(&htim3);
  HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_4);

  __HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_4, 195);
  __HAL_TIM_SET_COMPARE(&htim4, TIM_CHANNEL_2, 27);
//PHASE_INC[0]=2.5;
vol_smooth[0]=0;


HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_dma_buffer, 16);


HAL_Delay(50);
for(int j=0;j<10;j++)
{
	 for(int i = 0; i < 16; i++){
		 set_mux(i);HAL_Delay(2);
		 touch_cal[i]	 =touch_cal[i]+ adc_val[2];
		 touch_cal[i+16] =touch_cal[i+16]+ adc_val[1];
		 touch_cal[i+32] =touch_cal[i+32]+ adc_val[0];
	 }
}


for(int i = 0; i < 48; i++){
	 touch_cal[i]= round(touch_cal[i]/10);
}
TM1637_SetColon(0);
TM1637_DisplayString("PLAY");
drone_pa_freq=440.0f * powf(1.0594630f, (drone_sa_key - 48));
drone_sa_freq=440.0f * powf(1.0594630f, (drone_pa_key - 48));

PHASE_INC[3] =phase_v * drone_sa_freq;
PHASE_INC[4] =phase_v * drone_pa_freq;


HAL_Delay(20);
HAL_I2S_Transmit_DMA(&hi2s2, (uint16_t*)buffer0, BUFFER_SIZE);
HAL_Delay(20);



  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  last_count = __HAL_TIM_GET_COUNTER(&htim3);
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */

	    now = __HAL_TIM_GET_COUNTER(&htim3);


	    if ((now - last_count) >= 250)
	    {

	        last_count = now;

					touch_p2 [mux_sel] = touch_p1[mux_sel];
					touch_p2 [mux_sel+16] = touch_p1[mux_sel+16];
					touch_p2 [mux_sel+32] = touch_p1[mux_sel+32];

	        		touch_p1 [mux_sel] = touch_p[mux_sel];
	        		touch_p1 [mux_sel+16] = touch_p[mux_sel+16];
	        		touch_p1 [mux_sel+32] = touch_p[mux_sel+32];

	        		//meaure
					touch[mux_sel] =  0.25f*(adc_val[2]+adc_val[6]+adc_val[10]+adc_val[14]);
					touch[mux_sel+16]=0.25f*(adc_val[1]+adc_val[5]+adc_val[9]+adc_val[13]);
					touch[mux_sel+32]=0.25f*(adc_val[0]+adc_val[4]+adc_val[8]+adc_val[12]);

					touch_p[mux_sel]   = touch[mux_sel] -touch_cal[mux_sel];
					touch_p[mux_sel+16]= touch[mux_sel+16] -touch_cal[mux_sel+16];
					touch_p[mux_sel+32]= touch[mux_sel+32] -touch_cal[mux_sel+32];

	        	  if(mux_sel==15){
	        	        mux_dir = -1;
	        	  }
	        	  else if (mux_sel == 0)
	        	    {
	        	        mux_dir = +1;   // forward again
	        	    }

	        	  mux_sel += mux_dir;
	        	  set_mux(mux_sel);

	        	  if(mux_sel==15 || mux_sel==0){
	        		  touch_estimate();
	        		  vol_knob=(float)adc_val[3];
	        		  vol_knob=vol_knob/4095;
	        		  set_freq();
	        		  HAL_GPIO_TogglePin(GPIOC, GPIO_PIN_13);
	        	  }
	    }




  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 25;
  RCC_OscInitStruct.PLL.PLLN = 336;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV4;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief ADC1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_ADC1_Init(void)
{

  /* USER CODE BEGIN ADC1_Init 0 */

  /* USER CODE END ADC1_Init 0 */

  ADC_ChannelConfTypeDef sConfig = {0};

  /* USER CODE BEGIN ADC1_Init 1 */

  /* USER CODE END ADC1_Init 1 */

  /** Configure the global features of the ADC (Clock, Resolution, Data Alignment and number of conversion)
  */
  hadc1.Instance = ADC1;
  hadc1.Init.ClockPrescaler = ADC_CLOCK_SYNC_PCLK_DIV4;
  hadc1.Init.Resolution = ADC_RESOLUTION_12B;
  hadc1.Init.ScanConvMode = ENABLE;
  hadc1.Init.ContinuousConvMode = ENABLE;
  hadc1.Init.DiscontinuousConvMode = DISABLE;
  hadc1.Init.ExternalTrigConvEdge = ADC_EXTERNALTRIGCONVEDGE_NONE;
  hadc1.Init.ExternalTrigConv = ADC_SOFTWARE_START;
  hadc1.Init.DataAlign = ADC_DATAALIGN_RIGHT;
  hadc1.Init.NbrOfConversion = 4;
  hadc1.Init.DMAContinuousRequests = ENABLE;
  hadc1.Init.EOCSelection = ADC_EOC_SINGLE_CONV;
  if (HAL_ADC_Init(&hadc1) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_0;
  sConfig.Rank = 1;
  sConfig.SamplingTime = ADC_SAMPLETIME_15CYCLES;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_1;
  sConfig.Rank = 2;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_2;
  sConfig.Rank = 3;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }

  /** Configure for the selected ADC regular channel its corresponding rank in the sequencer and its sample time.
  */
  sConfig.Channel = ADC_CHANNEL_5;
  sConfig.Rank = 4;
  if (HAL_ADC_ConfigChannel(&hadc1, &sConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN ADC1_Init 2 */

  /* USER CODE END ADC1_Init 2 */

}

/**
  * @brief I2S2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_I2S2_Init(void)
{

  /* USER CODE BEGIN I2S2_Init 0 */

  /* USER CODE END I2S2_Init 0 */

  /* USER CODE BEGIN I2S2_Init 1 */

  /* USER CODE END I2S2_Init 1 */
  hi2s2.Instance = SPI2;
  hi2s2.Init.Mode = I2S_MODE_MASTER_TX;
  hi2s2.Init.Standard = I2S_STANDARD_PHILIPS;
  hi2s2.Init.DataFormat = I2S_DATAFORMAT_16B;
  hi2s2.Init.MCLKOutput = I2S_MCLKOUTPUT_DISABLE;
  hi2s2.Init.AudioFreq = I2S_AUDIOFREQ_32K;
  hi2s2.Init.CPOL = I2S_CPOL_LOW;
  hi2s2.Init.ClockSource = I2S_CLOCK_PLL;
  hi2s2.Init.FullDuplexMode = I2S_FULLDUPLEXMODE_DISABLE;
  if (HAL_I2S_Init(&hi2s2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN I2S2_Init 2 */

  /* USER CODE END I2S2_Init 2 */

}

/**
  * @brief TIM2 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM2_Init(void)
{

  /* USER CODE BEGIN TIM2_Init 0 */

  /* USER CODE END TIM2_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM2_Init 1 */

  /* USER CODE END TIM2_Init 1 */
  htim2.Instance = TIM2;
  htim2.Init.Prescaler = 0;
  htim2.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim2.Init.Period = 330;
  htim2.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim2.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_DISABLE;
  if (HAL_TIM_Base_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim2, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  if (HAL_TIM_PWM_Init(&htim2) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim2, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.Pulse = 165;
  if (HAL_TIM_PWM_ConfigChannel(&htim2, &sConfigOC, TIM_CHANNEL_4) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM2_Init 2 */

  /* USER CODE END TIM2_Init 2 */
  HAL_TIM_MspPostInit(&htim2);

}

/**
  * @brief TIM3 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM3_Init(void)
{

  /* USER CODE BEGIN TIM3_Init 0 */

  /* USER CODE END TIM3_Init 0 */

  TIM_ClockConfigTypeDef sClockSourceConfig = {0};
  TIM_MasterConfigTypeDef sMasterConfig = {0};

  /* USER CODE BEGIN TIM3_Init 1 */

  /* USER CODE END TIM3_Init 1 */
  htim3.Instance = TIM3;
  htim3.Init.Prescaler = 83;
  htim3.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim3.Init.Period = 65535;
  htim3.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim3.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_ENABLE;
  if (HAL_TIM_Base_Init(&htim3) != HAL_OK)
  {
    Error_Handler();
  }
  sClockSourceConfig.ClockSource = TIM_CLOCKSOURCE_INTERNAL;
  if (HAL_TIM_ConfigClockSource(&htim3, &sClockSourceConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim3, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM3_Init 2 */

  /* USER CODE END TIM3_Init 2 */

}

/**
  * @brief TIM4 Initialization Function
  * @param None
  * @retval None
  */
static void MX_TIM4_Init(void)
{

  /* USER CODE BEGIN TIM4_Init 0 */

  /* USER CODE END TIM4_Init 0 */

  TIM_MasterConfigTypeDef sMasterConfig = {0};
  TIM_OC_InitTypeDef sConfigOC = {0};

  /* USER CODE BEGIN TIM4_Init 1 */

  /* USER CODE END TIM4_Init 1 */
  htim4.Instance = TIM4;
  htim4.Init.Prescaler = 0;
  htim4.Init.CounterMode = TIM_COUNTERMODE_UP;
  htim4.Init.Period = 47;
  htim4.Init.ClockDivision = TIM_CLOCKDIVISION_DIV1;
  htim4.Init.AutoReloadPreload = TIM_AUTORELOAD_PRELOAD_ENABLE;
  if (HAL_TIM_OC_Init(&htim4) != HAL_OK)
  {
    Error_Handler();
  }
  sMasterConfig.MasterOutputTrigger = TIM_TRGO_RESET;
  sMasterConfig.MasterSlaveMode = TIM_MASTERSLAVEMODE_DISABLE;
  if (HAL_TIMEx_MasterConfigSynchronization(&htim4, &sMasterConfig) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.OCMode = TIM_OCMODE_TOGGLE;
  sConfigOC.Pulse = 0;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_LOW;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
  if (HAL_TIM_OC_ConfigChannel(&htim4, &sConfigOC, TIM_CHANNEL_1) != HAL_OK)
  {
    Error_Handler();
  }
  sConfigOC.Pulse = 27;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  if (HAL_TIM_OC_ConfigChannel(&htim4, &sConfigOC, TIM_CHANNEL_2) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN TIM4_Init 2 */

  /* USER CODE END TIM4_Init 2 */
  HAL_TIM_MspPostInit(&htim4);

}

/**
  * Enable DMA controller clock
  */
static void MX_DMA_Init(void)
{

  /* DMA controller clock enable */
  __HAL_RCC_DMA1_CLK_ENABLE();
  __HAL_RCC_DMA2_CLK_ENABLE();

  /* DMA interrupt init */
  /* DMA1_Stream4_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA1_Stream4_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA1_Stream4_IRQn);
  /* DMA2_Stream0_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA2_Stream0_IRQn, 0, 0);
  HAL_NVIC_EnableIRQ(DMA2_Stream0_IRQn);

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};
  /* USER CODE BEGIN MX_GPIO_Init_1 */

  /* USER CODE END MX_GPIO_Init_1 */

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(indicator_GPIO_Port, indicator_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(sel_3_GPIO_Port, sel_3_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOB, sel_2_Pin|sel_1_Pin|sel_0_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : indicator_Pin */
  GPIO_InitStruct.Pin = indicator_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(indicator_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : sel_3_Pin */
  GPIO_InitStruct.Pin = sel_3_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(sel_3_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : sel_2_Pin sel_1_Pin sel_0_Pin */
  GPIO_InitStruct.Pin = sel_2_Pin|sel_1_Pin|sel_0_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pins : D_clock_Pin PA12 */
  GPIO_InitStruct.Pin = D_clock_Pin|GPIO_PIN_12;
  GPIO_InitStruct.Mode = GPIO_MODE_ANALOG;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : Fun_Key_Pin */
  GPIO_InitStruct.Pin = Fun_Key_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_PULLUP;
  HAL_GPIO_Init(Fun_Key_GPIO_Port, &GPIO_InitStruct);

  /* USER CODE BEGIN MX_GPIO_Init_2 */

  /* USER CODE END MX_GPIO_Init_2 */
}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */
