# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jeff_table_v1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_Window(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 800)
        Form.setStyleSheet("background-color: #F9F6EE; color: #254117")

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 150, 900, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(1)
    
        self.label_90 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_90.setFrameShape(QtWidgets.QFrame.Box)
        self.label_90.setAlignment(QtCore.Qt.AlignCenter)
        self.label_90.setObjectName("label_90")
        self.label_90.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_90, 9, 0, 1, 1)
        self.label_04 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_04.setFrameShape(QtWidgets.QFrame.Box)
        self.label_04.setAlignment(QtCore.Qt.AlignCenter)
        self.label_04.setObjectName("label_04")
        self.label_04.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_04, 0, 4, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_100.setFrameShape(QtWidgets.QFrame.Box)
        self.label_100.setAlignment(QtCore.Qt.AlignCenter)
        self.label_100.setObjectName("label_100")
        self.label_100.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_100, 10, 0, 1, 1)
        self.label_00 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_00.setFrameShape(QtWidgets.QFrame.Box)
        self.label_00.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_00.setObjectName("label_00")
        self.label_00.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_00, 0, 0, 1, 1)
        self.label_05 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_05.setFrameShape(QtWidgets.QFrame.Box)
        self.label_05.setAlignment(QtCore.Qt.AlignCenter)
        self.label_05.setObjectName("label_05")
        self.label_05.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_05, 0, 5, 1, 1)
        self.label_01 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_01.setFrameShape(QtWidgets.QFrame.Box)
        self.label_01.setAlignment(QtCore.Qt.AlignCenter)
        self.label_01.setObjectName("label_01")
        self.label_01.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_01, 0, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setFrameShape(QtWidgets.QFrame.Box)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_30, 3, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_80.setFrameShape(QtWidgets.QFrame.Box)
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.label_80.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_80, 8, 0, 1, 1)
        self.label_02 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_02.setFrameShape(QtWidgets.QFrame.Box)
        self.label_02.setAlignment(QtCore.Qt.AlignCenter)
        self.label_02.setObjectName("label_02")
        self.label_02.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_02, 0, 2, 1, 1)
        self.label_07 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_07.setFrameShape(QtWidgets.QFrame.Box)
        self.label_07.setAlignment(QtCore.Qt.AlignCenter)
        self.label_07.setObjectName("label_07")
        self.label_07.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_07, 0, 7, 1, 1)
        self.label_03 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_03.setFrameShape(QtWidgets.QFrame.Box)
        self.label_03.setAlignment(QtCore.Qt.AlignCenter)
        self.label_03.setObjectName("label_03")
        self.label_03.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_03, 0, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_40.setFrameShape(QtWidgets.QFrame.Box)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.label_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_40, 4, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_60.setFrameShape(QtWidgets.QFrame.Box)
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.label_60.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_60, 6, 0, 1, 1)
        self.label_06 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_06.setFrameShape(QtWidgets.QFrame.Box)
        self.label_06.setAlignment(QtCore.Qt.AlignCenter)
        self.label_06.setObjectName("label_06")
        self.label_06.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_06, 0, 6, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_70.setFrameShape(QtWidgets.QFrame.Box)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.label_70.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_70, 7, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setFrameShape(QtWidgets.QFrame.Box)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_50.setFrameShape(QtWidgets.QFrame.Box)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.label_50.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gridLayout.addWidget(self.label_50, 5, 0, 1, 1)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(1100, 730, 228, 21))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ref_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ref_3.setObjectName("ref_3")
        self.gridLayout_2.addWidget(self.ref_3, 0, 0, 1, 1)
        self.ref_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ref_4.setObjectName("ref_4")
        self.gridLayout_2.addWidget(self.ref_4, 0, 2, 1, 1)
        self.ref_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ref_1.setStyleSheet("background-color: #728FCE")
        self.ref_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.ref_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ref_1.setObjectName("ref_1")
        self.gridLayout_2.addWidget(self.ref_1, 0, 1, 1, 1)
        self.ref_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ref_2.setStyleSheet("background-color: #64E986")
        self.ref_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.ref_2.setObjectName("ref_2")
        self.ref_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gridLayout_2.addWidget(self.ref_2, 0, 3, 1, 1)

        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(860, 123, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setMouseTracking(True)
        self.checkBox.setChecked(True)
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(710, 123, 141, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setMouseTracking(True)
        self.checkBox_2.setChecked(True)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(255, 121, 161, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #C5C2BA")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 121, 161, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: #C5C2BA")
 
        self.week = QtWidgets.QLabel(Form)
        self.week.setGeometry(QtCore.QRect(450, 121, 240, 25))
        self.week.setObjectName("week")
        self.week.setFrameShadow(QtWidgets.QFrame.Raised)
        self.week.setFrameShape(QtWidgets.QFrame.Box)
        self.week.setAlignment(QtCore.Qt.AlignCenter)

        self.toLog = QtWidgets.QPushButton(Form)
        self.toLog.setGeometry(QtCore.QRect(1100, 123, 100, 25))
        self.toLog.setObjectName("toLog")

        self.toLog = QtWidgets.QPushButton(Form)
        self.toLog.setGeometry(QtCore.QRect(1100, 123, 100, 25))
        self.toLog.setObjectName("toLog")
        self.toLog.setStyleSheet("background-color: #C5C2BA")

        self.tottb = QtWidgets.QPushButton(Form)
        self.tottb.setGeometry(QtCore.QRect(1100, 123, 100, 25))
        self.tottb.setObjectName("tottb")
        self.tottb.setStyleSheet("background-color: #C5C2BA")
        
        self.logOut = QtWidgets.QPushButton(Form)
        self.logOut.setGeometry(QtCore.QRect(1250, 20, 100, 25))
        self.logOut.setObjectName("logOut")
        self.logOut.setStyleSheet("background-color: #F3A393")

        self.welcomemsg = QtWidgets.QLabel(Form)
        self.welcomemsg.setGeometry(QtCore.QRect(90, 20, 1110, 95))
        self.welcomemsg.setObjectName("welcomemsg")
        self.welcomemsg.setStyleSheet("background-color: #b3d2ff")
        self.welcomemsg.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.welcomemsg.setFrameShape(QtWidgets.QFrame.Box)
        self.welcomemsg.setMargin(5)

        self.log_title = QtWidgets.QLabel(self)
        self.log_title.setGeometry(QtCore.QRect(90, 129, 225, 21))
        self.log_title.setStyleSheet("background : #B2B2B1;")
        self.log_title.setObjectName("log_title")
        self.log_title.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">log_id</span></p></body></html>")
        self.log_title_2 = QtWidgets.QLabel(self)
        self.log_title_2.setGeometry(QtCore.QRect(315, 129, 225, 21))
        self.log_title_2.setStyleSheet("background : #B2B2B1;")
        self.log_title_2.setObjectName("log_title_2")
        self.log_title_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">login_time</span></p></body></html>")
        self.log_title_3 = QtWidgets.QLabel(self)
        self.log_title_3.setGeometry(QtCore.QRect(540, 129, 225, 21))
        self.log_title_3.setStyleSheet("background : #B2B2B1;")
        self.log_title_3.setObjectName("log_title_3")
        self.log_title_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">logout_time</span></p></body></html>")
        self.log_title_4 = QtWidgets.QLabel(self)
        self.log_title_4.setGeometry(QtCore.QRect(765, 129, 225, 21))
        self.log_title_4.setStyleSheet("background : #B2B2B1;")
        self.log_title_4.setObjectName("log_title_4")
        self.log_title_4.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">duration</span></p></body></html>")

        self.list_widget = QListWidget(self)
        self.list_widget.setGeometry(90, 150, 900, 450)
        self.scroll_bar = QScrollBar(self)
        self.scroll_bar.setStyleSheet("background : #EAE9E5;")
        self.list_widget.setVerticalScrollBar(self.scroll_bar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
    
        self.label_90.setText(_translate("Form", " 16:30-17:30 "))
        self.label_04.setText(_translate("Form", "  Wednesday  "))
        self.label_100.setText(_translate("Form", " 17:30-18:30 "))
        self.label_00.setText(_translate("Form", "<html><head/><body><p align=\"center\">Time \\ Day</p></body></html>"))
        self.label_05.setText(_translate("Form", "  Thursday  "))
        self.label_01.setText(_translate("Form", "  Sunday  "))
        self.label_30.setText(_translate("Form", " 10:30-11:30 "))
        self.label_80.setText(_translate("Form", " 15:30-16:30 "))
        self.label_02.setText(_translate("Form", "  Monday  "))
        self.label_07.setText(_translate("Form", "  Saturday  "))
        self.label_03.setText(_translate("Form", "  Tuesday  "))
        self.label_40.setText(_translate("Form", " 11:30-12:30 "))
        self.label_60.setText(_translate("Form", " 13:30-14:30 "))
        self.label_06.setText(_translate("Form", "  Friday  "))
        self.label_70.setText(_translate("Form", " 14:30-15:30 "))
        self.label_20.setText(_translate("Form", " 09:30-10:30 "))
        self.label_10.setText(_translate("Form", " 08:30-09:30 "))
        self.label_50.setText(_translate("Form", " 12:30-13:30 "))

        self.ref_3.setText(_translate("Form", "Lecture:"))
        self.ref_4.setText(_translate("Form", "Tutorial: "))
        self.ref_1.setText(_translate("Form", "              "))
        self.ref_2.setText(_translate("Form", "              "))

        self.checkBox.setText(_translate("Form", "Show tutorials"))
        self.checkBox_2.setText(_translate("Form", "Show lectures"))

        self.pushButton.setText(_translate("Form", "Show Next Week"))
        self.pushButton_2.setText(_translate("Form", "Show Previous Week"))

        self.toLog.setText(_translate("Form", "View Log"))
        self.tottb.setText(_translate("Form", "View Timetable"))
        self.logOut.setText(_translate("Form", "Log Out"))
