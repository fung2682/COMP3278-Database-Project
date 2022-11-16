import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime

#get student id -> current_student_id
current_student_id = "123123"
logintime = datetime.now()

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

cursor.execute("""WITH courseids AS (SELECT course_id AS courseids FROM Study WHERE student_id = ?)
SELECT * FROM News_announcement NA, courseids WHERE NA.course_id = courseids.course_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------


#-----------get course announcements-------------------

cursor.execute("""WITH courseids AS (SELECT course_id AS courseids FROM Study WHERE student_id = ?)
SELECT * FROM News_announcement NA, courseids WHERE NA.course_id = courseids.course_id;""", (current_student_id))
results = cursor.fetchall()

#---------------------------------------------------


#-----------get lecture notes-------------------

cursor.execute("""WITH lectures AS (SELECT * FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Lecture L WHERE courseids.course_id = L.course_id)
SELECT LN.course_id, LN.class_id, LN.note_link
FROM lectures L, Lecture_note LN
WHERE L.course_id = LN.course_id
AND L.class_id = LN.class_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------get tutorial notes-------------------

cursor.execute("""WITH tutorials AS (SELECT * FROM (SELECT course_id FROM Study WHERE student_id = ?) AS courseids, Tutorial T WHERE courseids.course_id = T.course_id)
SELECT TN.course_id, TN.class_id, TN.note_link
FROM tutorials T, Tutorial_note TN
WHERE T.course_id = TN.course_id
AND T.class_id = TN.class_id;""", (current_student_id))
results = cursor.fetchall()

#-------------------------------------------

#-----------Insert log records-------------------

cursor.execute("INSERT INTO Log VALUES (?,?,?);",(current_student_id, logintime, datetime.now()))

#----------------------------------------------
