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
#include "usb_device.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "tm1637.h"
#include "stm32f4xx_hal.h"
#include "usbd_core.h"
#include "usbd_cdc_if.h"
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */
extern uint8_t rx_data_buffer[64];
extern uint8_t rx_flag;
extern uint8_t command;
extern uint32_t rx_packet_len;

extern USBD_HandleTypeDef hUsbDeviceFS;


uint32_t file_size = 0;
uint32_t write_offset = 0;
uint8_t ack_byte = 0x06;
int button = 0;

#define APP_START_ADDR     0x08010000 // Allocation: 16KB for Bootloader
typedef void (*pFunction)(void);

void JumpToApplication(void)
{
    uint32_t appStack;
    uint32_t appResetHandler;
    pFunction appEntry;

    USBD_DeInit(&hUsbDeviceFS);
    HAL_RCC_DeInit();
    HAL_DeInit();

    /* Read application stack pointer */
    appStack = *(volatile uint32_t*)APP_START_ADDR;

    /* Read reset handler address */
    appResetHandler = *(volatile uint32_t*)(APP_START_ADDR + 4);
    appEntry = (pFunction)appResetHandler;

    /* Disable interrupts */
    __disable_irq();

    /* Stop SysTick */
    SysTick->CTRL = 0;
    SysTick->LOAD = 0;
    SysTick->VAL  = 0;

    /* Set main stack pointer */
    __set_MSP(appStack);

    /* Jump to application reset handler */

    appEntry();
}

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */

void Bootloader_EraseAppSpace(uint32_t fileSize)
{
    HAL_FLASH_Unlock();

    FLASH_EraseInitTypeDef EraseInitStruct;
    uint32_t SectorError;

    EraseInitStruct.TypeErase     = FLASH_TYPEERASE_SECTORS;
    EraseInitStruct.VoltageRange  = FLASH_VOLTAGE_RANGE_3;
    EraseInitStruct.Sector        = FLASH_SECTOR_3;        // Application start address location
    EraseInitStruct.NbSectors     = 2;                     // Erase Sectors 2, 3, 4 (Total 192KB)

    HAL_FLASHEx_Erase(&EraseInitStruct, &SectorError);

    HAL_FLASH_Lock();
}

void Bootloader_WriteFlash(uint32_t destAddress, uint8_t *data, uint32_t dataLength)
{
    HAL_FLASH_Unlock();

    // Loop through payload jumping by 4-byte boundaries (Words)
    for (uint32_t i = 0; i < dataLength; i += 4)
    {
        uint32_t word = *(uint32_t*)(&data[i]);
        HAL_FLASH_Program(FLASH_TYPEPROGRAM_WORD, destAddress + i, (uint64_t)word);
    }

    HAL_FLASH_Lock();
}
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */

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
  MX_USB_DEVICE_Init();
  /* USER CODE BEGIN 2 */
  TM1637_Init();
  HAL_Delay(50);
  TM1637_SetColon(0);
  TM1637_DisplayString("COnn");
  button = HAL_GPIO_ReadPin(GPIOB, GPIO_PIN_9);
  if(button == 1){
	  JumpToApplication();
  }

  else{
	  while(1){
		  TM1637_SetColon(0); TM1637_DisplayString("COnn"); HAL_Delay(500);
		  TM1637_SetColon(0); TM1637_DisplayString(""); HAL_Delay(500);
		  if(rx_flag == 1 && command == 5){
			  rx_flag = 0;
			  HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, RESET);
			  TM1637_DisplayString("FLAS");
			  break;
		  }
	  }
  }

  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
	 if(rx_flag == 1){
		 rx_flag =0;

		 if(command == 1){
			 write_offset = 0;
			 file_size =0;

			 file_size = ((uint32_t)rx_data_buffer[0]) |
						  ((uint32_t)rx_data_buffer[1] << 8) |
						  ((uint32_t)rx_data_buffer[2] << 16) |
						  ((uint32_t)rx_data_buffer[3] << 24);
			 Bootloader_EraseAppSpace(file_size);
			 HAL_Delay(10);
			 CDC_Transmit_FS(&ack_byte, 1);
		 }

	 else if (command == 0x02) {

		   uint32_t current_chunk_len = rx_packet_len;
		   Bootloader_WriteFlash(APP_START_ADDR + write_offset, &rx_data_buffer[0], rx_packet_len);
		   write_offset += current_chunk_len;

		   CDC_Transmit_FS(&ack_byte, 1); // Tell Python: "Chunk saved, send next"
	   }

	 else if (command == 0x03) // DONE Packet
	   {
		   CDC_Transmit_FS(&ack_byte, 1); // Final synchronization ACK
		   HAL_Delay(200);                 // Short delay to let USB finish transmitting

		   JumpToApplication();            // Boot into your fresh firmware!
	   }
	}

    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
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
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSI|RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.HSICalibrationValue = RCC_HSICALIBRATION_DEFAULT;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 15;
  RCC_OscInitStruct.PLL.PLLN = 144;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 5;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }

  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_HSI;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_0) != HAL_OK)
  {
    Error_Handler();
  }
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
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();

  /*Configure GPIO pin : PB9 */
  GPIO_InitStruct.Pin = GPIO_PIN_9;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

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
