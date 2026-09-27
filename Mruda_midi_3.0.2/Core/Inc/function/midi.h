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
void send_usb_midi_packet(uint8_t cin, uint8_t status, uint8_t data1, uint8_t data2);
void midi_set_channel(uint8_t channel) ;

#endif /* INC_FUNCTION_MIDI_H_ */
