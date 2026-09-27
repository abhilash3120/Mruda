/*
 * func_sel.c
 *
 *  Created on: Apr 12, 2026
 *      Author: abhil
 */



#include "stm32f4xx.h"
#include "main.h"
#include "math.h"
#include <stdlib.h>
#include <stdio.h>
#include "tm1637.h"
#include "function/f_set.h"
#include "function/measure.h"
#include "function/func_sel.h"
#include "function/general_func.h"
#include "function/usb.h"
#include "function/midi.h"


typedef enum {
	none = 0,
	test =1,
	MiDi = 21,
	scale_down = 22,
	scale_up = 23,
	oct_down = 24,
	oct_up = 25,
	tune_down = 26,
	tune_up = 27,
	auto_corr = 28,
	touch_sen_down = 29,
	touch_sen_up = 30,
	reverb = 31,
	ch_down = 32,
	ch_up = 33,
	pb_down = 34,
	pb_up = 35,
	p3_down = 36,
	p3_up = 37,
	p_set = 38,
	t_scale_down = 39,
	t_scale_up = 40,
	t_vol_down = 41,
	t_vol_up = 42,
	t_on = 43,
}functionID;

typedef struct{
	int flag;
	functionID ID;
}function_info;

function_info func_butn;

int func_val[45];


volatile uint8_t new_setting_flag = 0;
volatile uint8_t setting_array[17] = {0};


void display_menu(const char* label, int val) {
    char buffer[8];
    snprintf(buffer, sizeof(buffer), "%s%d", label, val);
    TM1637_SetColon(1);
    TM1637_DisplayString(buffer);
}




void Scale_Down(){

	func_val[scale_down] = func_val[scale_down]-1;
	func_val[scale_down] = clampf(func_val[scale_down], -9, 9);
	set_para.transpose = func_val[scale_down];
	display_menu("SC", func_val[scale_down]);
}


void Scale_Up(){
	func_val[scale_down] = func_val[scale_down]+1;
	func_val[scale_down] = clampf(func_val[scale_down], -9, 9);
	set_para.transpose = func_val[scale_down];
	display_menu("SC", func_val[scale_down]);
}

void Oct_Down(){
	func_val[oct_down] = func_val[oct_down]-1;
	func_val[oct_down] = clampf(func_val[oct_down], -3, 3);
	set_para.octave = 12*func_val[oct_down];
	display_menu("OC", func_val[oct_down]);
}

void Oct_Up(){
	func_val[oct_down] = func_val[oct_down]+1;
	func_val[oct_down] = clampf(func_val[oct_down], -3, 3);
	set_para.octave = 12*func_val[oct_down];
	display_menu("OC", func_val[oct_down]);
}


void Auto_Corr(){
	func_val[auto_corr] ++;
	if(func_val[auto_corr]>5)func_val[auto_corr] = 0;
	set_para.auro_corr = auto_corr_val[func_val[auto_corr]];
	display_menu("AC", func_val[auto_corr]);
}


void TS_Down(){
	func_val[touch_sen_down] --;
	func_val[touch_sen_down] = clampf(func_val[touch_sen_down], 0, 4);
	set_para.auro_corr = auto_corr_val[func_val[touch_sen_down]];
	display_menu("TS", func_val[touch_sen_down]);
}

void TS_Up(){
	func_val[touch_sen_down] ++;
	func_val[touch_sen_down] = clampf(func_val[touch_sen_down], 0, 4);
	set_para.auro_corr = auto_corr_val[func_val[touch_sen_down]];
	display_menu("TS", func_val[touch_sen_down]);
}




void CH_Down(){
	func_val[ch_down] --;
	func_val[ch_down] = clampf(func_val[ch_down], 1, 16);
	set_para.MIDI_ch = func_val[ch_down];
	midi_set_channel(set_para.MIDI_ch);
	display_menu("CH", func_val[ch_down]);
}

