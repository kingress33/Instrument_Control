import pyvisa
import time

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
        self.instrument = self.rm.open_resource(self.resource_address)
        print("Connected to MSO64B.")
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
            print("MSO64B connection closed.")
        else:
            print("No instrument to close.")

    def clear(self):
        if self.instrument:
            self.instrument.write(f':CLEAR')
            time.sleep(0.3)  # 在命令之間暫停0.5
            print(f"clear acquistions, measuremetns, and waveforms")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_channel_state(self, channel, state):
        #將通道顯示在示波器畫面
        if self.instrument:
            self.instrument.write(f':DIS:WAVEVIEW1:{channel}:STATE {state}') 
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"display {channel}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_channel_state(self, channel):
        if self.instrument:
            self.instrument.write(f':DIS:WAVEVIEW1:{channel}:STATE?') 
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            return float(self.instrument.read())
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

    def query_acquistion_num(self):
        if self.instrument:
            self.instrument.write(f':ACQuire:NUMAVg?')
            time.sleep(0.05)
            return self.instrument.read()
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

    def probe_bandwidth_limit(self, channel, bandwidth_limit):
        # 設定探棒的頻寬限制
        if self.instrument:
            self.instrument.write(f':{channel}:BANdwidth {bandwidth_limit}')
            print(f"Set {channel} Bandwidth Limit to {bandwidth_limit}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_bandwidth_limit(self, channel):
        # 查詢探棒的頻寬限制
        if self.instrument:
            self.instrument.write(f':{channel}:BANdwidth?')
            return self.instrument.read()
        else:
            raise Exception("Instrument not connected. Please connect first.")
            
    def measure_delay(self, meas, source1, source2):
        if self.instrument:
            # 將命令連接在一起，減少單獨發送命令的次數
            type_CMD = f":MEASUrement:{meas}:TYPE DELAY" #測量類型CMD
            source1_CMD = f":MEASUrement:{meas}:SOURCE1 {source1}" #訊號源1CMD
            source2_CMD = f":MEASUrement:{meas}:SOURCE2 {source2}" #訊號源2CMD
            command = (f"{type_CMD};{source1_CMD};{source2_CMD};") #完整叫出DELAY的CMD
            self.instrument.write(command) #寫入儀器
            time.sleep(0.05) # 在命令之間暫停0.1秒
            print(f"Add {meas} to measure delay of {source1} to {source2}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def measure_amplitude(self, meas, source):
        if self.instrument:
            type_CMD = f":MEASUrement:{meas}:TYPE AMPLitude" #測量類型CMD
            source_CMD = f":MEASUrement:{meas}:SOURCE {source}" #訊號源CMD
            command = f"{type_CMD};{source_CMD}" #完整叫出AMPLITUDE的CMD
            self.instrument.write(command) #寫入儀器
            time.sleep(0.05) # 在命令之間暫停0.1秒
            print(f"Add {meas} to measure Amplitude of {source}")
        else:
            raise Exception("Instrument not connected. Please connect first.")   

    def result_table(self):
        if self.instrument:
            self.instrument.write(f':MEASTABle:ADDNew "TABLE1"')
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"add measurent result table")
        else:
            raise Exception("Instrument not connected. Please connect first.")
          
    def query_scale(self):
        if self.instrument:
            return self.instrument.query(f":MEASUrement:MEAS10:RESUlts:CURRentacq:MAXimum?")
            time.sleep(0.05) # 在命令之間暫停0.1秒
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_horizon_scale(self, horizon_scale):
        if self.instrument:
            self.instrument.write(f':HORizontal:MODe MANual') #將Horizontal模式切為Manual
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            self.instrument.write(f':HORIZONTAL:MODE:SCALE {horizon_scale}') #設定示波器水平刻度(非整數)
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"set Horizontal Scale be {horizon_scale}s/div")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def detect_clip(self,clip_check):
        if self.instrument:
            return self.instrument.query(f":{clip_check}:CLIPping?")
            time.sleep(0.05)  # 在命令之間暫停0.5秒
        else:
            raise Exception("Instrument not connected. Please connect first.")
            
    def query_vertical_scale(self,clip_check):
        if self.instrument:
            return self.instrument.query(f":{clip_check}:SCAle?")
            time.sleep(0.05)  # 在命令之間暫停0.5秒
        else:
            raise Exception("Instrument not connected. Please connect first.")
    
    def set_vertical_scale(self, clip_channel, new_vertical_value):
        if self.instrument:
            self.instrument.write(f":{clip_channel}:SCAle {new_vertical_value}")
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"set {clip_channel} vertical scale be {new_vertical_value}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_population(self):
        if self.instrument:
            self.instrument.write(f'MEASUrement:MEAS3:RESUlts:ALLAcqs:POPUlation?')
            time.sleep(0.05)
            return int(self.instrument.read())
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_mean_value(self, meas):
        if self.instrument:                    
            self.instrument.write(f'MEASUrement:{meas}:RESUlts:ALLAcqs:MEAN?')
            time.sleep(0.05)
            return float(self.instrument.read())
        else:
             raise Exception("Instrument not connected. Please connect first.")

    def set_deskew_zero(self):
        if self.instrument:
            self.instrument.write(f'CH2:DESKEW 0')
            print(f"CH2 deskew set to 0")
            self.instrument.write(f'CH3:DESKEW 0')
            print(f"CH3 deskew set to 0")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")
    
    def set_deskew(self, delay_ch1, delay_ch2):
        if self.instrument:
            self.instrument.write(f'CH2:DESKEW {delay_ch1}')
            print(f"deskew ch2: {delay_ch1}")
            time.sleep(0.05)
            self.instrument.write(f'CH3:DESKEW {delay_ch2}')
            print(f"deskew ch3: {delay_ch2}")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_attenuation_unit(self):
        if self.instrument:
            self.instrument.write(f'CH1:PROBEFunc:EXTAtten 1')
            print(f"set external attenuation of CH1 be 1")
            time.sleep(0.05)
            self.instrument.write(f'CH2:PROBEFunc:EXTAtten 1')
            print(f"set external attenuation of CH2 be 1")
            time.sleep(0.05)
            self.instrument.write(f'CH3:PROBEFunc:EXTAtten 1')
            print(f"set external attenuation of CH3 be 1")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")
    
    def set_attenuation(self, ratio, meas):
        if self.instrument:
            self.instrument.write(f'{meas}:PROBEFunc:EXTAtten {ratio}')
            print(f"set external attenuation of {meas} be {ratio}")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def measure_mean(self,meas,source):
        if self.instrument:       #新增CH1、CH2、CH3的MEAN測量值
            type_CMD = f":MEASUrement:{meas}:TYPE MEAN" #測量類型CMD
            source_CMD = f":MEASUrement:{meas}:SOURCE {source}" #訊號源CMD
            command = f"{type_CMD};{source_CMD}" #完整叫出AMPLITUDE的CMD
            self.instrument.write(command) #寫入儀器
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"add measurent {meas} of {source}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_gating_type(self):
        if self.instrument:
            #設定measurement中Gating type
            self.instrument.write(f'MEASUrement:GATing CURSor')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"take measurements on the portion of the waveform between the cursor")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def math_add(self, math_num, math_function):
        if self.instrument:
            #新增math formula
            self.instrument.write(f':MATH:ADDNew "{math_num}"')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            self.instrument.write(f':MATH:{math_num}:DEFine "{math_function}"')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"Add {math_num} to calculate {math_function}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_math_autoscale(self):
        if self.instrument:
            #新增math formula
            self.instrument.write(f':DISplay:WAVEView1:MATH:MATH4:AUTOScale ON')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"enables the autoscaling the math4 in the specified Waveform View")
            self.instrument.write(f':DISplay:WAVEView1:MATH:MATH5:AUTOScale ON')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"enables the autoscaling the math5 in the specified Waveform View")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_math_unit(self, math_num, unit_name):
        if self.instrument:
            #新增math formula
            self.instrument.write(f':MATH:{math_num}:VUNIT "{unit_name}" ')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"set unit of {math_num} be {unit_name} ")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_cursor(self, cursor_A_position, cursor_B_position):
        if self.instrument:
            #設定cursor範圍為三個波形週期
            self.instrument.write(f':DISplay:WAVEView1:CURSor:CURSOR1:STATE ON')
            self.instrument.write(f':DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:APOSition {cursor_A_position}')
            self.instrument.write(f':DISplay:WAVEView1:CURSor:CURSOR1:WAVEform:BPOSition {cursor_B_position}')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"set cursor range be {cursor_A_position} to {cursor_B_position}")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def measure_delta_B(self):
        if self.instrument:
            #新增測量磁通最大值及最小值的measurement
            self.instrument.write(f':MEASUREMENT:MEAS9:TYPE MAXIMUM; SOUrce MATH5') #新增math5的最大值
            time.sleep(0.05)  # 在命令之間暫停0.5秒           
            self.instrument.write(f':MEASUREMENT:MEAS10:TYPE MINIMUM; SOUrce MATH5') #新增math5的最小值
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"add measurent maximum of math5")
            print(f"add measurent minimum of math5")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def add_power_quality(self,num,voltage,current):
        if self.instrument:
            self.instrument.write(f'POWer:POWer{num}:TYPe POWERQUALITY') 
            time.sleep(0.05) 
            self.instrument.write(f':POWer:POWer{num}:POWERQUALITY:VSOURce {voltage}') 
            time.sleep(0.05)  # 在命令之間暫停0.5
            self.instrument.write(f':POWer:POWer{num}:POWERQUALITY:ISOURce {current}')
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"add power function of voltage:CH2/current:MATH4")
            print(f"add power function of voltage:CH3/current:MATH4")
        else:
            raise Exception("Instrument not connected. Please connect first.")
    
    def add_magnetic_property(self, core_length, core_area):
        if self.instrument:
            self.instrument.write(f'POWer:POWer3:TYPe MAGPROPERTY') 
            time.sleep(0.05) 
            self.instrument.write(f':POWer:POWer3:MAGPROPERTY:VSOURce MATH2') 
            time.sleep(0.05)  # 在命令之間暫停0.5
            self.instrument.write(f':POWer:POWer3:MAGPROPERTY:ISOURce MATH4')
            time.sleep(0.05)  # 在命令之間暫停0.5
            self.instrument.write(f':POWer:POWer3:MAGPROPERTY:LENgth {core_length}e-3')
            time.sleep(0.05)  # 在命令之間暫停0.5
            self.instrument.write(f':POWer:POWer3:MAGPROPERTY:AREAofcrosssection {core_area}e-6') 
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"add magnetic property of core voltage:CH2/current:MATH4")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def plot_BH_curve(self):
        if self.instrument:
            self.instrument.write(f':PLOT:PLOT2:TYPe MAGPROPERTY') 
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"plot BH curve of core")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def save_plot_data(self):
        if self.instrument:
            self.instrument.write(f':SAVe:PLOTData plot1.csv') 
            time.sleep(0.05)  # 在命令之間暫停0.5
            print(f"Save plot1 csv data")
        else:
            raise Exception("Instrument not connected. Please connect first.")
        
    def off_display(self, off_math):  
        if self.instrument:
            #將不必要的波形關閉
            # self.instrument.write(f':DIS:WAVEVIEW1:{off_channel}:STATE OFF')
            # time.sleep(0.05)  # 在命令之間暫停0.5秒
            # print(f"turn {off_channel} display off")
            self.instrument.write(f':DISplay:WAVEView1:MATH:{off_math}:STATE OFF')
            time.sleep(0.05)  # 在命令之間暫停0.5秒
            print(f"turn {off_math} display off")
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_CH1_deskew(self, deskew_ch1):
        if self.instrument:
            self.instrument.write(f'CH1:DESKEW {deskew_ch1}')
            print(f"CH1 deskew set to {deskew_ch1}")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def set_CH1_deskew_zero(self):
        if self.instrument:
            self.instrument.write(f'CH1:DESKEW 0')
            print(f"CH1 deskew set to 0")
            time.sleep(0.05)
        else:
            raise Exception("Instrument not connected. Please connect first.")

    def query_mean_value(self, meas):
        if self.instrument:                  
            self.instrument.write(f'MEASUrement:{meas}:RESUlts:CURRentacq:MEAN?')
            time.sleep(0.05)
            return float(self.instrument.read())
        else:
             raise Exception("Instrument not connected. Please connect first.")

    def query_true_power(self, power_num):
        if self.instrument:
            self.instrument.write(f'POWer:POWer{power_num}:RESUlts:CURRentacq:MEAN? "TruePWR"')
            time.sleep(0.05)
            return float(self.instrument.read())
        else:
             raise Exception("Instrument not connected. Please connect first.")

