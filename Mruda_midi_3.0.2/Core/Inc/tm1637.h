#ifndef TM1637_H_
#define TM1637_H_

#include "stm32f4xx_hal.h"

// === USER CONFIGURABLE ===
#define TM1637_CLK_PORT GPIOA
#define TM1637_CLK_PIN  GPIO_PIN_9
#define TM1637_DIO_PORT GPIOA
#define TM1637_DIO_PIN  GPIO_PIN_10

// === API ===
void TM1637_Init(void);
void TM1637_DisplayDecimal(int value);
void TM1637_DisplayString(const char* str);  // Up to 4 characters
void TM1637_SetBrightness(uint8_t brightness); // 0-7
void TM1637_SetColon(uint8_t on);

#endif
