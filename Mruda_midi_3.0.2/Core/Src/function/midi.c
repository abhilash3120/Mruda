/*
 * midi.c
 *
 *  Created on: May 14, 2026
 *      Author: abhil
 */
#include "stm32f4xx.h"
#include "math.h"
#include <stdlib.h>
#include "tm1637.h"
#include "function/midi.h"
#include "usbd_hid.h"

extern USBD_HandleTypeDef hUsbDeviceFS;


// 1. Add a global variable to store the channel (0-15 corresponds to Channels 1-16)
uint8_t current_midi_channel = 0;

// 2. Add this new function to set the channel
void midi_set_channel(uint8_t channel) {
    current_midi_channel = (channel-1) & 0x0F; // & 0x0F keeps it safely between 0 and 15
}

// 3. Original function (completely untouched)
void send_usb_midi_packet(uint8_t cin, uint8_t status, uint8_t data1, uint8_t data2) {
    uint8_t packet[4];
    packet[0] = (0x0 << 4) | (cin & 0x0F);  // Cable #0 + CIN
    packet[1] = status;
    packet[2] = data1;
    packet[3] = data2;

   // USBD_HID_SendReport(&hUsbDeviceFS, packet, 4);
}

// 4. Modify internal status bytes to include the current_midi_channel
void midi_note_on(uint8_t note, uint8_t velocity) {
    uint8_t status = 0x90 | current_midi_channel;
    send_usb_midi_packet(0x9, status, note, velocity);
}

void midi_note_off(uint8_t note, uint8_t velocity) {
    uint8_t status = 0x80 | current_midi_channel;
    send_usb_midi_packet(0x8, status, note, velocity);
}

void midi_pitch_bend(float semitones) {
    int32_t bend = (int32_t)(semitones);
    if (bend < 0) bend = 0;
    if (bend > 16383) bend = 16383;

    uint8_t lsb = bend & 0x7F;
    uint8_t msb = (bend >> 7) & 0x7F;

    uint8_t status = 0xE0 | current_midi_channel;
    send_usb_midi_packet(0xE, status, lsb, msb);
}

void midi_pressure(uint8_t note, uint8_t pressure) {
    uint8_t status = 0xA0 | current_midi_channel;
    send_usb_midi_packet(0xA, status, note, pressure);
}
