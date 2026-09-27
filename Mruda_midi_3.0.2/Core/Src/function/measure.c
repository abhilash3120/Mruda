/*
 * measure.c
 *
 *  Created on: Mar 7, 2026
 *      Author: abhil
 */

#include "stm32f4xx.h"
#include "main.h"
#include <stdlib.h>
#include "function/general_func.h"
#include "function/measure.h"
#include "math.h"
#include "tm1637.h"
#include "function/f_set.h"



float touch_raw[50];
float touch_filtered[50];
float touch_p1[50];
float touch_p2[50];
float touch_cal[50];
int mux_sel =0;
static int mux_dir = 1;


struct channels {
	container ch1;
	container ch2;
	container ch3;
};



typedef struct {
	float threshold_on;
	float threshold_off;
	float threshold_ss;
	float threshold_old;
	float sum;
	float side_sum;
	float old_sum;
}touch_validation;

touch_validation touch_check;

//first value is from existing notes to new measurement
float distance_mat[poly_phony][poly_phony];


/*
 * this function needs to be run at the initialistion
 * it measure few values to check the offsets
 * it is dependent on the adc_val that global variable
 */
void key_cal(){

	TM1637_DisplayString("CAL-");
	// ensuere it to zero
	for(int i =0; i<50;i++){
		touch_cal[i] = 0;
	}


	for(int j =0; j<10;j++){

	 	 for(int i = 0; i < 16; i++){
	 		 set_mux(i);HAL_Delay(2);
	 		 touch_cal[i]	 =touch_cal[i]+ adc_val[2];
	 		 touch_cal[i+16] =touch_cal[i+16]+ adc_val[1];
	 		 touch_cal[i+32] =touch_cal[i+32]+ adc_val[0];
	 	 }
	}

	for(int i =0; i<48;i++){
		touch_cal[i] = 0.1f*touch_cal[i];
	}

	TM1637_DisplayString("PLAY");
}




float parabolic_fit(uint8_t index){

	float y0 = touch_filtered[index - 1];
	float y1 = touch_filtered[index];
	float y2 = touch_filtered[index + 1];

	    float denominator = 2.0f * (y0 - 2.0f * y1 + y2);
	    float delta = (y0 - y2) / denominator;
	    delta=delta+(float)index;

	    return delta;
}


float linear_fit(uint8_t index) {
    float y0 = (float)touch_filtered[index - 1];
    float y1 = (float)touch_filtered[index];
    float y2 = (float)touch_filtered[index + 1];

    float total_amp = y0 + y1 + y2;

    if (total_amp < 10.0f) {
        return (float)index;
    }

    float delta = ((y2 - y0) / total_amp);
    return (float)index + delta;
}




peak_Info peak;

void touch_mono(){
	//get max
    float best_amp = 0;
    static float best_pos = -10.0f;

    // --- Peak detection (pick strongest only) ---
    peak.flag_old[0] = peak.flag[0];
    peak.flag[0] = 0;
    for(uint8_t i = 1; i < 47; i++){
        if(touch_filtered[i-1] < touch_filtered[i] &&
           touch_filtered[i+1] < touch_filtered[i])
        {
            float current_sum = touch_filtered[i] +
                                touch_filtered[i-1] +
                                touch_filtered[i+1];

            float threshold_low  = 50;
            float threshold_high = 200;


            float threshold = (peak.flag_old[0] == 1) ? threshold_low : threshold_high;



            if(current_sum > threshold && current_sum > best_amp){
                best_amp = current_sum;
                best_pos = parabolic_fit(i);
                peak.flag[0] = 1;
            }
        }
    }



    //assign to the main note
    peak.pos_out[0] = 0.5*best_pos;
    peak.pos_out[1] = 0;
    peak.pos_out[2] = 0;

    peak.amp[0] = best_amp;


	peak.amp[0]=0.9*peak.amp[0]+0.1*peak.amp_old[0];
	peak.amp_old[0]=peak.amp[0];

	if(peak.amp[0]<0){peak.amp[0]=0;}
	//touch amplitude
	peak.vol[0] = powf(peak.amp[0],set_para.touch_exp);
	key.vol[0] = peak.vol[0]*0.001;
	key.vol[1] = 0;
	key.vol[2] = 0;

}