void CH_Up(){
	func_val[ch_down]++;
	func_val[ch_down] = clampf(func_val[ch_down], 1, 16);
	set_para.MIDI_ch = func_val[ch_down];
	midi_set_channel(set_para.MIDI_ch);
	display_menu("CH", func_val[ch_down]);
}

void PB_Down(){
	func_val[pb_down] --;
	func_val[pb_down] = clampf(func_val[pb_down], 0, 2);
	set_para.PB_range = PB_range[func_val[pb_down]];
	display_menu("Pb", func_val[pb_down]);
}

void PB_Up(){
	func_val[pb_down] ++;
	func_val[pb_down] = clampf(func_val[pb_down], 0, 2);
	set_para.PB_range = PB_range[func_val[pb_down]];
	display_menu("Pb", func_val[pb_down]);
}



void dispach(){

	            switch (func_butn.ID) {
	                case scale_down:	Scale_Down();	break;
	                case scale_up:		Scale_Up();  	break;
	                case oct_down:		Oct_Down(); 	break;
	                case oct_up:		Oct_Up(); 		break;
	                case auto_corr:		Auto_Corr();	break;
	                case touch_sen_down:TS_Down();		break;
	                case touch_sen_up:	TS_Up();		break;


	                default:	break;
	            }
	}



void do_pc_command() {
    if (new_setting_flag == 0) return;

    uint8_t cmd = setting_array[0];

    // ==========================================
    // COMMAND 0-5: LOAD & EDIT PRESET
    // ==========================================
    if (cmd <= 5) {
        // 1. Update state variables FIRST
        func_val[p_set] = cmd;
        set_para.preset = (int)cmd;

        // 2. Load incoming data into the correct preset slot
        for (int i = 0; i < 16; i++) {
            preset[cmd][i] = (float)setting_array[i + 1];
        }

//        // 3. Generate the correct sine table
//        if (cmd < 5) {
//            Creat_sine_table(sine_data, cmd);
//        } else {
//            Creat_sine_table(sine_data_tanpura, 5);
//        }
    }

    // ==========================================
    // COMMAND 10-19: SAVE TO FLASH
    // ==========================================
    else if (cmd >= 10 && cmd < 20) {
        uint8_t slot_index = cmd - 10;
        uint8_t start_index = 16 * slot_index;

        // Write directly from the float array to the flash_data byte array
        for (int i = 0; i < 16; i++) {
            flash_data[start_index + i] = (uint8_t)preset[func_val[p_set]][i];
        }

        Flash_SaveData(flash_data);
    }



    new_setting_flag = 0;
}



void function_process(){
	static int counter = 0;
	static uint8_t trigger_latched = 0;
	counter ++;
	if(counter <4) return;  // minimse gpio reads
	counter =0;


	do_pc_command();


	if(mode == Edit) return;

	static int function_t;
	  if (HAL_GPIO_ReadPin(GPIOB, GPIO_PIN_9) == 0) { // Button pressed

	      function_t++;
	      if (function_t == 300) {  // Held for 200ms = 500ms if loop runs every 2.5ms (or adjust if 1ms)
	    	  func_butn.flag = 1;   // Set flag once
	          TM1637_SetColon(0);
	          TM1637_DisplayString("FUNC");
	      }
	  } else {
	      function_t = 0; // Reset counter on release

		  if(func_butn.flag == 1){
			  TM1637_SetColon(0);
			  TM1637_DisplayString("PLAY");}
		  func_butn.flag = 0;
		  trigger_latched = 0;
	      // Do NOT reset function_flag here if you want it to stay ON
	  }

	  if(func_butn.flag){

		  float max = peak.amp[0];
		  func_butn.ID = key.snap[0];
		  if(peak.amp[1]>max){max = peak.amp[1]; func_butn.ID = key.snap[1];}
		  if(peak.amp[2]>max){max = peak.amp[2]; func_butn.ID = key.snap[2];}

	        if(max > 1500) {

	            if(!trigger_latched) {
	                dispach();
	                trigger_latched = 1;
	            }

	        } else {
	            trigger_latched = 0;  // Reset when signal drops
	            func_butn.ID = none;
	        }
	    }

}



