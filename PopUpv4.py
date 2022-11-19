from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from latestPopUpsetup import Ui_PopUp
import sys
import mysql.connector
from datetime import datetime, date, timedelta, time
from queryfunc import checkclass, getStudentInfo
from sendemail import send_template

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="facerecognition"
)

def set_student_info(student):
    global student_name, current_student_id, useremail
    student_name = student
    student_name = "JEFF" ### TEMPORARY, TO BE REMOVED!
    info = getStudentInfo(student_name)[0]
    current_student_id = info[0]
    useremail = info[1]
    global ClassesInformation
    ClassesInformation = checkclass(current_student_id)
    global course_id, class_id, room, date, zoom_link, start_time, end_time, note_link_list, class_teacher_tuple, class_type
    global news_list
    if ClassesInformation != None:
        course_id = ClassesInformation[0]
        class_id = ClassesInformation[1]
        date = ClassesInformation[2]
        start_time = ClassesInformation[3]
        end_time = ClassesInformation[4]
        room = ClassesInformation[5]
        zoom_link = ClassesInformation [6]
        news_list = ClassesInformation[7]
        note_link_list = ClassesInformation[8]
        class_teacher_tuple = ClassesInformation[10]
        class_type = ClassesInformation[11]



def test_set_class_info(): #hardcoded for testing
    global course_id, class_id, room, date, zoom_link, start_time, end_time, note_link_list, class_teacher_tuple, class_type
    global news_list
    course_id = "COMP3278_1A"
    class_id = "2"
    room = "MWT2"
    date = "YYYY-M-D"
    start_time = "14:30"
    end_time = "16:30"
    zoom_link = "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"
    note_link_list = ["https://moodle.hku.hk/mod/resource/view.php?id=2668112", "https://moodle.hku.hk/mod/resource/view.php?id=2639596", "https://moodle.hku.hk/mod/resource/view.php?id=2639597"]
    news_list = ["msg111111  1111111111111 111111111 1111111111111111111 11111111111", "msg222222222", "msg33333333333333333333", "msg44444", "msg5555"]
    class_teacher_tuple = ("cs1", "Ping Luo", "pluo@cs.hku.hk", "CB326")
    class_type = "Tutorial"


def get_remind_msg():
    global remind_msg
    if class_type == "Tutorial":
        remind_msg = str(student_name) + ", you have a " + "tutorial" + " within an hour!"
    elif class_type == "Lecture":
        remind_msg = str(student_name) + ", you have a " + "lecture" + " within an hour!"

def get_start_to_end_time():
    global start_to_end_time
    start_to_end_time = start_time + " - " + end_time

def get_note_link():
    global note_link_list
    global note_link
    note_link = ''
    for i in range(len(note_link_list)):
        note_link = note_link + " " + "<a href= "+note_link_list[i]+">"+ "Note" + str(i) +"</a>"

class PopUp (QWidget, Ui_PopUp):
    def __init__(self, student):
        set_student_info(student)
        test_set_class_info() #hardcoded for testing
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
        self.set_note_link()
        self.set_class_teacher()


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
        self.zoom_link.setText("<a href= '"+zoom_link+"'>Click here to enter zoom</a>")

    def set_news(self):
        #get_news()
        for i in range (len(news_list)):
            self.news.addItem(QListWidgetItem(news_list[i]))

    def set_room(self):
        self.room.setText(room)

    def set_note_link(self):
        get_note_link()
        for i in range(len(note_link_list)):
            self.note_link.setText(note_link)

    def set_class_teacher(self):
        self.class_teacher.setText(class_teacher_tuple[1] + "      Email: " + class_teacher_tuple[2] + "      Office: " + class_teacher_tuple[3])

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = PopUp("JEFF")

    myWin.show()

    sys.exit(app.exec_())
