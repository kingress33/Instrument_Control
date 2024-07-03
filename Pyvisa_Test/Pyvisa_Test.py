# 引入套件
import tkinter as TK
import tkinter.ttk as TTK
import pyvisa  as VS
import re

Magnitude_Symbol  = {"+12" : "T", "+09" : "G", "+06" : "M", "+03" : "k",
                     "-03" : "m", "-06" : "u", "-09" : "n", "-12" : "p"}

Magnitude_Symbol  = dict((re.escape(k), v) for k, v in Magnitude_Symbol.items())
Magnitude_replace = re.compile("|".join(Magnitude_Symbol.keys()))

Combo_Test = ["1", "2", "3"]
bu = ["2", "1", "0"]

Top_Buttons          = ["Root_Scan_Button", "AutoSet_Button", "Single_Button", "SS_Button"]
Top_Buttons_Function = ["Root_Scan"       , "AutoSet"       , "Single"       , "SS"       ]

class Oscallarator_GUI():
    def __init__(self, master):
        #Create a Label
        self.Equipment_Label = TK.Label(master, height = 2)
        self.Equipment_Label.config(text = "Scanning\nEquipment...", justify = "left")
        self.Equipment_Label.grid(row = 0, column = 0, padx = 20, pady = 9, sticky = "nw")
        #Create a Scan button
        self.Scan_Button = TTK.Button(master)
        self.Scan_Button.config(text = "Scan", command = self.Scan)
        self.Scan_Button.grid(row = 0, column = 1, padx = 16, pady = 9)
        #Create a testing button
        self.Test_Button = TTK.Button(master)
        self.Test_Button.config(text = "Test", command = self.Test)
        self.Test_Button.grid(row = 0, column = 2, padx = 16, pady = 9)
        #Create a combo box
        self.Test_Combobox = TTK.Combobox(master)
        self.Test_Combobox.config(value = Combo_Test, width = 5)
        self.Test_Combobox.grid(row = 0, column = 3, padx = 16, pady = 9)
    #Scan Equipment then chage the Label
    def Scan(self):
        self.RM = VS.ResourceManager()
        self.Equipment_List  = self.RM.list_resources()
        print(self.Equipment_List[0])
        # Connect not by Serial/Prellel Port
        if "ASRL" not in self.Equipment_List:
            try:
                self.Equipment_Now   = self.RM.open_resource(self.Equipment_List[0])
                self.Equipment_Model = self.Equipment_Now.query('*IDN?')
            except:
                self.Equipment_Label.config(text = "Error: Not Connect\n %s" %self.Equipment_List)
            else:
                self.Equipment_Label.config(text = self.Equipment_Model)
                print(self.Equipment_Model)
    #Test Button Function
    def Test(self):
        self.Equipment_Now.write("CHAN 5")
        print(self.Equipment_Now.query("CHAN?"))
        
        self.Equipment_Now.write("LOAD ON")
        print(self.Equipment_Now.query("Load?"))
#Only execute while running this file
if __name__ == "__main__":    
    root = TK.Tk()
    root.title("Oscallarator Equipment Processing")
    root.geometry("854x480")
    root.resizable(width = False, height = False)
    root.config(bg = "snow")
    try:
        pass
    except:
        bu = ["a",""]

    # Create GUI inside window and run fuction  
    Oscallarator_GUI(root)
    # Continue reflesh window
    root.mainloop()