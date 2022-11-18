# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUpUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(707, 490)
        self.Email_Exit_button = QtWidgets.QPushButton(dialog)
        self.Email_Exit_button.setGeometry(QtCore.QRect(190, 420, 141, 28))
        self.Email_Exit_button.setObjectName("Email_Exit_button")

        self.Exit_button = QtWidgets.QPushButton(dialog)
        self.Exit_button.setGeometry(QtCore.QRect(390, 420, 93, 28))
        self.Exit_button.setObjectName("Exit_button")

        self.Course_info_label = QtWidgets.QLabel(dialog)
        self.Course_info_label.setGeometry(QtCore.QRect(70, 80, 121, 16))
        self.Course_info_label.setObjectName("Course_info_label")

        self.Classroom_address_label = QtWidgets.QLabel(dialog)
        self.Classroom_address_label.setGeometry(QtCore.QRect(70, 150, 121, 16))
        self.Classroom_address_label.setObjectName("Classroom_address_label")

        self.Teachers_message_label = QtWidgets.QLabel(dialog)
        self.Teachers_message_label.setGeometry(QtCore.QRect(70, 200, 121, 16))
        self.Teachers_message_label.setObjectName("Teachers_message_label")

        self.Zoom_link_label = QtWidgets.QLabel(dialog)
        self.Zoom_link_label.setGeometry(QtCore.QRect(70, 270, 121, 16))
        self.Zoom_link_label.setObjectName("Zoom_link_label")

        self.Note_link_label = QtWidgets.QLabel(dialog)
        self.Note_link_label.setGeometry(QtCore.QRect(70, 350, 55, 16))
        self.Note_link_label.setObjectName("Note_link_label")

        self.Within_1hour_label = QtWidgets.QLabel(dialog)
        self.Within_1hour_label.setGeometry(QtCore.QRect(210, 40, 291, 16))
        self.Within_1hour_label.setObjectName("Within_1hour_label")

        self.Course_info = QtWidgets.QLabel(dialog)
        self.Course_info.setGeometry(QtCore.QRect(200, 80, 100, 16))
        self.Course_info.setObjectName("Course_info")

        self.Zoom_link_browser = QtWidgets.QTextBrowser(dialog)
        self.Zoom_link_browser.setGeometry(QtCore.QRect(200, 270, 391, 51))
        self.Zoom_link_browser.setPlaceholderText("")
        self.Zoom_link_browser.setOpenExternalLinks(True)
        self.Zoom_link_browser.setObjectName("Zoom_link_browser")

        self.Note_link_browser = QtWidgets.QTextBrowser(dialog)
        self.Note_link_browser.setGeometry(QtCore.QRect(200, 341, 391, 51))
        self.Note_link_browser.setOpenExternalLinks(True)
        self.Note_link_browser.setObjectName("Note_link_browser")

        self.Teachers_message = QtWidgets.QLabel(dialog)
        self.Teachers_message.setGeometry(QtCore.QRect(200, 200, 391, 16))
        self.Teachers_message.setObjectName("Teachers_message")

        self.Classroom_address = QtWidgets.QLabel(dialog)
        self.Classroom_address.setGeometry(QtCore.QRect(200, 150, 391, 16))
        self.Classroom_address.setObjectName("Classroom_address")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def email_exit_button_clicked(self):
        print("1clicked")

    def exit_button_clicked(self):
        print("2clicked")
        self.close()

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Reminder"))

        self.Email_Exit_button.setText(_translate("dialog", "Send email and Exit"))
        self.Email_Exit_button.clicked.connect(self.email_exit_button_clicked)

        self.Exit_button.setText(_translate("dialog", "Exit"))
        self.Exit_button.clicked.connect(self.exit_button_clicked)

        self.Course_info_label.setText(_translate("dialog", "Course info:"))
        self.Classroom_address_label.setText(_translate("dialog", "Classroom address:"))
        self.Teachers_message_label.setText(_translate("dialog", "Teacher\'s message:"))
        self.Zoom_link_label.setText(_translate("dialog", "Zoom link:"))
        self.Note_link_label.setText(_translate("dialog", "Notes:"))
        self.Within_1hour_label.setText(_translate("dialog", "Student_name, you have a class within an hour!"))
        self.Course_info.setText(_translate("dialog", "INFO"))
        self.Teachers_message.setText(_translate("dialog", "MSG"))
        self.Classroom_address.setText(_translate("dialog", "ADDRESS"))

        self.Zoom_link_browser.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://google.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Google</span></a></p></body></html>"))
        self.Note_link_browser.setHtml(_translate("dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Github</span></a></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())

