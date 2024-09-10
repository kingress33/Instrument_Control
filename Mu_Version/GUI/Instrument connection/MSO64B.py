class MSO_64B():
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
        try:
            self.instrument = self.rm.open_resource(self.resource_address)
            print("Connected to MSO64B.")
            print(self.query_identity())
        except Exception as e:
            print(f"Failed to connect to instrument: {e}")
            self.instrument = None
        
    def query_identity(self):
         # 查詢並返回儀器的身份識別信息
        if self.instrument:
             return self.instrument.query("*IDN?")
        else:
             raise Exception("Instrument not connected. Please connect first.")

    def close_instrument(self):
        if self.instrument:
            self.instrument.close()
            print("MSO64B connection closed.")
        else:
            print("No instrument to close.")






