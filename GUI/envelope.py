import numpy as np


class envelope_set():
    def __init__(self, ui):
        self.ui = ui


        self.slider_list = [
            self.ui.s1, self.ui.s2, self.ui.s3, self.ui.s4,
            self.ui.s5, self.ui.s6, self.ui.s7, self.ui.s8,
            self.ui.s9, self.ui.s10, self.ui.s11, self.ui.s12,
            self.ui.s13, self.ui.s14, self.ui.s15, self.ui.s16
            ]


        self.env_slide_list =[
            self.ui.expo, self.ui.tilt, self.ui.oe, self.ui.ham_mix,
            self.ui.randomness, self.ui.fs_c, self.ui.fs_w
            ]
        
        self.env_para_list = [
            self.ui.e_expo, self.ui.e_tilt, self.ui.e_oe, self.ui.e_ham_mix,
            self.ui.e_randomness, self.ui.e_fs_c, self.ui.e_fs_w
            ]
        
        
        for slider, value in zip(self.env_slide_list, self.env_para_list):
            slider.valueChanged.connect(value.setValue)
            value.valueChanged.connect(slider.setValue)

            slider.valueChanged.connect(self.update_array)



        self.envelope = None
        self.base_val = np.full(16, 64)

        self.ui.reset_dist.clicked.connect(self.reset_dist)




    def reset_dist(self):
        self.base_val = np.full(16, 64)
        self.envelope = self.base_val

        self.ui.tilt.setValue(0)
        self.ui.expo.setValue(25)
        self.ui.oe.setValue(0)
        self.ui.ham_mix.setValue(0)
        self.ui.randomness.setValue(0)
        self.ui.fs_c.setValue(0)
        self.ui.fs_w.setValue(0)

        self.norm_and_update()
        for i, slide in enumerate(self.slider_list):
            slide.setValue(int(self.envelope[i]))



    def norm_and_update(self):
        self.envelope = 127* self.envelope / np.max(self.envelope)
        


    def apply_tilt(self):
        value = self.ui.tilt.value()*3/100

        for i in range(16):
            self.envelope[i] = self.envelope[i] / (i+1)**value

        self.norm_and_update()


    def apply_expo(self):
        value = self.ui.expo.value()/25
        print(value)

        for i in range(16):
            self.envelope[i] = self.envelope[i]**value

        self.norm_and_update()

    
    def apply_oe(self):
        value = self.ui.oe.value()
        value = 2 ** (value / 25)

        for i in range(16):

            harmonic = i + 1

            if harmonic % 2 == 0:
                self.envelope[i] *= value
            else:
                self.envelope[i] /= value

        self.norm_and_update()


    def apply_harmonic_mix(self):
        mix = self.ui.ham_mix.value() / 100.0
        temp = self.envelope.copy()

        length = len(self.envelope)
        for i in range(length - 1):

            self.envelope[i] = (
                temp[i]
                + mix * temp[i + 1]
            )

            self.envelope[i] *= (
                1.0 + np.cos(np.pi * (i + 1) / 20.0)
            )

        self.envelope[-1] *= (
            1.0 + np.cos(np.pi * length / 20.0)
        )

        self.norm_and_update()


    def apply_randomness(self):

        amount = self.ui.randomness.value() / 100.0

        temp = self.envelope.copy()

        noise = np.random.uniform(
            -amount,
            amount,
            len(temp)
        )

        self.envelope = temp * (1.0 + noise)
        self.norm_and_update()



    def apply_formant(self):

        center = self.ui.fs_c.value()
        width  = self.ui.fs_w.value()
        if width <= 0:
            return

        temp = self.envelope.copy()

        formant_curve = np.zeros(len(temp))

        for i in range(len(temp)):

            harmonic = i + 1

            formant_curve[i] = np.exp(
                -((harmonic - center) ** 2)
                / (2.0 * (width ** 2))
            )

        # normalize curve
        formant_curve /= np.max(formant_curve)

        # optional: zero-mean behavior
        formant_curve = formant_curve - np.mean(formant_curve)

        self.envelope = temp * (1.0 + formant_curve)
        self.norm_and_update()




    def update_array(self):
        self.envelope = np.full(16, 64)
        self.apply_tilt()
        self.apply_expo()
        self.apply_oe()
        self.apply_formant()
        self.apply_randomness()

        for i, slide in enumerate(self.slider_list):
            slide.setValue(int(self.envelope[i]))

