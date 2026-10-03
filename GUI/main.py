
import threading
from PySide6.QtWidgets import QMessageBox
import mido

slot_1 = [127,127,85,85,59,	25,	13,	17,	4,	8,	0,	4,	0,	4,	0,	4]
slot_2 = [1, 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
slot_3 = [1, 0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
slot_4 =  [1.0, 1.00, 1.0, 1.0, 1.00, 1.00, 1.000, 1.00, 1.000, 1.00, 1, 1.000, 1, 0.000, 0, 0.000]
slot_5 =  [64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64]
tanpura = [127,127,85,85,59,	25,	13,	17,	4,	8,	0,	4,	0,	4,	0,	4]



#  Mix || Feedback || damping
reverb_preset = [[0 ,0 ,0],   #off
                 [10,65,65],  #Studio
                 [20,80,45],  #Room
                 [40,88,30],  #cathedral
                 [65,96,20],  #Deep space
                 [80,98,10]   #Dreamy
                 ]

default_values = [slot_1, slot_2, slot_3, slot_4, slot_5, tanpura]
Current_values = [slot_1, slot_2, slot_3, slot_4, slot_5, tanpura]

class setup():
    def __init__(self, ui):
        self.ui = ui

        self.slider_list = [
            self.ui.s1, self.ui.s2, self.ui.s3, self.ui.s4,
            self.ui.s5, self.ui.s6, self.ui.s7, self.ui.s8,
            self.ui.s9, self.ui.s10, self.ui.s11, self.ui.s12,
            self.ui.s13, self.ui.s14, self.ui.s15, self.ui.s16
        ]

        self.value_list = [
            self.ui.v1, self.ui.v2, self.ui.v3, self.ui.v4,
            self.ui.v5, self.ui.v6, self.ui.v7, self.ui.v8,
            self.ui.v9, self.ui.v10, self.ui.v11, self.ui.v12,
            self.ui.v13, self.ui.v14, self.ui.v15, self.ui.v16
        ]
      
        self.device = None
        self.inport = None
        self.outport = None

        self.other_set_slider = [
            self.ui.slide_rev_feedback, self.ui.slide_rev_damp, self.ui.slide_rev_mix,
            self.ui.slide_voice_attack, self.ui.slide_voice_sustain, self.ui.slide_voice_timber]

        self.other_set_val = [
            self.ui.val_rev_feedback, self.ui.val_rev_damp, self.ui.val_rev_mix,
            self.ui.val_voice_attack, self.ui.val_voice_sustain, self.ui.val_voice_timber            
        ]

        for slider, value in zip(self.other_set_slider, self.other_set_val):
            slider.valueChanged.connect(value.setValue)
            value.valueChanged.connect(slider.setValue)


        for slider, value in zip(self.slider_list, self.value_list):
            slider.valueChanged.connect(value.setValue)
            value.valueChanged.connect(slider.setValue)


        ui.slot_list.addItems(["Preset 1", "Preset 2", "Preset 3", "Preset 4", "Preset 5", "Tanpura"])
        ui.comb_voice_rev.addItems(["Off", "Studio", "Room", "Cathedral" , "Deep Space" , "Dreamy"])
        ui.slot_list.setCurrentIndex(4)
        ui.update.clicked.connect(self.update_slot)
        ui.send.clicked.connect(self.send_values)
        ui.connection.clicked.connect(self.connect_usb)
        ui.def_but.clicked.connect(self.set_default)
        ui.Refresh.clicked.connect(self.dev_refresh)
        ui.flash.clicked.connect(self.save_to_flash)


        for slider in self.slider_list:
            slider.sliderReleased.connect(self.send_values)

        for slider in self.other_set_slider:
            slider.sliderReleased.connect(self.send_values)


        self.ui.comb_voice_rev.currentIndexChanged.connect(self.reverb_update)


        dev_list = mido.get_input_names()
        ui.device.addItems(dev_list)

        self.ui.slot_list.currentIndexChanged.connect(self.set_default)

        self.send_flag = 0
        


    def set_default(self):
        slot = self.ui.slot_list.currentIndex()
        Current_values[slot] = default_values[slot]

        data = [x * 1 for x in Current_values[slot]]
        for data, slider in zip(data, self.slider_list):
            slider.setValue(int(data))

            for slider in self.other_set_slider:
                if slot == 5:
                    slider.setEnabled(False)
                else:
                    slider.setEnabled(True)

            if slot ==5 :
                self.ui.comb_voice_rev.setEnabled(False)

            else :
                self.ui.comb_voice_rev.setEnabled(True)



    def dev_refresh(self):
        dev_list = mido.get_input_names()
        self.ui.device.clear()
        self.ui.device.addItems(dev_list)

        # auto-select STM32
        for i, n in enumerate(dev_list):
            if "STM32" in n:
                self.ui.device.setCurrentIndex(i)
                break


    def update_slot(self):
        slot = self.ui.slot_list.currentIndex()

        data =  Current_values[slot]
        for data, slider in zip(data, self.slider_list):
            slider.setValue(int(data))

    
    def send_values(self):

        command = self.ui.slot_list.currentIndex()
        values = [command] + [slider.value() for slider in self.slider_list] + [slider.value() for slider in self.other_set_slider] + 8*[0]
        #  16+6+8
        # keep total 30 spaces for future additions 

        

        print(values)
        sysex_payload = [0x7D, 0x01] + values

        # Create and send the message
        try:
            msg = mido.Message('sysex', data=sysex_payload)
            self.outport.send(msg)
            self.send_flag = 1

        except:
            QMessageBox.warning(
                None,
                "Info",
                "Please connect to Mruda.",
                QMessageBox.StandardButton.Ok
            )



    def find_ports(self):

        inport_name = None
        outport_name = None

        for n in mido.get_input_names():
            if "STM32" in n:
                inport_name = n

        for n in mido.get_output_names():
            if "STM32" in n:
                outport_name = n


        return inport_name, outport_name




    def connect_usb(self):

        in_name, out_name = self.find_ports()

        if not in_name:
            self.ui.status.setText("Device not found")
            return

        self.inport = mido.open_input(in_name)

        if out_name:
            self.outport = mido.open_output(out_name)
        else:
            self.outport = None

        self.ui.status.setText("Connected")
        self.start_listener()
        
        values = [99,10,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
        sysex_payload = [0x7D, 0x01] + values
        # Create and send the message
        msg = mido.Message('sysex', data=sysex_payload)
        self.outport.send(msg)



            
    def start_listener(self):

        def loop():
            print("MIDI listener started")

            for msg in self.inport:
                print("RX:", msg)


        self.midi_thread = threading.Thread(target=loop, daemon=True)
        self.midi_thread.start()


    def save_to_flash(self):


        preset = self.ui.slot_list.currentText()

        # Use the explicit StandardButton enum

        if self.send_flag == 0:
            QMessageBox.information(
                None,
                "Info",
                "Please send the values using the 'Send to Mruda' button before overwriting the Current values.",
                QMessageBox.StandardButton.Ok
            )
            return


        
        reply = QMessageBox.question(
            None,
            "Confirm",
            f"Overwrite {preset} with current value?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        # Compare against the explicit enum member
        if reply == QMessageBox.StandardButton.No:
            print("cancelled")
            return
        
        # If it reaches here, the user clicked 'Yes'
        print("Saving...")

        try:
            values = [100,1]
            sysex_payload = [0x7D, 0x01] + values
            msg = mido.Message('sysex', data=sysex_payload)
            self.outport.send(msg)

        except:
            QMessageBox.warning(
                None,
                "Info",
                "Please connect to Mruda.",
                QMessageBox.StandardButton.Ok
            )



    def send_data(self, values):
        try:
            sysex_payload = [0x7D, 0x01] + values
            msg = mido.Message('sysex', data=sysex_payload)
            self.outport.send(msg)

        except:
            QMessageBox.warning(
                None,
                "Info",
                "Please connect to Mruda.",
                QMessageBox.StandardButton.Ok
            )

    def reverb_update(self):
        print("reverb update")
        index = self.ui.comb_voice_rev.currentIndex()
        self.ui.slide_rev_feedback.setValue(reverb_preset[index][1])
        self.ui.slide_rev_damp.setValue(reverb_preset[index][2])
        self.ui.slide_rev_mix.setValue(reverb_preset[index][0])