uint8_t touch_valid(uint8_t i){
	touch_check.threshold_on = 180;
	touch_check.threshold_off = 100;
	touch_check.threshold_ss = 80;
	touch_check.threshold_old = 80;

	float threshold = 0;

	// check peak else return false
	if(touch_filtered[i-1]<touch_filtered[i] && touch_filtered[i+1]<touch_filtered[i]){}
	else{return 0;}

	// threshold calc
	touch_check.old_sum = touch_p1[i]+touch_p1[i+1]+touch_p1[i-1]; // hostory data for sensor array
	touch_check.sum = touch_filtered[i]+touch_filtered[i+1]+touch_filtered[i-1];
	touch_check.side_sum = touch_filtered[i+1]+touch_filtered[i-1];


	// check threshold
	// check if note is already on and apply hysteresis is so

	for (int i = 0; i<poly_phony; i++){
		float dist = abs_calc((float)i, peak.pos_track[i]);
		if (dist < 2.5) {threshold = touch_check.threshold_off; break;}
		else{threshold = touch_check.threshold_on;}
	}

	if (touch_check.sum < threshold) return 0;


	/*check side sensor value and history at least one should satisfy
	 *
	 * 1. at a time there are more than one sensor are triggered. we are giving lower threshold to side value
	 *
	 * 2. for extreme cases there might be only one plate in contact, so past value are checked with their own threshold
	 *
	 */

	if ((touch_check.side_sum> touch_check.threshold_ss) || (touch_check.old_sum > touch_check.threshold_old)) {return 1;}
	else {return 0;}
}


void calc_dist_matrics(){
	for(int key = 0; key< poly_phony ;key++){
		for(int measure = 0; measure < poly_phony; measure++){
			distance_mat[key][measure] = abs_calc(peak.pos[key], peak.pos_track[measure]);
		}
	}
}


uint8_t get_min(){
	float min;
	uint8_t min_key = 0, min_measure = 0;


	//get the minimum entry from the metrics
	min = 2000;
	for(uint8_t key =0; key < poly_phony; key++){
		for(uint8_t measure = 0; measure < poly_phony; measure++){
			if (min>distance_mat[key][measure]){
				min_key = key;
				min_measure = measure;
				min = distance_mat[key][measure];
			}
		}
	}


	// set the row and column to very high value to avoid detection later
	for(int i = 0; i < poly_phony; i++){
		distance_mat[i][min_measure]=2000;
		distance_mat[min_key][i]=2000;
	}

	uint8_t out = ((min_measure & 0x0F) | ((min_key << 4) & 0xF0));
	return out;
}


