/*
 * measure.h
 *
 *  Created on: Mar 7, 2026
 *      Author: abhil
 */

#ifndef INC_FUNCTION_MEASURE_H_
#define INC_FUNCTION_MEASURE_H_

/*
 * not required for function
 * only for debugging
 */
//extern float touch_p1[50];
//extern float touch_p2[50];
//extern float touch_cal[50];
//extern float touch_filtered[50];
//extern int mux_sel;



extern peak_Info peak;


void key_cal();
void get_touch_position();
void touch_estimate();
void pos_measure_f_cal();
void touch_poly_robust();

#endif /* INC_FUNCTION_MEASURE_H_ */
