from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from ttb import Ui_Form
import sys

query = []

class MainWindow (QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.checkBox.clicked.connect(lambda:self.toddle_tutorials(query))
        self.checkBox_2.clicked.connect(lambda:self.toddle_lectures(query))
    
    def build_ttb(self, query):
        for item in query:

            newClass = QtWidgets.QLabel(self.gridLayoutWidget)
            newClass.setAlignment(QtCore.Qt.AlignCenter)
            newClass.setFrameShape(QtWidgets.QFrame.Box)
            newClass.setMargin(5)
            newClass.setFrameShadow(QtWidgets.QFrame.Raised)
            newClass.setEnabled(True)

            label_name = item[0]+"/"+item[1]+"/"+item[5]
            newClass.setObjectName(label_name)
            newClass.setAccessibleName(label_name)

            coursecode = item[0]
            class_time = item[1]+ " - " + item[2]
            room = item[3]
            class_info = coursecode + "\n" + class_time + "\n" + room
            newClass.setText(QtCore.QCoreApplication.translate("Form", class_info))

            if (item[4] == 1):
                color = "#728FCE"
            else:
                color = "#64E986"
            newClass.setStyleSheet("background-color: "+color)

            hour = int(item[2][0:2]) - int(item[1][0:2])
            row_num = int(item[1][0:2]) - 8 + 1
            col_num = 0
            if (item[5] == "Sunday"):
                col_num = 1
            elif (item[5] == "Monday"):
                col_num = 2
            elif (item[5] == "Tuesday"):
                col_num = 3
            elif (item[5] == "Wednesday"):
                col_num = 4
            elif (item[5] == "Thursday"):
                col_num = 5
            elif (item[5] == "Friday"):
                col_num = 6
            elif (item[5] == "Saturday"):
                col_num = 7
            self.gridLayout.addWidget(newClass, row_num, col_num, hour, 1)
    
    def toddle_tutorials(self, query):
        checked = self.checkBox.isChecked()
        self.gridLayout.itemAtPosition(1, 2).widget().setStyleSheet("opacity: 0; background-color: #64E986")
        for item in query:
            if (item[4] == 0):
                row_num = int(item[1][0:2]) - 8 + 1
                col_num = 0
                if (item[5] == "Sunday"):
                    col_num = 1
                elif (item[5] == "Monday"):
                    col_num = 2
                elif (item[5] == "Tuesday"):
                    col_num = 3
                elif (item[5] == "Wednesday"):
                    col_num = 4
                elif (item[5] == "Thursday"):
                    col_num = 5
                elif (item[5] == "Friday"):
                    col_num = 6
                elif (item[5] == "Saturday"):
                    col_num = 7
                tutorial = self.gridLayout.itemAtPosition(row_num, col_num).widget()
                if (checked):
                    tutorial.show()
                else:
                    tutorial.hide()

    def toddle_lectures(self, query):
        checked = self.checkBox_2.isChecked()
        for item in query:
            if (item[4] == 1):
                row_num = int(item[1][0:2]) - 8 + 1
                col_num = 0
                if (item[5] == "Sunday"):
                    col_num = 1
                elif (item[5] == "Monday"):
                    col_num = 2
                elif (item[5] == "Tuesday"):
                    col_num = 3
                elif (item[5] == "Wednesday"):
                    col_num = 4
                elif (item[5] == "Thursday"):
                    col_num = 5
                elif (item[5] == "Friday"):
                    col_num = 6
                elif (item[5] == "Saturday"):
                    col_num = 7
                lecture = self.gridLayout.itemAtPosition(row_num, col_num).widget()
                if (checked):
                    lecture.show()
                else:
                    lecture.hide()

# sample with only a few classes
# query = [('COMP1323 - 1A', '08:30', '09:30', 'MWT2', 0, 'Monday'), 
# ('COMP8394 - 1A', '14:30', '17:30', 'MWT4', 0, 'Monday'),
# ('COMP9409 - 1A', '12:30', '13:30', 'MWT3', 1, 'Tuesday'),
# ('COMP2102 - 1A', '11:30', '14:30', 'MWT5', 1, 'Thursday')]

# sample with many classes
query = [('COMP1323 - 1A', '08:30', '09:30', 'MWT2', 0, 'Monday'), 
('COMP9409 - 1A', '12:30', '14:30', 'MWT3', 1, 'Wednesday'), 
('COMP8394 - 1A', '14:30', '15:30', 'MWT4', 0, 'Thursday'), 
('COMP2102 - 1A', '11:30', '14:30', 'MWT5', 1, 'Thursday'), 
('COMP1323 - 1A', '08:30', '09:30', 'MWT2', 0, 'Friday'), 
('COMP9409 - 1A', '13:30', '14:30', 'MWT3', 1, 'Monday'), 
('COMP8394 - 1A', '14:30', '15:30', 'MWT4', 0, 'Wednesday'), 
('COMP2102 - 1A', '11:30', '14:30', 'MWT5', 1, 'Wednesday'), 
('COMP1323 - 1A', '08:30', '09:30', 'MWT2', 0, 'Thursday'), 
('COMP9409 - 1A', '12:30', '14:30', 'MWT3', 1, 'Friday'), 
('COMP8394 - 1A', '14:30', '15:30', 'MWT4', 0, 'Monday'),
('COMP8394 - 1A', '09:30', '10:30', 'MWT4', 1, 'Monday'),
('COMP8394 - 1A', '10:30', '11:30', 'MWT4', 0, 'Monday'),
('COMP8394 - 1A', '11:30', '12:30', 'MWT4', 1, 'Monday'),
('COMP8394 - 1A', '12:30', '13:30', 'MWT4', 0, 'Monday'),
('COMP8394 - 1A', '15:30', '16:30', 'MWT4', 0, 'Monday'),
('COMP8394 - 1A', '16:30', '17:30', 'MWT4', 0, 'Monday'),
('COMP8394 - 1A', '17:30', '18:30', 'MWT4', 0, 'Monday'),
('COMP9409 - 1A', '12:30', '16:30', 'MWT3', 0, 'Sunday'),
('COMP9409 - 1A', '12:30', '13:30', 'MWT3', 1, 'Tuesday'),
('COMP9409 - 1A', '13:30', '14:30', 'MWT3', 1, 'Saturday')
]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = MainWindow()
    myWin.build_ttb(query)
    myWin.show()

    sys.exit(app.exec_())