from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from latestPopUpsetup import Ui_PopUp
import sys
from datetime import datetime, date, timedelta, time
from queryfunc import checkclass, getStudentInfo
from sendemail import send_template

def set_student_info(student):
    global student_name, current_student_id, useremail
    student_name = student
    student_name = "JEFF" ### TEMPORARY, TO BE REMOVED!
    info = getStudentInfo(student_name)[0]
    current_student_id = info[0]
    useremail = info[1]

def test_set_class_info(): #hardcoded for testing
    global course_id, class_id, room, date, zoom_link, start_time, end_time, note_link, class_teacher, class_type
    global news_list
    course_id = "COMP3278_1A"
    class_id = "2"
    room = "MWT2"
    date = "YYYY-M-D"
    start_time = "14:30"
    end_time = "16:30"
    zoom_link = "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"
    note_link = "https://moodle.hku.hk/mod/resource/view.php?id=2668112"
    news_list = ["msg1111111111111111111111111111111111111111111111111111111111111111111111", "msg2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222", "msg33333333333333333333333333333333333333333333333333333"]
    class_teacher = {"cs1", "Ping Luo", "pluo@cs.hku.hk", "CB326"}
    class_type = "Tutorial"


#def set_class_info(CLASS): #Capital letter to avoid mixing with class
#    global class_info, address, zoom_link, note_link
#    global teacher_msg_list
#    teacher_msg_list = []



def get_remind_msg():
    global remind_msg
    if class_type == "Tutorial":
        remind_msg = str(student_name) + ", you have a " + "tutorial" + " within an hour!"
    elif class_type == "Lecture":
        remind_msg = str(student_name) + ", you have a " + "lecture" + " within an hour!"

def get_start_to_end_time():
    global start_to_end_time
    start_to_end_time = start_time + " - " + end_time


def get_news():
    global news_list
    global news
    news = ''
    for i in range(len(news_list)):
        news = news + news_list[i] + "\n"

#def get_class_teacher():
#    global class_teacher







class PopUp (QWidget, Ui_PopUp):
    def __init__(self, student): #3rd argument be CLASS
        set_student_info(student)
        test_set_class_info() ##hardcoded for testing
        super(PopUp, self).__init__()
        self.setupUi(self)
        self.set_course_id()
        self.set_class_id()
        self.set_date()
        self.set_start_to_end_time()
        self.set_zoom_link()
        self.set_remind_msg()
        self.set_news()
        self.set_room()


        self.exit_button.clicked.connect(self.close)
        self.email_and_exit_button.clicked.connect(lambda: self.email_and_exit_button_clicked())


    def email_and_exit_button_clicked(self,evnt):
        super(PopUp, self).closeEvent(evnt)
        #send email here
        evnt.accept()

    def set_remind_msg(self):
        get_remind_msg()
        self.remind_msg.setText(remind_msg)
        self.remind_msg.setFont(QFont('Georgia', 12))

    def set_course_id(self):
        self.course_id.setText(course_id)

    def set_class_id(self):
        self.class_id.setText(class_id)

    def set_date(self):
        self.date.setText(date)

    def set_start_to_end_time(self):
        get_start_to_end_time()
        self.start_time.setText(start_to_end_time) #start time is now start to end time

    def set_zoom_link(self):
        self.zoom_link.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href= "+zoom_link+"><span style=\" text-decoration: underline; color:#0000ff;\">Click here to enter zoom</span></a></p></body></html>")

    def set_news(self):
        get_news()
        self.news.setText(news)
        #self.Within_1hour_label.setFont(QFont('Georgia', 12))

    def set_room(self):
        self.room.setText(room)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = PopUp("JEFF")#2nd argument as CLASS

    myWin.show()

    sys.exit(app.exec_())