void note_assignment(){
	uint8_t combination, key, measure;
	float frame_slide = 1.5;

	// Tracks which voices have been assigned in THIS frame
	uint8_t track_arr[poly_phony] = {0};

	for(int n = 0; n < poly_phony; n++){
		combination = get_min();
		key = (combination & 0xF0) >> 4;   // Old voice index
		measure = combination & 0x0F;      // New touch index

		float dist_now = abs_calc(peak.pos[key], peak.pos_track[measure]);

		// Only process valid touch positions (ignore the 1000 dummy values)
		if (peak.pos_track[measure] < 150) {

			// CONDITION 1: Valid Slide or Hold
			if(dist_now < frame_slide && peak.flag[key] == 1) {
				peak.pos[key] = peak.pos_track[measure];
				peak.amp[key] = peak.amp_track[measure];
				peak.index[key] = peak.index_track[measure];

				track_arr[key] = 1; // Mark this voice as kept alive
			}

			// CONDITION 2: New Note (too far for a slide, or old voice was off)
			else {
				int available = -1;

				// Find a slot that hasn't been used this frame AND was OFF last frame
				for(int v = 0; v < poly_phony; v++){
					if (track_arr[v] == 0 && peak.flag[v] == 0) {
						available = v;
						break;
					}
				}

				// If we found a truly empty slot, assign the new touch to it
				if (available != -1) {
					peak.pos[available] = peak.pos_track[measure];
					peak.amp[available] = peak.amp_track[measure];
					peak.index[available] = peak.index_track[measure];

					track_arr[available] = 1; // Mark this new voice as active
				}
			}
		}
	}

	// Update the main flags for the synthesizer
	// Any old voice that didn't get a slide update will have track_arr == 0,
	// effectively turning it OFF this frame.
	for (int v = 0; v < poly_phony; v++){
		peak.flag[v] = track_arr[v];
	}
}


/*
 * flow:
 * 1. validate if topuch is genuine or not
 * 2. get distance between all combination os measured position and previous position
 * 3.find the combination that has lowest disttance between the measured and last acrtive key
 * 4. set all combination of those value to some high value to avoid detection
 * 5. run this lowest distance thing for 5 cycles
 */
void robust_touch_poly(){

	uint8_t measure_index = 0;
	//identify peak and get its position and amplitude
	for(uint8_t i=1;i<47;i++){
			if(touch_valid(i)){
				peak.index_track[measure_index]= i;
				peak.amp_track[measure_index] = touch_check.sum;
				peak.pos_track[measure_index] = linear_fit(i);
				measure_index++;
				if(measure_index>=poly_phony) break;
			}
		}

	//reset the value of unused channel to some default and distinguishable values
	if(measure_index < poly_phony){
		while(measure_index < poly_phony){
			peak.amp_track[measure_index] = 0;
			peak.pos_track[measure_index] = 1000;
			measure_index++;
		}
	}


	//calculate distance matrics
	calc_dist_matrics();
	note_assignment();
}





void touch_estimate(){

	uint8_t temp_indice=0;
	for(uint8_t i=1;i<47;i++){
		if(touch_filtered[i-1]<touch_filtered[i] && touch_filtered[i+1]<touch_filtered[i])
		{
			float current_sum = touch_filtered[i]+touch_filtered[i+1]+touch_filtered[i-1];
			int8_t already_active = 0;

			for (uint8_t k = 0; k < 3; k++) {
				if (peak.flag[k] == 1 && fabsf(peak.pos_old[k] - (float)i) < 4.0f) {
					already_active = 1;
					break;
				}
			}

			float threshold = already_active ? 180 : 250;
			if (current_sum > threshold) {
				peak.index[temp_indice]=i;
				peak.amp[temp_indice]=touch_filtered[i]+touch_filtered[i-1]+touch_filtered[i+1];
				peak.pos[temp_indice]=parabolic_fit(i);
				temp_indice++;
				if(temp_indice==3){break;}
			}
		}
	}


	for (uint8_t k = temp_indice; k < 3; k++) {
	    peak.pos[k] = 0;
	    peak.amp[k] = 0;
	}


	//track

	uint8_t used_new[3] = {0};
	uint8_t used_old[3] = {0};
	for (uint8_t i = 0; i < 3; i++) {
		for (uint8_t j = 0; j < 3; j++) {
			float diff = fabsf(peak.pos_old[i] - peak.pos[j]);
			if (diff < 0.75f && !used_old[i] && !used_new[j]) {
				peak.pos_track[i] = peak.pos[j];
				peak.amp_track[i] = peak.amp[j];
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
					peak.pos_track[i] = peak.pos[j];
					peak.amp_track[i] = peak.amp[j];
					used_old[i] = 1;
					used_new[j] = 1;
					break;
				}
			}
		}
	}

	// Update peak_pos and peak_pos_old for next frame
	for (uint8_t i = 0; i < 3; i++) {
		peak.pos[i] = peak.pos_track[i];
		peak.amp[i] = peak.amp_track[i];
		peak.pos_old[i] = peak.pos[i];

		peak.flag_old[i]=peak.flag[i];
		if(peak.pos[i]!=0){peak.flag[i]=1;}
		else {peak.flag[i]=0; peak.pos_old[i] = -10.0f;}
	}


	for(int i=0;i<3;i++){

		peak.pos_out[i]=0.5f*peak.pos[i];

		peak.amp[i]=0.85*peak.amp[i]+0.15*peak.amp_old[i];
		peak.amp_old[i]=peak.amp[i];

		if(peak.amp[i]<0){peak.amp[i]=0;}
		//touch amplitude
		peak.vol[i] = powf(peak.amp[i],set_para.touch_exp);
		key.vol[i] = peak.vol[i];
	}


	HAL_GPIO_WritePin(GPIOC, GPIO_PIN_13, !(peak.flag[0] || peak.flag[1] || peak.flag[2]));
}




