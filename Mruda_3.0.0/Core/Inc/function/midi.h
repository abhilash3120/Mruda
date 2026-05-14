/*
 * midi.h
 *
 *  Created on: May 14, 2026
 *      Author: abhil
 */

#ifndef INC_FUNCTION_MIDI_H_
#define INC_FUNCTION_MIDI_H_

void midi_note_on(uint8_t note, uint8_t velocity);
void midi_note_off(uint8_t note, uint8_t velocity);
void midi_pitch_bend(float semitones);
void midi_pressure(uint8_t note, uint8_t pressure);

#endif /* INC_FUNCTION_MIDI_H_ */
