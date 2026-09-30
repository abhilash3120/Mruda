# this sets the custom scales for autocorrect functions

import mido

scale_notation = ["Indian","Western"]
Scale_type = ["Natural", "Chromatic"]
Sclae_slot = ["Custom 1", "Custom 2", "Custom 3"]



class autocorr_set():
    def __init__(self, ui, conn_class):
        self.ui = ui
        self.conn = conn_class

        self.ac_buttons_list = [self.ui.scale_b1, self.ui.scale_b2,self.ui.scale_b3, self.ui.scale_b4,
                           self.ui.scale_b5, self.ui.scale_b6,  self.ui.scale_b7, self.ui.scale_b8,
                           self.ui.scale_b9, self.ui.scale_b10, self.ui.scale_b11, self.ui.scale_b12]

        self.ac_radio_list = [self.ui.scale_r1, self.ui.scale_r2,self.ui.scale_r3, self.ui.scale_r4,
                           self.ui.scale_r5, self.ui.scale_r6,   self.ui.scale_r7, self.ui.scale_r8,
                           self.ui.scale_r9, self.ui.scale_r10,  self.ui.scale_r11, self.ui.scale_r12]

        self.ac_val_list= [self.ui.scale_sb1, self.ui.scale_sb2,self.ui.scale_sb3, self.ui.scale_sb4,
                           self.ui.scale_sb5, self.ui.scale_sb6,  self.ui.scale_sb7, self.ui.scale_sb8,
                           self.ui.scale_sb9, self.ui.scale_sb10, self.ui.scale_sb11, self.ui.scale_sb12]

        
        self.ac_slide_list= [self.ui.scale_s1, self.ui.scale_s2,self.ui.scale_s3, self.ui.scale_s4,
                           self.ui.scale_s5, self.ui.scale_s6,  self.ui.scale_s7, self.ui.scale_s8,
                           self.ui.scale_s9, self.ui.scale_s10, self.ui.scale_s11, self.ui.scale_s12]



        self.indian_notes = ["SA", "re", "RE","ga", "GA","ma","MA","PA","dha","DHA","ni","NI"]
        self.chromatic_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

        self.w = "background-color: white; color: black;"
        self.b = "background-color: black; color: white;" 
        self.chromatic_colors = [self.w, self.b, self.w, self.b, self.w, self.w, 
                                 self.b, self.w, self.b, self.w, self.b, self.w]


        for btn, radio, val, slide in zip(self.ac_buttons_list, self.ac_radio_list, self.ac_val_list, self.ac_slide_list):

            radio.setAutoExclusive(False)
            btn.clicked.connect(radio.toggle)
            
            val.valueChanged.connect(slide.setValue)
            slide.valueChanged.connect(val.setValue)

            radio.toggled.connect(slide.setEnabled)
            radio.toggled.connect(val.setEnabled)

            # Set initial enable/disable state at startup
            initial_state = radio.isChecked()
            slide.setEnabled(initial_state)
            val.setEnabled(initial_state)


        ui.type_w_i.addItems(scale_notation)
        ui.scale_nat_ch.addItems(Scale_type)
        ui.scale_slot.addItems(Sclae_slot)

        self.ui.type_w_i.currentTextChanged.connect(self.update_root_note)
        self.update_root_note()

        self.ui.scale_to_mruda.clicked.connect(self.prepare_scale)

        self.ui.scale_b1.setEnabled(False)
        self.ui.scale_r1.setChecked(True)
        self.ui.scale_r1.setEnabled(False)
        self.ui.scale_sb1.setEnabled(False)
        self.ui.scale_s1.setEnabled(False)


        for slide, radio, val in zip(self.ac_slide_list, self.ac_radio_list, self.ac_val_list):
            slide.sliderReleased.connect(self.prepare_scale)
            radio.toggled.connect(self.prepare_scale)
            val.editingFinished.connect(self.prepare_scale)


        self.ui.type_w_i.currentTextChanged.connect(self.prepare_scale)
        self.ui.scale_nat_ch.currentTextChanged.connect(self.prepare_scale)




    def update_root_note(self):

        note_type = self.ui.type_w_i.currentText()

        print(note_type)

        if note_type == "Indian":
            final_notes = self.indian_notes 
            
        elif note_type == "Western":
            final_notes = self.chromatic_notes

        for btn, name, color in zip(self.ac_buttons_list, final_notes,  self.chromatic_colors):
            btn.setText(name)
            btn.setStyleSheet(color)


    def prepare_scale(self):

        active_slider_values = []

        

        if self.ui.type_w_i.currentText() == "Indian":
            active_slider_values.append(1)
        else:
            active_slider_values.append(0)


        for active, slide in zip(self.ac_radio_list, self.ac_slide_list):
                    if active.isChecked():
                        slide_value = slide.value()
                        active_slider_values.append(1)
                        active_slider_values.append(slide_value)

                    else:
                        active_slider_values.append(0)
                        active_slider_values.append(0)


        active_slider_values = [int(val) + 64 for val in active_slider_values]

        padd = 30 - len(active_slider_values)
        active_slider_values.extend([64]*padd)

        active_slider_values = [self.ui.scale_slot.currentIndex()+20]+active_slider_values

        print(active_slider_values)

        sysex_payload = [0x7D, 0x01] + active_slider_values
        # Create and send the message
        msg = mido.Message('sysex', data=sysex_payload)
        self.conn.outport.send(msg)

