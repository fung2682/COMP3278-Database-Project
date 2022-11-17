import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime

#get student id -> current_student_id
current_student_id = "0001"
logintime = datetime.now()
last_log = 1


#-------get timetable data----------------

def getClasses(weekNo):
    #get lectures
    cursor.execute("""SELECT L.course_id,L.starttime,L.endtime,L.room, WEEKDAY(L.date) FROM (SELECT course_id FROM Study WHERE student_id = "?") AS courseids, Lecture L 
    WHERE courseids.course_id = L.course_id
    AND WEEK(L.date) = WEEK(NOW())+?;""", (current_student_id,weekNo))
    class1 = cursor.fetchall()
    # get tutorials
    cursor.execute("""SELECT T.course_id, T.starttime, T.endtime, T.room, WEEKDAY(T.date) FROM (SELECT course_id FROM Study WHERE student_id = "?") AS courseids, Tutorial T 
    WHERE courseids.course_id = T.course_id
    AND WEEK(T.date) = WEEK(NOW())+?;""", (current_student_id,weekNo))
    class2 = cursor.fetchall()
    
    for i in class1:
        i = (*i,True)
    for j in class2:
        j = (*j,False)
        class1.append(j)
    return class1

#-----------------------------------------

#--------check for classes in a hour-------

def checkclass():
    cursor.execute("""SELECT L.course_id, L.class_id, L.date, L.starttime, L.endtime, L.room, L.zoom_link FROM (SELECT course_id FROM Study WHERE student_id = "?") AS courseids, Lecture L WHERE courseids.course_id = L.course_id
    AND L.date = CURRENT_DATE
    AND TIMEDIFF(CURRENT_TIME, L.starttime) >= '00:00'
	AND TIMEDIFF(CURRENT_TIME, L.starttime) <= '59:59';""",(current_student_id))
    ret = cursor.fetchall()
    if not ret:
        return NULL
    courseid = ret[0][0]
    cursor.execute("""news_announcement FROM news_announcement WHERE course_id = "?";""", (courseid))
    ret2 = cursor.fetchall()
    classid = ret[0][1]
    cursor.execute("""SELECT note_link FROM Lecture_Note WHERE course_id = "?" AND class_id = "?";""", (courseid, classid))
    ret3 = cursor.fetchall()
    ret[0] = (*ret[0],ret2,ret3)
    return ret


#-------------connect mysql-----------------

db_connection = mysql.connector.connect(
    #host = "localhost",
    #user = "nameeeeeee",
    #password = "pwwwwwww",
    #database = "dbbbbbb"
)

cursor = db_connection.cursor()

#-------------------------------------------

#-----------get courseIDs-------------------

cursor.execute("""SELECT course_id AS courseids FROM Study WHERE student_id = "?";""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------Update current login time-------------

cursor.execute("""UPDATE Student SET current_login_time = ? WHERE Student_id = "?";""",(logintime, current_student_id))
db_connection.commit()

#-------------------------------------------------

#-----------for welcome message-------------------

cursor.execute("""SELECT name, current_login_time FROM Student WHERE Student_id = "?";""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get LogInfo-------------------

cursor.execute("""SELECT * FROM Log WHERE Log.student_id = "?" ORDER BY login_time DESC;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get course announcements-------------------

cursor.execute("""SELECT NA.course_id, NA.news_announcement FROM news_announcement NA, (SELECT course_id FROM Study WHERE student_id = "?") AS courseids WHERE NA.course_id = courseids.course_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#---------get Lectures--------------
cursor.execute("""SELECT * FROM (SELECT course_id FROM Study WHERE student_id = "?") AS courseids, Lecture L WHERE courseids.course_id = L.course_id;""", (current_student_id))
results = cursor.fetchall()
#-----------------------------------

#-----------get Tutorials-------------------
cursor.execute("""SELECT * FROM (SELECT course_id FROM Study WHERE student_id = "?") AS courseids, Tutorial T WHERE courseids.course_id = T.course_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get course announcements-------------------

cursor.execute("""SELECT * FROM news_announcement NA, (SELECT course_id FROM Study WHERE student_id = ?) AS courseids WHERE NA.course_id = courseids.course_id;""", (current_student_id))
results = cursor.fetchall()

#---------------------------------------------------


#-----------get lecture notes-------------------

cursor.execute("""SELECT LN.course_id, LN.class_id, LN.note_link
FROM Lecture_Note LN, (SELECT Le.course_id, Le.class_id FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Lecture Le WHERE courseids.course_id = Le.course_id) AS L
WHERE L.course_id = LN.course_id
AND L.class_id = LN.class_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get tutorial notes-------------------

cursor.execute("""SELECT TN.course_id, TN.class_id, TN.note_link
FROM Tutorial_Note TN,(SELECT Tu.course_id, Tu.class_id FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Tutorial Tu WHERE courseids.course_id = Tu.course_id) AS T
WHERE T.course_id = TN.course_id
AND T.class_id = TN.class_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------Insert log records-------------------

cursor.execute("INSERT INTO Log VALUES (?,?,?,?);",(last_log,current_student_id, logintime, datetime.now()))
db_connection.commit()

#----------------------------------------------
