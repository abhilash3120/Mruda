import mido


def send_test_setting():
    outport_name = None
    # Find the keyboard
    for n in mido.get_output_names():
        if "STM32" in n: # Change this if your device name is different
            outport_name = n
            
    if not outport_name:
        print("Keyboard not found!")
        return

    outport = mido.open_output(outport_name)

    # Build the SysEx Message
    # 0x7D = Our ID, 0x01 = Command, 0x32 = Value
    msg = mido.Message('sysex', data=[100, 125, 77])

    print("Sending setting to keyboard...")
    outport.send(msg)
    print("Sent!")
    outport.close()

send_test_setting()