float vol_knob;
void get_touch_position(){


	static float touch_p0[50];
	//meaure
	// maintaining history of last 2 framestouch_p0
	  touch_p1[mux_sel]    = touch_filtered[mux_sel];
	  touch_p1[mux_sel+16] = touch_filtered[mux_sel+16];
	  touch_p1[mux_sel+32] = touch_filtered[mux_sel+32];


	  touch_p2[mux_sel]    = touch_p1[mux_sel];
	  touch_p2[mux_sel+16] = touch_p1[mux_sel+16];
	  touch_p2[mux_sel+32] = touch_p1[mux_sel+32];

	//make 4 measurement and take average



	  touch_raw[mux_sel] =  0.25f*(adc_val[2]+adc_val[5]+adc_val[8]+adc_val[11]);
	  touch_raw[mux_sel+16]=0.25f*(adc_val[1]+adc_val[4]+adc_val[7]+adc_val[10]);
	  touch_raw[mux_sel+32]=0.25f*(adc_val[0]+adc_val[3]+adc_val[6]+adc_val[9]);

	  //removiong the offsets
	  touch_p0[mux_sel]    = touch_raw[mux_sel] - touch_cal[mux_sel];
	  touch_p0[mux_sel+16] = touch_raw[mux_sel+16] - touch_cal[mux_sel+16];
	  touch_p0[mux_sel+32] = touch_raw[mux_sel+32] - touch_cal[mux_sel+32];

	  //IIR LPF
	  float alpha = 0.66;
	  touch_filtered[mux_sel] 	 += alpha * (touch_p0[mux_sel] 	  - touch_filtered[mux_sel]);
	  touch_filtered[mux_sel+16] += alpha * (touch_p0[mux_sel+16] - touch_filtered[mux_sel+16]);
	  touch_filtered[mux_sel+32] += alpha* (touch_p0[mux_sel+32] - touch_filtered[mux_sel+32]);



	if(mux_sel==15){
		mux_dir = -1;
	}
	else if (mux_sel == 0)	{
		mux_dir = +1;   // forward again
	}

	mux_sel += mux_dir;
	set_mux(mux_sel);
}

void sig_sum(){

	float temp = 0;
	for (int i=0; i<48;i++){
		temp = temp + touch_filtered[i];
	}
	touch_filtered[49] = temp*0.02f;
}


void pos_measure_f_cal(){
	if(mux_sel==15 || mux_sel==0){
		//system volume
	    float vol_knob=(float)adc_val[3];
	    peak.sys_vol=vol_knob*0.00025*0.0002;
	    //touch position measurement
	    //sig_sum();
	    //touch_estimate();
		touch_mono();
	    //robust_touch_poly();
		set_freq();
	}
}


