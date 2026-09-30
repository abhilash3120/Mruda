from PySide6.QtWidgets import QComboBox, QSpinBox, QDoubleSpinBox
raag_list = ["Natural",
"Chromatic",
"Thaat_Bilawal",
"Thaat_Kalyan",
"Thaat_Khamaj",
"Thaat_Kafi",
"Thaat_Asavari",
"Thaat_Bhairavi",
"Thaat_Bhairav",
"Thaat_Marva",
"Thaat_Purvi",
"Thaat_Todi",
"Raag_Abhogi",
"Raag_Ahir_bhairav",
"Raag_Bageshri",
"Raag_Bhairav",
"Raag_Bhairavi",
"Raag_Bhimpalasi",
"Raag_Bhupali",
"Raag_Bihag",
"Raag_Charukeshi",
"Raag_Darbari_kanada",
"Raag_Desh",
"Raag_Durga",
"Raag_Hamsadhwani",
"Raag_Jog",
"Raag_Jonpuri",
"Raag_Kalavati",
"Raag_Kedar",
"Raag_Khamaj",
"Raag_Kirvani",
"Raag_Lalit",
"Raag_Malkauns",
"Raag_Marwa",
"Raag_Megh_Malhar",
"Raag_Miya_ki_malhar",
"Raag_Nand",
"Raag_Pahadi",
"Raag_Pilu",
"Raag_Puriya_Dhanashree",
"Raag_Raagshree",
"Raag_Sarang",
"Raag_Shivranjini",
"Raag_Shree",
"Raag_Tilak_Kamod",
"Raag_Tilang",
"Raag_Yaman",
"Scale_Custom_1",
"Scale_Custom_2",
"Scale_Custom_3"
]

class set_Default():
    def __init__(self, ui, conn_class):

        self.ui = ui
        self.conn = conn_class

        self.ui.d_midi.addItems(["On","Off"])
        self.ui.d_transpose.addItems(['-7','-6','-5','-4','-3','-2','-1','0','1','2','3','4','5','6','7'])
        self.ui.d_octave.addItems(['-3','-2','-1','0','1','2','3'])
        self.ui.d_tune.setValue(0)
        self.ui.d_tsens.addItems(['1','2','3','4','5'])
        self.ui.d_reverb.addItems(['1','2','3','4','5'])
        self.ui.d_sustain.addItems(['1','2','3','4','5'])
        self.ui.d_voice_def.addItems(['1','2','3','4','5'])
        self.ui.d_voice_p1.addItems(['1','2','3','4','5'])
        self.ui.d_voice_p2.addItems(['1','2','3','4','5'])
        self.ui.d_auto_corr.addItems(['0','1','2','3','4','5'])
        self.ui.d_ac_boot.addItems(raag_list)
        self.ui.d_ac_s1.addItems(raag_list)
        self.ui.d_ac_s2.addItems(raag_list)
        self.ui.d_tanpura_state.addItems(['On','Off'])
        self.ui.d_tanpura_scale.addItems(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
        self.ui.d_tanpura_vol.addItems(['1','2','3','4','5','6','7','8','9'])
        self.ui.d_tanpura_sec.addItems(['PA','ma (Suddh)','ni (Komal)','NI (suddh)'])

        self.default_list = [self.ui.d_midi, self.ui.d_transpose, self.ui.d_octave, self.ui.d_tune,
                        self.ui.d_tsens, self.ui.d_reverb, self.ui.d_sustain, 
                        self.ui.d_voice_def, self.ui.d_voice_p1, self.ui.d_voice_p2,
                        self.ui.d_auto_corr, self.ui.d_ac_boot, self.ui.d_ac_s1, self.ui.d_ac_s2,
                        self.ui.d_tanpura_state, self.ui.d_tanpura_scale, self.ui.d_tanpura_vol, self.ui.d_tanpura_sec]

        # These are now all INTEGERS representing the index (for comboboxes) 
        # or the value (for spinboxes)
        self.default_values = [
            1,   # d_midi (Index 1 = "Off")
            7,   # d_transpose (Index 7 = "0")
            3,   # d_octave (Index 3 = "0")
            0,   # d_tune (SpinBox value = 0)
            1,   # d_tsens (Index 1 = "2")

            1,   # d_reverb (Index 1 = "2")
            1,   # d_sustain (Index 1 = "2")
            0,   # d_voice_def (Index 0 = "0")
            1,   # d_voice_p1 (Index 1 = "1")
            2,   # d_voice_p2 (Index 2 = "2")

            3,   # d_auto_corr (Index 3 = "3")
            0,   # scale at boot
            2,   # d_ac_s1
            3,   # d_ac_s2
            1,   # d_tanpura_state (Index 1 = "Off")

            0,   # d_tanpura_scale (Index 0 = "C")
            2,   # d_tanpura_vol (Index 2 = "3")
            0    # d_tanpura_sec (Index 0 = "PA")
        ]


        self.apply_defaults(self.default_values)

        ui.set_default.clicked.connect(lambda:self.apply_defaults(self.default_values))
        ui.default_send.clicked.connect(self.send_default)





    def apply_defaults(self, values_list=None):
        """Applies a list of integers to the UI."""
        
        # If no list is passed, use the defaults
        if values_list is None:
            values_list = self.default_values
            
        for widget, val in zip(self.default_list, values_list):
            widget.blockSignals(True)

            if isinstance(widget, QComboBox):
                # Use setCurrentIndex instead of setCurrentText
                widget.setCurrentIndex(int(val))

            elif isinstance(widget, (QSpinBox, QDoubleSpinBox)):
                # SpinBoxes still use setValue
                widget.setValue(float(val) if isinstance(widget, QDoubleSpinBox) else int(val))

            widget.blockSignals(False)


    def send_default(self):
        extracted_values = []

        
        for widget in self.default_list:
            if isinstance(widget, QComboBox):
                # Use currentIndex() to get the integer for your STM32
                # (Or use widget.currentText() if you want the actual word)
                extracted_values.append(widget.currentIndex())
                
            elif isinstance(widget, QSpinBox):
                # QLineEdit always gives you a string
                text_value = widget.value()
                extracted_values.append(text_value)

        extracted_values[0]  = 1- extracted_values[0]
        extracted_values[1] -= 7
        extracted_values[2] -= 3
        extracted_values[13]  = 1- extracted_values[13]


        extracted_values = [int(val) + 64 for val in extracted_values]
        extracted_values = [30]+extracted_values
        print(f"Read values: {extracted_values}")

        import mido

        sysex_payload = [0x7D, 0x01] + extracted_values
        # Create and send the message
        msg = mido.Message('sysex', data=sysex_payload)
        self.conn.outport.send(msg)
