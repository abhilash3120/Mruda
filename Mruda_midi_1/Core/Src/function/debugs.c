/*
 * debugs.c
 *
 *  Created on: May 3, 2026
 *      Author: abhil
 */


#include <math.h>
#include <stdint.h>

#include "function/debugs.h"

#define SAMPLE_RATE 32000.0f
#define PI 3.14159265359f

void generate_sine_block(int16_t *buffer, uint16_t size)
{
    static float phase = 0.0f;
    const float freq = 200.0f;  // change this for testing
    const float amp = 4000.0f;

    float phase_inc = 2.0f * PI * freq / SAMPLE_RATE;

    for (uint16_t i = 0; i < size; i += 2)
    {
        float s = sinf(phase) * amp;
        int16_t sample = (int16_t)s;

        // stereo output (L = R)
        buffer[i]     = sample;
        buffer[i + 1] = sample;

        // increment phase
        phase += phase_inc;

        // safe wrap
        if (phase >= 2.0f * PI)
            phase -= 2.0f * PI;
    }
}
