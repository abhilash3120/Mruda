/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
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

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/

/* USER CODE BEGIN Private defines */


#define SAMPLE_RATE 32000.0f  // Sample rate (Hz)
#define TWOPI       360.0f
#define BUFFER_SIZE 128

#define S0_pin GPIO_PIN_2
#define S0_port GPIOB

#define S1_pin GPIO_PIN_1
#define S1_port GPIOB

#define S2_pin GPIO_PIN_0
#define S2_port GPIOB

#define S3_pin GPIO_PIN_7
#define S3_port GPIOA

#define poly_phony 3

#define PHASE_FACT (TWOPI/SAMPLE_RATE)
#define SINE_TABLE_LEN 1800 // +1 required
#define ADC_DMA_LEN 16  // must be factor of 4

extern float adc_val[ADC_DMA_LEN];
#define angle_mult (SINE_TABLE_LEN / 360.0f)

typedef enum sweep{
	RUN,
	Calibration
}sweep_type;


typedef enum operation{
	Onboard,
	Midi,
	Edit
}operation_mode;

extern operation_mode mode;

typedef struct {
    float touch_exp;
    float auro_corr;
    int octave;
    int transpose;
    float tune;
    float p1;
    float p2;
    float p3;
    float preset;
    float reverb;
} parameter_t;


typedef struct {
    int status;
    int scale;
    float vol;
    float tune;
    float sa;
    float pa;
}tanpura_info;




typedef struct peak_info{
	int index[poly_phony];
	int flag_old[poly_phony];
	int flag[poly_phony];
	float pos[poly_phony];
	float pos_old[poly_phony];
	float vel[poly_phony];
	float vel_old[poly_phony];
	float pos_out[poly_phony];
	float amp[poly_phony];
	float amp_old[poly_phony];
	float vol[poly_phony+2];
	float sys_vol;
	float pos_track[poly_phony];
	float amp_track[poly_phony];
} peak_Info;



typedef struct midi_data{
	uint8_t note;
	uint8_t pressure;
	uint16_t bend;
	uint16_t last_bend;
	uint8_t attack;
	uint8_t release;
}midi_info;



typedef struct frequency_info{
	float abs[poly_phony];
	float play[poly_phony+2];
	float snap_scale[poly_phony+2];
	int snap[poly_phony+2];
	float freq[poly_phony+2];
	float phase[poly_phony+2];
	float error[poly_phony+2];
	float smooth[poly_phony+2];
	float vol[poly_phony+2];
	float vol_smooth[poly_phony+2];

} frequency_Info;

extern volatile uint32_t dfu_flag;





/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
