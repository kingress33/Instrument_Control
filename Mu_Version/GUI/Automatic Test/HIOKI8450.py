import pyvisa
import time

class HIOKI_8450():
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
        print("Connected to HIOKI8450.")
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
            print("HIOKI8450 connection closed.")
        else:
            print("No instrument to close.")

    def set_channel(self, channel, state):
        if self.instrument:
            #選擇模組中的通道是否顯示測量
            self.instrument.write(f":UNIT:STORe {channel},{state}")
            print(f"set {channel} {state}")
        else:
            print("No instrument to close.")

    def set_measurement_mode(self, channel, mode):
        if self.instrument:
            #設定測量通道的模式 [電壓、熱電偶、濕度]
            self.instrument.write(f":UNIT:INMOde {channel},{mode}")
            print(f"set mode of {channel} be {mode}")
        else:
            print("No instrument to close.")

    def set_rtd_type(self, channel, rtd_type):
        if self.instrument:
            #設定熱電偶線的類型[K、J、E、T、N、R、S、C]
            self.instrument.write(f":UNIT:SENSor {channel},{rtd_type}")
            print(f"set the sensor kind for the {channel} be {rtd_type}")
        else:
            print("No instrument to close.")

    def query_data(self):
        if self.instrument:
            #直接顯示unit1此模組當下測量的所有數據
            self.instrument.write(f":MEMory:TVREAL? UNIT1")
            time.sleep(0.05)
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")





