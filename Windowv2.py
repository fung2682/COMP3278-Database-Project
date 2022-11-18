from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from Winsetup import Ui_Window
import sys
from datetime import datetime, date, timedelta, time
from queryfunc import getClasses, checkclass, addLog, updateLog, getLog

student_name = ''
current_student_id = -1
useremail = ''
query = []
welcome_msg = []

def set_student_info(student):
    global student_name, current_student_id, useremail
    student_name = student
    student_name = "JEFF" ### TEMPORARY, TO BE REMOVED!
    info = getStudentInfo(student_name)
    current_student_id = info[0]
    useremail = info[1]

def get_wel_msg():
    global welcome_msg
    now = datetime.now()
    welcome_msg = " Hello, " + str(student_name) + ". " + "The time now is " + str(now.strftime("%d/%m/%Y %H:%M \n")) + " You last logged in at xx/xx/xxxx xx:xx" + "\n                                                                                      I am always ready to learn, although I do not always like being taught.  - Winston Churchill"

def get_ttb_info(aDate):
    global query
    query = getClasses(aDate, current_student_id)
    # sample
#     if (aDate == date.today() + timedelta(7)):
#         # print("next week")
#         query = [('COMP1323 - 1A', datetime.strptime('08::30::00', '%H::%M::%S').time(), datetime.strptime('09::30::00', '%H::%M::%S').time(), 'MWT2', 5, 1)]
#     elif (aDate == date.today() - timedelta(7)):
#         # print("last week")
#         query = [('COMP1333 - 1A', datetime.strptime('16::30::00', '%H::%M::%S').time(), datetime.strptime('17::30::00', '%H::%M::%S').time(), 'MWT2', 3, 1),
#         ('COMP1323 - 1A', datetime.strptime('13::30::00', '%H::%M::%S').time(), datetime.strptime('14::30::00', '%H::%M::%S').time(), 'MWT2', 2, 0)]
#     elif (aDate == date.today()):
#         query = [('COMP1344 - 1A', datetime.strptime('08::30::00', '%H::%M::%S').time(), datetime.strptime('10::30::00', '%H::%M::%S').time(), 'MWT2', 2, 1),
#         ('COMP1323 - 1A', datetime.strptime('10::30::00', '%H::%M::%S').time(), datetime.strptime('12::30::00', '%H::%M::%S').time(), 'MWT2', 2, 0)]
#     else:
#         query = []

def get_log():
    #### query #####
    logs = getLog(current_student_id)
#     logs = []
#     log = [00000000, datetime.strptime('22-10-20 00:00:00', '%y-%m-%d %H:%M:%S'), datetime.strptime('22-10-20 00:05:03', '%y-%m-%d %H:%M:%S'), datetime.strptime('00:05:03', '%H:%M:%S')]
#     for i in range(0,40):
#         log[0] += 1
#         logs.append(tuple(log))
    _logs = []
    for i in range(1,40):
        _logs.append([(8-len(str(logs[i][0])))*'0'+str(logs[i][0]), logs[i][1], logs[i][2], logs[i][3]])
    return _logs

