import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime

#get student id -> current_student_id
current_student_id = "123123"
logintime = datetime.now()
last_log = 1

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

cursor.execute("SELECT course_id AS courseids FROM Study WHERE student_id = ?;", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------Update current login time-------------

cursor.execute("UPDATE Student SET current_login_time = ? WHERE Student_id = ?;",(logintime, current_student_id))
db_connection.commit()

#-------------------------------------------------

#-----------for welcome message-------------------

cursor.execute("SELECT name, current_login_time FROM Student WHERE Student_id = ?;", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get LogInfo-------------------

cursor.execute("SELECT * FROM Log WHERE Log.student_id = ? ORDER BY login_time DESC;", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get course announcements-------------------

cursor.execute("""SELECT NA.course_id, NA.news_announcement FROM news_announcement NA, (SELECT course_id FROM Study WHERE student_id = ?) AS courseids WHERE NA.course_id = courseids.course_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#---------get Lectures--------------
cursor.execute("""SELECT * FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Lecture L WHERE courseids.course_id = L.course_id;""", (current_student_id))
results = cursor.fetchall()
#-----------------------------------

#-----------get Tutorials-------------------
cursor.execute("""SELECT * FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Tutorial T WHERE courseids.course_id = T.course_id;""", (current_student_id))
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
