import pyvisa
import time

class RF_150A100D():
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
        print("Connected to RF150A100D.")
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
            print("Instrument connection closed.")
        else:
            print("No instrument to close.")

    def power_on(self):
        if self.instrument:
            self.instrument.write(f"P1")
            print(f"turn RF150A100D power on")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def power_off(self):
        if self.instrument:
            self.instrument.write(f"P0")
            print(f"turn RF150A100D power off")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_gain(self, gain ,gain_set):
        if self.instrument:
            self.instrument.write(f"G{gain_set}")
            print(f"set power gain be {gain}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_gain(self):
        if self.instrument:
            self.instrument.write(f"G?")
            time.sleep(0.05)
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_state(self):
        if self.instrument:
            self.instrument.write(f"STATE?")
            time.sleep(0.05)
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")

    """
    POWER:ON/Local control--0301
    POWER:OFF/Local control--0201
    POWER:ON/Remote control--8301
    POWER:OFF/Remote control--8201
    """





