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

    def display_channel(self, channel, state):
        #將通道顯示在示波器畫面
        if self.instrument:
            self.instrument.write(f':DIS:WAVEVIEW1:{channel}:STATE {state}') 
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"Turn {channel} {state}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_acquistion(self, acquistion_num):
        #設定採樣模式及數量
        if self.instrument:
            self.instrument.write(f':ACQuire:MODe AVE;:ACQuire:NUMAVg {acquistion_num}')
            #設定Acquistion mode為average並波形獲取數量為128
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"set acquisition in average mode and waveform acquire number be {acquistion_num}")
        else:
            raise Exception("Instrument not connected. Please connect first.") 

    def probe_autozero(self, channel):
        #將探棒Auto Zero調整波形位準
        if self.instrument:
            self.instrument.write(f':{channel}:PRObe:AUTOZero EXECute')
            time.sleep(0.05)  
            print(f"set probe in {channel} Auto Zero")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def probe_correction(self, channel, limit):
        #設定探棒的頻寬限制
        if self.instrument:
            self.instrument.write(f':{channel}:BANdwidth {limit}')
            print(f"set {channel} Bandwidth Limit be {limit}E+06")
        else:
            raise Exception("Instrument not connected. Please connect first.") 






