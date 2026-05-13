/*
 * synth.c
 *
 *  Created on: Mar 8, 2026
 *      Author: abhil
 */

#include "main.h"
#include "function/general_func.h"
#include "function/synth.h"
#include <stdlib.h>
#include "math.h"
#include "function/f_set.h"
#include "function/measure.h"

long t1,t2,dt;

int16_t Buffer[BUFFER_SIZE];

void filter_vol(int ch){
	static float vol_old[5],vol_smooth_old[5];

	for(uint8_t j=0;j<ch;j++){
		key.vol[j]=0.2f*key.vol[j]+0.8f*vol_old[j];
		vol_old[j]=key.vol[j];

		float alpha = (key.vol[j] > key.vol_smooth[j]) ? 0.03f : 0.0005f;
		key.vol_smooth[j] += alpha * (key.vol[j] - key.vol_smooth[j]);
		if(key.vol_smooth[j] < 0.0001f)	key.vol_smooth[j] = 0.0f;
	}

	key.vol[3]=0.005f*key.vol[3]+0.995f*vol_old[3];
	vol_old[3]=key.vol[3];
	key.vol_smooth[3]=0.0002f*key.vol[3]+0.9998f*vol_smooth_old[3];
	vol_smooth_old[3]=key.vol_smooth[3];

	key.vol[4]=0.005f*key.vol[4]+0.995f*vol_old[4];
	vol_old[4]=key.vol[4];
	key.vol_smooth[4]=0.0002f*key.vol[4]+0.9998f*vol_smooth_old[4];
	vol_smooth_old[4]=key.vol_smooth[4];
}


float p[5];
float t_samp_rev;
float t_samp;

void buffer_gen(){

	   t_samp_rev=   key.vol_smooth[0]*sine(p[0])+
			   	   	 key.vol_smooth[1]*sine(p[1])+
					 key.vol_smooth[2]*sine(p[2]);

	   t_samp=		t_samp_rev+
			   	   	key.vol_smooth[3]*sine_t(p[3])+
					key.vol_smooth[4]*sine_t(p[4]);

     // Increment and wrap phase
     p[0] += key.phase[0];
			if (p[0] >= TWOPI)
				p[0] -= TWOPI;

     p[1] += key.phase[1];
         if (p[1] >= TWOPI)
         	p[1] -= TWOPI;

     p[2] += key.phase[2];
         if (p[2] >= TWOPI)
         	p[2] -= TWOPI;

     p[3] += key.phase[3];
         if (p[3] >= TWOPI)
             p[3] -= TWOPI;

     p[4] += key.phase[4];
         if (p[4] >= TWOPI)
             p[4] -= TWOPI;
}


void buffer_gen_mono(){
	filter_vol(1);
	   t_samp_rev=   key.vol_smooth[0]*sine(p[0]);

	   t_samp=		t_samp_rev+
			   	   	key.vol_smooth[3]*sine_t(p[3])+
					key.vol_smooth[4]*sine_t(p[4]);




     // Increment and wrap phase
     p[0] += key.phase[0];
     while  (p[0] >= TWOPI)
				p[0] -= TWOPI;


     p[3] += key.phase[3];
     while  (p[3] >= TWOPI)
             p[3] -= TWOPI;

     p[4] += key.phase[4];
     while  (p[4] >= TWOPI)
             p[4] -= TWOPI;
}



#define AP1_DELAY 117
#define AP2_DELAY 73
#define AP_GAIN   0.4f

float reverb_gen(){
	static int16_t reverb_buf[4001];
	static int reverb_ind = 0;
	static int16_t ap_buf1[AP1_DELAY] = {0};
	static int ap_idx1 = 0;
	static float ap_last1 = 0;

    reverb_buf[reverb_ind] = (int16_t)t_samp_rev;

    //revern using prime samples to avoid ringing
    int16_t rev_delay_chan[8]={503,1079,1499,2111,2503,3067,3547,3989};
    int16_t rev_delay_ind=0;
    float rev_sample=0;


    for(int k=0;k<8;k++){
    	rev_delay_ind= reverb_ind-rev_delay_chan[k];
    	if(rev_delay_ind<0){rev_delay_ind=rev_delay_ind+4000;}
    	rev_sample+=(float)reverb_buf[rev_delay_ind];
    }
    rev_sample=rev_sample*0.125f;

    reverb_ind++;
    if(reverb_ind>=4000){reverb_ind=0;}


    float input_sample=rev_sample;
//            // --- First all-pass filter ---
    float ap_delayed1 = (float)ap_buf1[ap_idx1];
    float ap_output1 = -AP_GAIN * input_sample + ap_delayed1 + AP_GAIN * ap_last1;
    ap_buf1[ap_idx1] = (int16_t)input_sample;
    ap_idx1 = (ap_idx1 + 1) % AP1_DELAY;
    ap_last1 = ap_output1;

    rev_sample=ap_output1;

    t_samp=(1-set_para.reverb)* t_samp+(set_para.reverb)*rev_sample;

    if(t_samp>32000) t_samp=32000;
    else if(t_samp<-32000) t_samp=-32000;
    return t_samp;
}


struct buf_diag_struct {
    int16_t max_amp;
    int16_t max_derivative;
    uint16_t RESET_INTERVAL;
};

struct buf_diag_struct buf_diag = {0, 0, 10000};

void buf_diag_update(int16_t input) {
    static int16_t old_amp = 0;
    static uint16_t reset_counter = 0;

    // Absolute value (safe)
    int16_t abs_sample = (input == INT16_MIN) ? INT16_MAX : (input < 0 ? -input : input);

    if (abs_sample > buf_diag.max_amp)
        buf_diag.max_amp = abs_sample;

    int16_t now_derivative = input - old_amp;
    int16_t abs_derivative = (now_derivative == INT16_MIN) ? INT16_MAX :
                            (now_derivative < 0 ? -now_derivative : now_derivative);

    if (abs_derivative > buf_diag.max_derivative)
        buf_diag.max_derivative = abs_derivative;

    old_amp = input;

    reset_counter++;
    if (reset_counter >= buf_diag.RESET_INTERVAL) {
        buf_diag.max_amp = 0;
        buf_diag.max_derivative = 0;
        reset_counter = 0;
    }
}



void fill_buffer(int16_t *buffer, uint16_t size){
	t1=micros();
	for (int16_t i=0; i < size; i+=2) {

		buffer_gen_mono();
		t_samp = reverb_gen();
		buf_diag_update(t_samp);

	    buffer[i] = (int16_t)t_samp;
	    buffer[i+1] = buffer[i];
	}
	t2=micros();
}
