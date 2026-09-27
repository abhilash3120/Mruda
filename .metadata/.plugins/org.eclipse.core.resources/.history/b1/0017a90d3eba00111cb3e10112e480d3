/*
 * f_set.c
 *
 *  Created on: Mar 7, 2026
 *      Author: abhil
 */



#include "stm32f4xx.h"
#include "main.h"
#include "math.h"
#include <stdlib.h>
#include "tm1637.h"
#include "function/f_set.h"
#include "function/measure.h"
#include "function/general_func.h"
#include "function/func_sel.h"
#include "function/midi.h"
#include "function/auto_corr.h"

parameter_t set_para;



float touch_expo[5]={1.1,1.25,1.34,1.55,1.7};
float auto_corr_val[6]={0,0.005,0.01,0.02,0.05, 0.15};

int PB_range[3] = {2,12,24};


float preset[6][16] ;
float default_preset[6][16];

void set_defaults(){
	set_para.touch_exp = touch_expo[2]; //sensivity default
	set_para.auro_corr = auto_corr_val[0]; //autocorrect default

	//transpose and shifts default
	set_para.tune = 0;
	set_para.transpose = 0;
	set_para.octave = 0;



	midi_set_channel(1);
}


frequency_Info key;
midi_info midi;
long rt1,rt2,rdt;
// Add these static variables near the top of your file or right before the function.
// They must retain their values between loop iterations.

static uint8_t active_midi_note = 0;
static uint8_t last_sent_pressure = 0;
static uint8_t midi_rate_counter = 0;

void set_freq() {
    // 1. Timing calculation
    rt2 = rt1;
    rt1 = micros();
    rdt = rt1 - rt2;

    // ==========================================
    // 2. HARDWARE MATH (Runs at full speed - 5ms)
    // ==========================================
    float play;
    for (uint8_t i = 0; i < 3; i++) {
        if (peak.flag[i] == 1) {

            key.abs[i] = peak.pos_out[i] + 21.0f - 0.5f;
            key.snap[i] = (int)roundf(key.abs[i]);

            if (peak.flag_old[i] == 0) {
                key.smooth[i] = 0;
                key.error[i] = 0;
            }

            // Error is distance from RAW finger to NEAREST note
            key.snap_scale[i] = auto_correct(0, key.abs[i])

            key.error[i] = (key.abs[i] + key.smooth[i]) - key.snap_scale[i];

            // Adjust the smoothing offset to reduce that error
            key.smooth[i] -= set_para.auro_corr * key.error[i];

            // Final pitch is raw + the smoothing offset
            play = key.abs[i] + key.smooth[i];

            key.play[i] = play + set_para.octave + set_para.transpose + set_para.tune;
        }
    }

    // ==========================================
    // 3. MIDI LOGIC (For peak 0)
    // ==========================================



    float vol_hold = key.vol[0];
    if(vol_hold >127) vol_hold = 127;

    midi.pressure = (uint8_t)(vol_hold);


    // --- INSTANT ACTIONS (Evaluated every loop) ---

    // NOTE OFF
    if(peak.flag[0] == 0 && peak.flag_old[0] == 1){
        midi_note_off(active_midi_note, 64);

        midi_pitch_bend(8192); // Snap pitch back to center
        midi.last_bend = 8192;
        last_sent_pressure = 0; // Reset pressure state
    }

    // NOTE ON
    if(peak.flag[0] == 1 && peak.flag_old[0] == 0){
        uint8_t internal_note = (uint8_t)roundf(key.play[0]);
        // 2. Add 21 to translate it to standard MIDI (e.g., 69)
        active_midi_note = internal_note + 21;

        midi.note = active_midi_note;
        midi_note_on(active_midi_note, 100);

        // Force an immediate pressure update to wake up synth envelopes
        midi_pressure(active_midi_note, midi.pressure);
        last_sent_pressure = midi.pressure;
    }


    // --- SLOW ACTIONS (Rate-limited to every 4th loop ~ 10ms) ---

    // CONTINUOUS SLIDING
    else if(peak.flag[0] == 1 && peak.flag_old[0] == 1) {

        midi_rate_counter++;

        if (midi_rate_counter >= 1) {
            midi_rate_counter = 0; // Reset counter

            // Pitch Bend Math (+/- 24 Semitones)
            float pitch_diff = key.play[0] - (float)active_midi_note +21;
            #define BEND_RANGE 12.0f
            int bend_int = 8192 + (int)((pitch_diff / BEND_RANGE) * 8191.0f);

            // CLAMP FIRST (Signed), THEN CAST (Unsigned) to prevent overflow bugs
            if(bend_int > 16383) bend_int = 16383;
            if(bend_int < 0) bend_int = 0;
            midi.bend = (uint16_t)bend_int;

            // Send Bend ONLY if changed
            if(midi.bend != midi.last_bend) {
                midi_pitch_bend(midi.bend);
                midi.last_bend = midi.bend;
            }

            // Send Pressure ONLY if changed
            if(midi.pressure != last_sent_pressure) {


                midi_pressure(active_midi_note, midi.pressure);
                last_sent_pressure = midi.pressure;
            }
        }
    }
}
