# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latestPopUpUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_PopUp(object):
    def setupUi(self, PopUp):
        PopUp.setObjectName("PopUp")
        PopUp.resize(760, 660)
        PopUp.setStyleSheet("background-color: #F9F6EE; color: #254117")
        self.remind_msg = QtWidgets.QLabel(PopUp)
        self.remind_msg.setGeometry(QtCore.QRect(90, 60, 400, 32))
        self.remind_msg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remind_msg.setObjectName("remind_msg")
        self.course_id_label = QtWidgets.QLabel(PopUp)
        self.course_id_label.setGeometry(QtCore.QRect(90, 100, 71, 16))
        self.course_id_label.setObjectName("course_id_label")
        self.class_id_label = QtWidgets.QLabel(PopUp)
        self.class_id_label.setGeometry(QtCore.QRect(90, 130, 71, 16))
        self.class_id_label.setObjectName("class_id_label")
        self.date_label = QtWidgets.QLabel(PopUp)
        self.date_label.setGeometry(QtCore.QRect(90, 160, 71, 16))
        self.date_label.setObjectName("date_label")
        self.start_time_label = QtWidgets.QLabel(PopUp)
        self.start_time_label.setGeometry(QtCore.QRect(90, 190, 71, 16))
        self.start_time_label.setObjectName("start_time_label")
        #self.end_time_label = QtWidgets.QLabel(PopUp)
        #self.end_time_label.setGeometry(QtCore.QRect(90, 220, 71, 16))
        #self.end_time_label.setObjectName("end_time_label")
        self.room_label = QtWidgets.QLabel(PopUp)
        self.room_label.setGeometry(QtCore.QRect(90, 220, 71, 16))
        self.room_label.setObjectName("room_label")
        self.zoom_link_label = QtWidgets.QLabel(PopUp)
        self.zoom_link_label.setGeometry(QtCore.QRect(90, 250, 71, 16))
        self.zoom_link_label.setTextFormat(QtCore.Qt.AutoText)
        self.zoom_link_label.setObjectName("zoom_link_label")
        self.news_label = QtWidgets.QLabel(PopUp)
        self.news_label.setGeometry(QtCore.QRect(90, 280, 131, 16))
        self.news_label.setOpenExternalLinks(True)
        self.news_label.setObjectName("news_label")
        self.note_link_label = QtWidgets.QLabel(PopUp)
        self.note_link_label.setGeometry(QtCore.QRect(90, 420, 71, 16))
        self.note_link_label.setTextFormat(QtCore.Qt.AutoText)
        self.note_link_label.setObjectName("note_link_label")
        self.class_teacher_label = QtWidgets.QLabel(PopUp)
        self.class_teacher_label.setGeometry(QtCore.QRect(90, 520, 91, 16))
        self.class_teacher_label.setObjectName("class_teacher_label")
        self.email_and_exit_button = QtWidgets.QPushButton(PopUp)
        self.email_and_exit_button.setGeometry(QtCore.QRect(170, 600, 161, 28))
        self.email_and_exit_button.setObjectName("email_and_exit_button")
        self.exit_button = QtWidgets.QPushButton(PopUp)
        self.exit_button.setGeometry(QtCore.QRect(440, 600, 93, 28))
        self.exit_button.setObjectName("exit_button")
        self.course_id = QtWidgets.QLabel(PopUp)
        self.course_id.setGeometry(QtCore.QRect(160, 100, 121, 16))
        self.course_id.setObjectName("course_id")
        self.course_id.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.class_id = QtWidgets.QLabel(PopUp)
        self.class_id.setGeometry(QtCore.QRect(160, 130, 61, 16))
        self.class_id.setObjectName("class_id")
        self.class_id.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.date = QtWidgets.QLabel(PopUp)
        self.date.setGeometry(QtCore.QRect(160, 160, 55, 16))
        self.date.setObjectName("date")
        self.date.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.start_time = QtWidgets.QLabel(PopUp)
        self.start_time.setGeometry(QtCore.QRect(160, 190, 81, 16))
        self.start_time.setObjectName("start_time")
        self.start_time.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        #self.end_time = QtWidgets.QLabel(PopUp)
        #self.end_time.setGeometry(QtCore.QRect(160, 220, 81, 16))
        #self.end_time.setObjectName("end_time")
        self.room = QtWidgets.QLabel(PopUp)
        self.room.setGeometry(QtCore.QRect(160, 220, 81, 16))
        self.room.setObjectName("room")
        self.room.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.zoom_link = QtWidgets.QLabel(PopUp)
        self.zoom_link.setGeometry(QtCore.QRect(160, 250, 561, 16))
        self.zoom_link.setTextFormat(QtCore.Qt.RichText)
        self.zoom_link.setOpenExternalLinks(True)
        self.zoom_link.setObjectName("zoom_link")

#        self.news = QtWidgets.QLabel(PopUp)
#        self.news.setGeometry(QtCore.QRect(90, 330, 631, 71))
#        self.news.setTextFormat(QtCore.Qt.AutoText)
#        self.news.setObjectName("news")
#        self.news.setWordWrap(True)  # test
#        self.news.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.news = QListWidget(self)
        self.news.setGeometry(90, 300, 590, 110)
        self.news.setWordWrap(True)
        self.news.setObjectName("news")

        self.scroll_bar = QScrollBar(self)
        self.scroll_bar.setStyleSheet("background : #EAE9E5;")
        self.news.setVerticalScrollBar(self.scroll_bar)

        self.note_link = QtWidgets.QLabel(PopUp)
        self.note_link.setGeometry(QtCore.QRect(90, 440, 590, 60))
        self.note_link.setTextFormat(QtCore.Qt.RichText)
        self.note_link.setOpenExternalLinks(True)
        self.note_link.setObjectName("note_link")


        self.class_teacher = QtWidgets.QLabel(PopUp)
        self.class_teacher.setGeometry(QtCore.QRect(180, 520, 590, 16))
        self.class_teacher.setTextFormat(QtCore.Qt.AutoText)
        self.class_teacher.setObjectName("class_teacher")
        self.class_teacher.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.retranslateUi(PopUp)
        QtCore.QMetaObject.connectSlotsByName(PopUp)

    def retranslateUi(self, PopUp):
        _translate = QtCore.QCoreApplication.translate
        PopUp.setWindowTitle(_translate("PopUp", "Reminder"))
        self.remind_msg.setText(_translate("PopUp", "REMIND MSG"))
        self.course_id_label.setText(_translate("PopUp", "Course ID:"))
        self.class_id_label.setText(_translate("PopUp", "Class ID:"))
        self.date_label.setText(_translate("PopUp", "Date:"))
        self.start_time_label.setText(_translate("PopUp", "Start time:"))
        #self.end_time_label.setText(_translate("PopUp", "End time:"))
        self.room_label.setText(_translate("PopUp", "Room:"))
        self.zoom_link_label.setText(_translate("PopUp", "Zoom link:"))
        self.news_label.setText(_translate("PopUp", "News announcement:"))
        self.note_link_label.setText(_translate("PopUp", "Note link:"))
        self.class_teacher_label.setText(_translate("PopUp", "Class teacher:"))
        self.email_and_exit_button.setText(_translate("PopUp", "Send email and Exit"))
        self.exit_button.setText(_translate("PopUp", "Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PopUp = QtWidgets.QDialog()
    ui = Ui_PopUp()
    ui.setupUi(PopUp)
    PopUp.show()
    sys.exit(app.exec_())

