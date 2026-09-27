/*
 * general_func.h
 *
 *  Created on: Mar 7, 2026
 *      Author: abhil
 */

#ifndef INC_GENERAL_FUNC_H_
#define INC_GENERAL_FUNC_H_

extern float sine_data[SINE_TABLE_LEN+1];
extern float sine_data_tanpura[SINE_TABLE_LEN+1];
extern tanpura_info tanpura;


void set_mux(uint8_t ch);
void Creat_sine_table(float* sin_table, uint8_t preset_type);
void Tanpura();
float clampf(float val, float min, float max) ;
uint32_t micros(void);
void DWT_Delay_Init(void) ;
float sine(float angle);
float sine_t (float angle);
float sine_slow(float angle);
#endif /* INC_GENERAL_FUNC_H_ */
