/*
 * synth.h
 *
 *  Created on: Mar 8, 2026
 *      Author: abhil
 */

#ifndef INC_FUNCTION_SYNTH_H_
#define INC_FUNCTION_SYNTH_H_


extern int16_t Buffer[BUFFER_SIZE];

void fill_buffer(int16_t *buff, uint16_t size);
void init_reverb(void);



#endif /* INC_FUNCTION_SYNTH_H_ */
