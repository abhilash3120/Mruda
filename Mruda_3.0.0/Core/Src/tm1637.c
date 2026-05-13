#include "tm1637.h"
#include <string.h>
#include <ctype.h>
#include <stdio.h>

// Segment map
static uint8_t segmentMap[128];
static uint8_t colonOn = 0;

static void TM1637_Delay(void) {
    for (volatile int i = 0; i < 20; i++) __NOP();
}

void TM1637_SetColon(uint8_t on) {
    colonOn = on ? 1 : 0;
}

static void TM1637_Start(void) {
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_SET);
    HAL_GPIO_WritePin(TM1637_DIO_PORT, TM1637_DIO_PIN, GPIO_PIN_SET);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_DIO_PORT, TM1637_DIO_PIN, GPIO_PIN_RESET);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_RESET);
}

static void TM1637_Stop(void) {
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_RESET);
    HAL_GPIO_WritePin(TM1637_DIO_PORT, TM1637_DIO_PIN, GPIO_PIN_RESET);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_SET);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_DIO_PORT, TM1637_DIO_PIN, GPIO_PIN_SET);
}

static void TM1637_WriteByte(uint8_t b) {
    for (int i = 0; i < 8; i++) {
        HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_RESET);
        HAL_GPIO_WritePin(TM1637_DIO_PORT, TM1637_DIO_PIN, (b & 0x01) ? GPIO_PIN_SET : GPIO_PIN_RESET);
        TM1637_Delay();
        HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_SET);
        TM1637_Delay();
        b >>= 1;
    }

    // Acknowledge
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_RESET);
    GPIO_InitTypeDef GPIO_InitStruct = {0};
    GPIO_InitStruct.Pin = TM1637_DIO_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(TM1637_DIO_PORT, &GPIO_InitStruct);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_SET);
    TM1637_Delay();
    HAL_GPIO_WritePin(TM1637_CLK_PORT, TM1637_CLK_PIN, GPIO_PIN_RESET);
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    HAL_GPIO_Init(TM1637_DIO_PORT, &GPIO_InitStruct);
}

void TM1637_SetBrightness(uint8_t brightness) {
    TM1637_Start();
    TM1637_WriteByte(0x88 | (brightness & 0x07));
    TM1637_Stop();
}

static void TM1637_DisplayRaw(uint8_t data[4]) {
    TM1637_Start();
    TM1637_WriteByte(0x40); // auto increment
    TM1637_Stop();

    TM1637_Start();
    TM1637_WriteByte(0xC0); // start addr
    for (int i = 0; i < 4; i++) {
        TM1637_WriteByte(data[i]);
    }
    TM1637_Stop();

    TM1637_SetBrightness(7);
}

void TM1637_DisplayString(const char* str) {
    uint8_t data[4] = {0};
    for (int i = 0; i < 4 && str[i]; i++) {
        char ch = toupper((uint8_t)str[i]);
        data[i] = segmentMap[(uint8_t)ch];

        // Enable colon on digit 2 (index 1)
        if (colonOn && i == 1) {
            data[i] |= 0x80;
        }
    }
    TM1637_DisplayRaw(data);
}

void TM1637_DisplayDecimal(int value) {
    char buf[5];
    snprintf(buf, sizeof(buf), "%4d", value);
    TM1637_DisplayString(buf);
}

void TM1637_Init(void) {
    // Init GPIOs if not done
    GPIO_InitTypeDef GPIO_InitStruct = {0};
    __HAL_RCC_GPIOA_CLK_ENABLE();
    GPIO_InitStruct.Pin = TM1637_CLK_PIN | TM1637_DIO_PIN;
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    // Segment encoding
    memset(segmentMap, 0, sizeof(segmentMap));
    segmentMap['0'] = 0x3f;
        segmentMap['1'] = 0x06;
        segmentMap['2'] = 0x5b;
        segmentMap['3'] = 0x4f;
        segmentMap['4'] = 0x66;
        segmentMap['5'] = 0x6d;
        segmentMap['6'] = 0x7d;
        segmentMap['7'] = 0x07;
        segmentMap['8'] = 0x7f;
        segmentMap['9'] = 0x6f;
        segmentMap['A'] = 0x77;
        segmentMap['B'] = 0x7c;
        segmentMap['C'] = 0x39;
        segmentMap['D'] = 0x5e;
        segmentMap['E'] = 0x79;
        segmentMap['F'] = 0x71;
        segmentMap['G'] = 0x3d;
        segmentMap['H'] = 0x76;
        segmentMap['I'] = 0x06;
        segmentMap['J'] = 0x1e;
        segmentMap['K'] = 0x75;  // Approximation
        segmentMap['L'] = 0x38;
        segmentMap['M'] = 0x37;  // Approximation
        segmentMap['N'] = 0x54;  // Approximation
        segmentMap['O'] = 0x3f;
        segmentMap['P'] = 0x73;
        segmentMap['Q'] = 0x67;  // Approximation
        segmentMap['R'] = 0x50;  // Approximation
        segmentMap['S'] = 0x6d;
        segmentMap['T'] = 0x78;
        segmentMap['U'] = 0x3e;
        segmentMap['V'] = 0x3e;
        segmentMap['W'] = 0x2a;  // Approximation
        segmentMap['X'] = 0x76;  // Approximation
        segmentMap['Y'] = 0x6e;
        segmentMap['Z'] = 0x5b;
        segmentMap['-'] = 0x40;
		segmentMap['_'] = 0x08;
		segmentMap[' '] = 0x00;
		segmentMap['='] = 0x48;
		segmentMap['*'] = 0x63;  // Approximate for star
		segmentMap['.'] = 0x80;
}
