import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime

#get student id -> current_student_id
current_student_id = "0001"
logintime = datetime.now()
currentlog = 1

#-------------connect mysql-----------------

db_connection = mysql.connector.connect(
    host = "localhost",
    user = "nameeeeeee",
    password = "pwwwwwww",
    database = "dbbbbbb"
)

cursor = db_connection.cursor()

#-------------------------------------------

#-------get timetable data----------------
#index: 0: course_id, 1: starttime, 2: endtime, 3:room, 4: weekday, 5:islecture

def getClasses(weekNo):
    #get lectures
    cursor.execute("""SELECT L.course_id,L.starttime,L.endtime,L.room, WEEKDAY(L.date) FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Lecture L WHERE courseids.course_id = L.course_id AND WEEK(L.date) = WEEK(NOW())+?;""", (current_student_id,weekNo))
    ret1 = cursor.fetchall()
    # get tutorials
    cursor.execute("""SELECT T.course_id, T.starttime, T.endtime, T.room, WEEKDAY(T.date) FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Tutorial T 
	WHERE courseids.course_id = T.course_id
    AND WEEK(T.date,0) = WEEK(NOW(),0)+?;""", (current_student_id,weekNo))
    ret2 = cursor.fetchall()

    for i in ret1:
        i = (*i,True)
     
    for j in ret2:
        j = (*j,False)
        ret1.append(j)
        
    return ret1

#-----------------------------------------

#--------check for classes in a hour-------
#index:0: course_id, 1: class_id, 2: date, 3: starttime, 4: endtime, 5: room, 6: zoom_link, 7: news_announcement(list), 8. note_link (list), 9: course_teacher (2D list), 10: class_teacher (tuple), 11: class type
def checkclass():
    cursor.execute("""SELECT L.course_id, L.class_id, L.date, L.starttime, L.endtime, L.room, L.zoom_link FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Lecture L WHERE courseids.course_id = L.course_id
	AND L.date = CURRENT_DATE
	AND TIMEDIFF(CURRENT_TIME, L.starttime) >= '00:00'
	AND TIMEDIFF(CURRENT_TIME, L.starttime) <= '59:59';""",(current_student_id))
    ret = cursor.fetchall()
    if not ret:
        cursor.execute("""SELECT T.course_id, T.class_id, T.date, T.starttime, T.endtime, T.room, T.zoom_link FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Tutorial T WHERE courseids.course_id = T.course_id
		AND T.date = CURRENT_DATE
		AND TIMEDIFF(CURRENT_TIME, T.starttime) >= '00:00'
		AND TIMEDIFF(CURRENT_TIME, T.starttime) <= '59:59';""",(current_student_id))
        ret = cursor.fetchall()
        if not ret:
            return None
        courseid = ret[0][0]
        cursor.execute("""news_announcement FROM news_announcement WHERE course_id = ?;""", (courseid))
        ret2 = cursor.fetchall()
        classid = ret[0][1]
        cursor.execute("""SELECT note_link FROM Tutorial_Note WHERE course_id = ? AND class_id = ?;""", (courseid, classid))
        ret3 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM `Lecturer` WHERE course_id = ?) AS L, (SELECT DISTINCT teacher_id FROM `Tutor` WHERE course_id = ?) AS T
WHERE Tch.teacher_id = T.teacher_id OR Tch.teacher_id = L.teacher_id;""", (courseid))
        ret4 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM Lecturer WHERE course_id = ? AND class_id = ?) AS L
WHERE Tch.teacher_id = L.teacher_id;""", (courseid, classid))
        ret5 = cursor.fetchall()
        ret5 = ret5[0]
        ret[0] = (*ret[0],ret2,ret3,ret4,ret5, "Lecture")
    else:
        courseid = ret[0][0]
        cursor.execute("""news_announcement FROM news_announcement WHERE course_id = ?;""", (courseid))
        ret2 = cursor.fetchall()
        classid = ret[0][1]
        cursor.execute("""SELECT note_link FROM Lecture_Note WHERE course_id = ? AND class_id = ?;""", (courseid, classid))
        ret3 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM `Lecturer` WHERE course_id = ?) AS L, (SELECT DISTINCT teacher_id FROM `Tutor` WHERE course_id = ?) AS T
WHERE Tch.teacher_id = T.teacher_id OR Tch.teacher_id = L.teacher_id;""", (courseid))
        ret4 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM Tutor WHERE course_id = ? AND class_id = ?) AS T
WHERE Tch.teacher_id = T.teacher_id;""" , (courseid, classid))
        ret5 = cursor.fetchall()
        ret5 = ret5[0]
        ret[0] = (*ret[0],ret2,ret3,ret4,ret5,"Tutorial")
    return ret
#----------------------------------------

#-------create log (right after login)-------------
def addLog():
	cursor.execute("SELECT log_id FROM Log WHERE Log.student_id = ? ORDER BY login_time DESC LIMIT 1;", current_student_id)
	results = cursor.fetchall()
	currentlog = results[0] +1
	cursor.execute("INSERT INTO Log VALUES (?,?,?,?);",(currentlog,current_student_id, logintime, datetime.now()))
	db_connection.commit()
#----------------------------------------



#-------update log-----------------
#update logout_time when user log out AND EVERY SMALL TIME INTERVAL (use a while loop with sleep()) !!!!!!!!!!!!!!!
def updateLog():
	cursor.execute("UPDATE Log SET logout_time = ? WHERE log_id = ?;",(datetime.now(),currentlog))
	db_connection.commit()

#---------------------------------

#----------get log-------

def getLog():
	cursor.execute("""SELECT log_id, login_time, logout_time, TIMEDIFF(logout_time,login_time) AS Duration FROM Log WHERE student_id = ? AND log_id != ? ORDER BY login_time DESC LIMIT 10;""", (current_student_id, currentlog))
	results = cursor.fetchall()
	return results

#------------------------

def getStudentInfo():
    cursor.execute("""SELECT name, current_login_time, email_address FROM Student WHERE Student_id = ?;""", (current_student_id))
    results = cursor.fetchall()
    return results
