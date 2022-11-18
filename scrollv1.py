from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(0, 0, 1400, 800)
        self.UiComponents()
        self.show()
  

    def UiComponents(self):

        self.log_title = QtWidgets.QLabel(self)
        self.log_title.setGeometry(QtCore.QRect(90, 129, 76, 21))
        self.log_title.setStyleSheet("background : #B2B2B1;")
        self.log_title.setObjectName("log_title")
        self.log_title.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">log_id</span></p></body></html>")
        self.log_title_2 = QtWidgets.QLabel(self)
        self.log_title_2.setGeometry(QtCore.QRect(166, 129, 144, 21))
        self.log_title_2.setStyleSheet("background : #B2B2B1;")
        self.log_title_2.setObjectName("log_title_2")
        self.log_title_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">login_time</span></p></body></html>")
        self.log_title_3 = QtWidgets.QLabel(self)
        self.log_title_3.setGeometry(QtCore.QRect(310, 129, 138, 21))
        self.log_title_3.setStyleSheet("background : #B2B2B1;")
        self.log_title_3.setObjectName("log_title_3")
        self.log_title_3.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">logout_time</span></p></body></html>")
        self.log_title_4 = QtWidgets.QLabel(self)
        self.log_title_4.setGeometry(QtCore.QRect(448, 129, 80, 21))
        self.log_title_4.setStyleSheet("background : #B2B2B1;")
        self.log_title_4.setObjectName("log_title_4")
        self.log_title_4.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">duration</span></p></body></html>")

  
        list_widget = QListWidget(self)
        list_widget.setGeometry(90, 150, 440, 600)
  
        item1 = QListWidgetItem("00000000 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item2 = QListWidgetItem("00000001 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item3 = QListWidgetItem("00000002 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item4 = QListWidgetItem("00000003 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item5 = QListWidgetItem("00000004 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item6 = QListWidgetItem("00000005 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item7 = QListWidgetItem("00000006 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item8 = QListWidgetItem("00000007 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item9 = QListWidgetItem("00000008 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item10 = QListWidgetItem("00000009 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item11 = QListWidgetItem("00000010 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item12 = QListWidgetItem("00000011 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item13 = QListWidgetItem("00000012 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item14 = QListWidgetItem("00000013 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item15 = QListWidgetItem("00000014 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item16 = QListWidgetItem("00000015 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item17 = QListWidgetItem("00000016 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item18 = QListWidgetItem("00000017 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item19 = QListWidgetItem("00000018 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")

        item20 = QListWidgetItem("00000019 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item21 = QListWidgetItem("00000020 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item22 = QListWidgetItem("00000021 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item23 = QListWidgetItem("00000022 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item24 = QListWidgetItem("00000023 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item25 = QListWidgetItem("00000024 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item26 = QListWidgetItem("00000025 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item27 = QListWidgetItem("00000026 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item28 = QListWidgetItem("00000027 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item29 = QListWidgetItem("00000028 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item30 = QListWidgetItem("00000029 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item31 = QListWidgetItem("00000030 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item32 = QListWidgetItem("00000031 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item33 = QListWidgetItem("00000032 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item34 = QListWidgetItem("00000033 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item35 = QListWidgetItem("00000034 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item36 = QListWidgetItem("00000035 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item37 = QListWidgetItem("00000036 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")
        item38 = QListWidgetItem("00000037 | 2022-10-20 00:00:00 | 2022-10-20 00:05:21 | 00:05:21")


        list_widget.addItem(item1)
        list_widget.addItem(item2)
        list_widget.addItem(item3)
        list_widget.addItem(item4)
        list_widget.addItem(item5)
        list_widget.addItem(item6)
        list_widget.addItem(item7)
        list_widget.addItem(item8)
        list_widget.addItem(item9)
        list_widget.addItem(item10)
        list_widget.addItem(item11)
        list_widget.addItem(item12)
        list_widget.addItem(item13)
        list_widget.addItem(item14)
        list_widget.addItem(item15)
        list_widget.addItem(item16)
        list_widget.addItem(item17)
        list_widget.addItem(item18)
        list_widget.addItem(item19)
        
        list_widget.addItem(item20)
        list_widget.addItem(item21)
        list_widget.addItem(item22)
        list_widget.addItem(item23)
        list_widget.addItem(item24)
        list_widget.addItem(item25)
        list_widget.addItem(item26)
        list_widget.addItem(item27)
        list_widget.addItem(item28)
        list_widget.addItem(item29)
        list_widget.addItem(item30)
        list_widget.addItem(item31)
        list_widget.addItem(item32)
        list_widget.addItem(item33)
        list_widget.addItem(item34)
        list_widget.addItem(item35)
        list_widget.addItem(item36)
        list_widget.addItem(item37)
        list_widget.addItem(item38)
  
        
  
        scroll_bar = QScrollBar(self)
        scroll_bar.setStyleSheet("background : #EAE9E5;")
        list_widget.setVerticalScrollBar(scroll_bar)
        value = list_widget.verticalScrollBar()
  
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 300)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



app = QApplication(sys.argv)
myWin = Window()
myWin.show()
sys.exit(app.exec_())