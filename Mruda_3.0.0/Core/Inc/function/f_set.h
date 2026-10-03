/*
 * f_set.h
 *
 *  Created on: Mar 7, 2026
 *      Author: abhil
 */

#ifndef INC_FUNCTION_F_SET_H_
#define INC_FUNCTION_F_SET_H_

extern float p_expo_val[5];
extern float reverb_val[10];;
extern float drone_vol_lookup[11];

extern float touch_expo[5];

extern parameter_t set_para;
extern float preset[6][16];
extern frequency_Info key;

extern uint8_t default_preset[6][16];
extern uint8_t raw_scale[3][25];
extern int8_t default_settings[18];

void set_defaults();
void set_freq();
#endif /* INC_FUNCTION_F_SET_H_ */
