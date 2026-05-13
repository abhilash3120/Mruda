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
#define indicator_Pin GPIO_PIN_13
#define indicator_GPIO_Port GPIOC
#define DEM_1_Pin GPIO_PIN_0
#define DEM_1_GPIO_Port GPIOA
#define DEM_2_Pin GPIO_PIN_1
#define DEM_2_GPIO_Port GPIOA
#define DEM_3_Pin GPIO_PIN_2
#define DEM_3_GPIO_Port GPIOA
#define dac_PWM_Pin GPIO_PIN_3
#define dac_PWM_GPIO_Port GPIOA
#define Extra_Pin GPIO_PIN_4
#define Extra_GPIO_Port GPIOA
#define vol_pot_Pin GPIO_PIN_5
#define vol_pot_GPIO_Port GPIOA
#define sel_3_Pin GPIO_PIN_7
#define sel_3_GPIO_Port GPIOA
#define sel_2_Pin GPIO_PIN_0
#define sel_2_GPIO_Port GPIOB
#define sel_1_Pin GPIO_PIN_1
#define sel_1_GPIO_Port GPIOB
#define sel_0_Pin GPIO_PIN_2
#define sel_0_GPIO_Port GPIOB
#define D_clock_Pin GPIO_PIN_9
#define D_clock_GPIO_Port GPIOA
#define Reference_Pin GPIO_PIN_3
#define Reference_GPIO_Port GPIOB
#define ReferenceB6_Pin GPIO_PIN_6
#define ReferenceB6_GPIO_Port GPIOB
#define ext_sig_800k_Pin GPIO_PIN_7
#define ext_sig_800k_GPIO_Port GPIOB
#define Fun_Key_Pin GPIO_PIN_9
#define Fun_Key_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
