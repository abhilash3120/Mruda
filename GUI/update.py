

from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QMessageBox, QApplication
from main import setup

from PySide6.QtWidgets import QMessageBox , QTextEdit# or PySide2/PySide6/PyQt6
from PySide6.QtCore import QProcess, QTimer
import serial
import serial.tools.list_ports
import time

import os

# Protocol commands matching STM32
CMD_conn_done = b'\x05'
CMD_START = b'\x01'
CMD_DATA  = b'\x02'
CMD_DONE  = b'\x03'
ACK       = b'\x06'
CHUNK_SIZE = 60  # Match USB packet size


class firmware_update():
    def __init__(self, ui):
        self.ui = ui
        self.firmware_path = None
        self.midi = setup(ui)


        self.ui.text_log.setReadOnly(True)
        self.ui.text_log.document().setMaximumBlockCount(50)

        ui.sel_file.clicked.connect(self.select_firmware)
        ui.flash_mrida.clicked.connect(self.flash_firmware)
        ui.update_find.clicked.connect(self.find_and_connect_bootloader)
        ui.flash_connect.clicked.connect(self.connect_port)


        self.port_list = list(serial.tools.list_ports.comports())
        ui.com_list.addItems([port.device for port in self.port_list])
        ui.progressBar.setValue(0)


        


        

    def log_message(self, message: str):
        self.ui.text_log.append(message)


    def connect_port(self):
        try:
            ser = serial.Serial(
                port=self.ui.com_list.currentText(),
                baudrate=115200,
                timeout=1
            )
            self.ser = ser
            time.sleep(0.5)

            self.ser.reset_input_buffer()
            self.ser.reset_output_buffer()

            packet = CMD_conn_done

            self.ser.write(packet)
            self.ser.flush()
            
        except Exception as e:
            self.log_message(f"Error: {e}")

        



    def select_firmware(self):
        self.log_message("Select Firmware")

        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Select Firmware File",
            "",
            "Firmware Files (*.bin)"
        )

        if file_path:
            self.firmware_path = file_path

        self.ui.path.setText(self.firmware_path)


    

    def find_and_connect_bootloader(self):
        self.log_message("Connecting...")
        QApplication.processEvents()

        # 1. Standard STMicroelectronics Hardware IDs
        # (0x0483 is ST's Vendor ID. 0x5740 is the default CubeMX USB CDC Product ID)
        STM32_VID = 0x0483
        STM32_PID = 0x5740
        
        # 2. Get all system serial ports
        ports = list(serial.tools.list_ports.comports())
        
        for port_info in ports:
            # 3. Check if the device plugged into this port is an STMicroelectronics chip
            if port_info.vid == STM32_VID and port_info.pid == STM32_PID:
                port_name = port_info.device
                self.log_message(f"Found STM32 device on: {port_name}")
                
                try:
                    # 4. Open the port directly
                    self.ser = serial.Serial(port_name, baudrate=115200, timeout=1.0)
                    
                    self.log_message(f" Success! STM32 connected on {port_name}.")
                    self.log_message("Select .bin file to flash")
                    packet = CMD_conn_done
                    self.ser.write(packet)

                    return 
                    
                except (serial.SerialException, PermissionError):
                    self.log_message(f"-> Found STM32 on {port_name} but it is busy/locked.")
                    return

        self.log_message("❌ Scan finished. No STM32 device found.")


    def flash_firmware(self):
        # 1. Validation checks
        if not hasattr(self, 'ser') or self.ser is None or not self.ser.is_open:
            self.log_message("❌ Error: Device not connected. Click 'Find and Connect' first.")
            return

        if not self.firmware_path:
            self.log_message("❌ Error: No firmware binary file selected.")
            return

        file_size = os.path.getsize(self.firmware_path)
        self.log_message(f"Starting Flash... Total size: {file_size} bytes")
        QApplication.processEvents()

        try:
            # 2. Send START command + 4-byte file size metadata
            self.ser.write(CMD_START + file_size.to_bytes(4, byteorder='little'))
            print(CMD_START + file_size.to_bytes(4, byteorder='little') )
            
            # Wait for STM32 to erase sectors and respond
            response = self.ser.read(1)
            print("reply:",response)
            if response != ACK:
                self.log_message("❌ Error: Bootloader rejected start command.")
                return

            self.log_message("Sectors Erased. Streaming blocks...")
            QApplication.processEvents()

            # 3. Stream binary chunks
            bytes_sent = 0
            with open(self.firmware_path, 'rb') as f:
                while bytes_sent < file_size:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break

                    # Pad the final block with 0xFF if it's smaller than CHUNK_SIZE
                    if len(chunk) < CHUNK_SIZE:
                        chunk = chunk.ljust(CHUNK_SIZE, b'\xFF')

                    # Write command byte + 64 bytes payload data
                    packat = CMD_DATA + chunk
                    
                    print("cmd:", CMD_DATA)
                    print("data:",chunk)
                    print(len(chunk))
                    print("packet:", packat)

                    self.ser.write(packat)
                    
                    


                    # Wait for ACK before shipping next block
                    response = self.ser.read(1)
                    print("reply:", response)
                    if response != ACK:
                        self.log_message(f"❌ Error: Lost sync at block {bytes_sent}")
                        return

                    bytes_sent += len(chunk)
                    
                    # Update progress in GUI seamlessly
                    percent = min(int((bytes_sent / file_size) * 100), 100)
                    self.log_message(f"Flashing: {percent}")
                    self.ui.progressBar.setValue(percent)
                    QApplication.processEvents()

            # 4. Send DONE command to execute jump
            self.log_message("Finishing up...")
            self.ser.write(CMD_DONE)
            self.ser.read(1) # Final acknowledgment consumption

            self.log_message("🎉 [SUCCESS] Flashing complete! App running.")
            self.log_message(" Device Restart Recomended.")
            self.ser.close()
            self.ser = None

        except Exception as e:
            self.log_message(f"❌ Serial Communication Failure: {str(e)}")