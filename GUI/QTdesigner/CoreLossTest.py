# Form implementation generated from reading ui file 'CoreLossTest.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1028, 740)
        self.Resource_QWidget = QtWidgets.QWidget(parent=MainWindow)
        self.Resource_QWidget.setObjectName("Resource_QWidget")
        self.Resource_group = QtWidgets.QGroupBox(parent=self.Resource_QWidget)
        self.Resource_group.setGeometry(QtCore.QRect(520, 30, 471, 251))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(14)
        self.Resource_group.setFont(font)
        self.Resource_group.setStyleSheet("QGroupBox {\n"
"    border: 1.5px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 10px;  /* 增加內邊距，讓內容與邊框保持距離 */\n"
"    margin-top: 10px;  /* 確保標題與內容之間有適當距離 */\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;  /* 調整標題的位置 */\n"
"    padding: 0 10px;  /* 給標題添加左右間距 */\n"
"}\n"
"")
        self.Resource_group.setObjectName("Resource_group")
        self.address_illustrate = QtWidgets.QLabel(parent=self.Resource_group)
        self.address_illustrate.setGeometry(QtCore.QRect(20, 40, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        self.address_illustrate.setFont(font)
        self.address_illustrate.setWordWrap(True)
        self.address_illustrate.setObjectName("address_illustrate")
        self.layoutWidget = QtWidgets.QWidget(parent=self.Resource_group)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 90, 431, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scope = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.scope.setFont(font)
        self.scope.setObjectName("scope")
        self.gridLayout.addWidget(self.scope, 0, 0, 1, 1)
        self.Scope_address = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.Scope_address.setObjectName("Scope_address")
        self.gridLayout.addWidget(self.Scope_address, 0, 1, 1, 1)
        self.FG = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.FG.setFont(font)
        self.FG.setObjectName("FG")
        self.gridLayout.addWidget(self.FG, 1, 0, 1, 1)
        self.FG_address = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.FG_address.setObjectName("FG_address")
        self.gridLayout.addWidget(self.FG_address, 1, 1, 1, 1)
        self.amp = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(10)
        self.amp.setFont(font)
        self.amp.setObjectName("amp")
        self.gridLayout.addWidget(self.amp, 2, 0, 1, 1)
        self.Amp_address = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.Amp_address.setObjectName("Amp_address")
        self.gridLayout.addWidget(self.Amp_address, 2, 1, 1, 1)
        self.adddress_refresh = QtWidgets.QPushButton(parent=self.Resource_group)
        self.adddress_refresh.setGeometry(QtCore.QRect(190, 210, 93, 28))
        self.adddress_refresh.setObjectName("adddress_refresh")
        MainWindow.setCentralWidget(self.Resource_QWidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Resource_group.setTitle(_translate("MainWindow", "Resoures Address"))
        self.address_illustrate.setText(_translate("MainWindow", "Make sure Scope address, Power Amplifier and Function Generator address are correct before recalling setup"))
        self.scope.setText(_translate("MainWindow", "Scope:"))
        self.FG.setText(_translate("MainWindow", "Function Generotor:"))
        self.amp.setText(_translate("MainWindow", "Power Amplifier:"))
        self.adddress_refresh.setText(_translate("MainWindow", "Refresh"))