class Window (QWidget, Ui_Window):

    date_to_show = date.today()
    def __init__(self, student, parent=None):
        set_student_info(student)
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.tottb.hide()
        self.set_welcome_msg()
        get_ttb_info(self.date_to_show)
        self.build_ttb()
        self.build_log()

        self.log_title.hide()
        self.log_title_2.hide()
        self.log_title_3.hide()
        self.log_title_4.hide()
        self.list_widget.hide()
        self.scroll_bar.hide()

        self.checkBox.stateChanged.connect(lambda:self.toddle_tutorials())
        self.checkBox_2.stateChanged.connect(lambda:self.toddle_lectures())
        self.pushButton.clicked.connect(lambda: self.show_next_week())
        self.pushButton_2.clicked.connect(lambda:self.show_previous_week())
        self.toLog.clicked.connect(lambda: self.jump_to_log())
        self.tottb.clicked.connect(lambda: self.jump_to_ttb())
        self.aboutToQuit.connect(lambda: addLog(current_student_id))
    
    def set_welcome_msg(self):
        get_wel_msg()
        self.welcomemsg.setText(QtCore.QCoreApplication.translate("Form", welcome_msg))
        self.welcomemsg.setFont(QFont('Georgia', 18))

    def jump_to_log(self):
        self.gridLayoutWidget.hide()
        self.gridLayoutWidget_2.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.checkBox_2.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.checkBox_2.hide()
        self.toLog.hide()

        self.tottb.show()
        self.log_title.show()
        self.log_title_2.show()
        self.log_title_3.show()
        self.log_title_4.show()
        self.list_widget.show()
        self.scroll_bar.show()
    
    def jump_to_ttb(self):
        self.gridLayoutWidget.show()
        self.gridLayoutWidget_2.show()
        self.checkBox.show()
        self.checkBox_2.show()
        self.checkBox_2.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.checkBox_2.show()
        self.toLog.show()

        self.tottb.hide()
        self.log_title.hide()
        self.log_title_2.hide()
        self.log_title_3.hide()
        self.log_title_4.hide()
        self.list_widget.hide()
        self.scroll_bar.hide()

    def build_log(self):
        logs = get_log()
        for log in logs:
            log_id = log[0]
            login_time = log[1].strftime("%y-%m-%d %H:%M:%S")
            logout_time = log[2].strftime("%y-%m-%d %H:%M:%S")
            duration = log[3].strftime("%H:%M:%S")
            # duration = '{:02}:{:02}:{:02}'.format((log[2]-log[1]).seconds//3600, ((log[2]-log[1]).seconds//60%60, ((log[2]-log[1]).seconds)%60)
            # log_entry = ('', log[0], '      |      ', login_time,'   |   ', logout_time,'      |       ', duration)
            newlog = QListWidgetItem('{:9s} {:8s} {:3s} {:19s} {:3s} {:19s} {:3s} {:8s}'.format('', log_id, '      |      ', login_time,'   |   ', logout_time,'      |       ', duration))
            newlog.setFont(QFont('Menlo', 13))
            self.list_widget.addItem(newlog)

    def build_ttb(self):
        for item in query:

            newClass = QtWidgets.QLabel(self.gridLayoutWidget)
            newClass.setAlignment(QtCore.Qt.AlignCenter)
            newClass.setFrameShape(QtWidgets.QFrame.Box)
            newClass.setMargin(5)
            newClass.setFrameShadow(QtWidgets.QFrame.Raised)

            # label_name = item[0]+"/"+item[1]+"/"+item[5]
            # newClass.setObjectName(label_name)
            # newClass.setAccessibleName(label_name)

            coursecode = item[0]
            class_time = str(item[1].hour)+":"+str(item[1].minute)+ " - " + str(item[2].hour)+":"+str(item[2].minute)
            room = item[3]
            class_info = coursecode + "\n" + class_time + "\n" + room
            newClass.setText(QtCore.QCoreApplication.translate("Form", class_info))

            if (item[5] == 1):
                color = "#728FCE"
            else:
                color = "#64E986"
            newClass.setStyleSheet("background-color: "+color)

            hr = int(item[2].hour-item[1].hour)
            row_num = int(item[1].hour) - 8 + 1
            col_num = 0
            if (item[4] == 6):
                col_num = 1
            else:
                col_num = item[4] + 2
            self.gridLayout.addWidget(newClass, row_num, col_num, hr, 1)

    def clear_current(self):
        for row in range(1, 11):
            for col in range(1, 8):
                pos_to_remove = self.gridLayout.itemAtPosition(row, col)
                if (pos_to_remove != None):
                    pos_to_remove.widget().deleteLater()

    def show_next_week(self):
        self.clear_current()
        self.date_to_show += timedelta(7)
        get_ttb_info(self.date_to_show)
        self.build_ttb()
        if (self.checkBox.isChecked() == False):
            self.toddle_tutorials()
        if (self.checkBox_2.isChecked() == False):
            self.toddle_lectures()

      
    def show_previous_week(self):
        self.clear_current()
        self.date_to_show -= timedelta(7)
        get_ttb_info(self.date_to_show)
        self.build_ttb()
        if (self.checkBox.isChecked() == False):
            self.toddle_tutorials()
        if (self.checkBox_2.isChecked() == False):
            self.toddle_lectures()

    def toddle_tutorials(self):
        checked = self.checkBox.isChecked()
        for item in query:
            if (item[5] == 0):
                row_num = int(item[1].hour) - 8 + 1
                col_num = 0
                if (item[4] == 6):
                    col_num = 1
                else:
                    col_num = item[4] + 2
                tutorial = self.gridLayout.itemAtPosition(row_num, col_num).widget()
                if (checked):
                    tutorial.show()
                else:
                    tutorial.hide()

    def toddle_lectures(self):
        checked = self.checkBox_2.isChecked()
        for item in query:
            if (item[5] == 1):
                row_num = int(item[1].hour) - 8 + 1
                col_num = 0
                if (item[4] == 6):
                    col_num = 1
                else:
                    col_num = item[4] + 2
                lecture = self.gridLayout.itemAtPosition(row_num, col_num).widget()
                if (checked):
                    lecture.show()
                else:
                    lecture.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = Window(student_name)

    myWin.show()

    sys.exit(app.exec_())