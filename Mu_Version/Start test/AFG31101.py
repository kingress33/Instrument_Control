#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pyvisa
import time

class AFG_31101():
    def __init__(self, resource_address, visa_dll=None):
        """
        初始化儀器控制器。
        :param resource_address: 儀器的資源地址。
        :param visa_dll: 使用的 VISA DLL 路徑。如果為 None，則使用系統預設空白。
        """
        self.resource_address = resource_address
        self.visa_dll = visa_dll if visa_dll is not None else ''
        self.rm = pyvisa.ResourceManager(self.visa_dll)
        self.instrument = None
        self.connect_to_instrument()
        
    def connect_to_instrument(self):
        # 建立與儀器的連接
        self.instrument = self.rm.open_resource(self.resource_address)
        print("Connected to AFG_31101.")
        print(self.query_identity())

    def query_identity(self):
         # 查詢並返回儀器的身份識別信息
        if self.instrument:
             return self.instrument.query("*IDN?")
        else:
             raise Exception("Instrument not connected. Please connect first.")

    def close_instrument(self):
        if self.instrument:
            self.instrument.close()
            print("AFG_31101 connection closed.")
        else:
            print("No instrument to close.")

    def set_waveform(self, shape):
        if self.instrument:
            self.instrument.write(f"SOURce1:FUNCtion {shape}")
            time.sleep(0.05)
            print(f"set signal form be {shape}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_frequency(self, freq_amplitude, freq_unit):
        if self.instrument:
            self.instrument.write(f"SOURce1:FREQuency:FIXed {freq_amplitude} {freq_unit}")
            time.sleep(0.05)
            print(f"set signal frequency be {freq_amplitude}{freq_unit}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_frequency(self):
        if self.instrument:
            self.instrument.write(f"SOURce1:FREQuency:FIXed?")
            time.sleep(0.05)
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_amplitude(self, amp_magnitude, amp_unit):
        if self.instrument:
            self.instrument.write(f"SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {amp_magnitude}{amp_unit}")
            time.sleep(0.05)
            print(f"set signal amplitude be {amp_magnitude}{amp_unit}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_amplitude(self):
        if self.instrument:
            self.instrument.write(f"SOURce1:VOLTage:LEVel:IMMediate:AMPLitude?")
            time.sleep(0.05)
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")
    
    def output_on(self):
        if self.instrument:
            self.instrument.write(f"OUTPut1:STATe ON")
            time.sleep(0.05)
            print(f"turn AFG31101 output on")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def output_off(self):
        if self.instrument:
            self.instrument.write(f"OUTPut1:STATe OFF")
            time.sleep(0.05)
            print(f"turn AFG31101 output off")
        else:
            raise Exception("Instrument not connected. Please connect first.")





