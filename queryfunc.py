import mysql.connector
from datetime import datetime

# get student id -> current_student_id
logintime = datetime.now()
currentlog = 1


# -------------connect mysql-----------------

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="facerecognition"
)

cursor = db_connection.cursor()


# -------------------------------------------

# -------get timetable data----------------
# index: 0: course_id, 1: starttime, 2: endtime, 3:room, 4: weekday, 5:islecture

def getClasses(d, current_student_id):
    # get lectures
    cursor.execute("""SELECT L.course_id,L.starttime,L.endtime,L.room, WEEKDAY(L.date) FROM (SELECT course_id FROM Study WHERE student_id = '%s') AS courseids, Lecture L 
    WHERE courseids.course_id = L.course_id AND YEARWEEK(date) = YEARWEEK('%s');""" % (current_student_id, d))
    ret1 = cursor.fetchall()
    # get tutorials
    cursor.execute("""SELECT T.course_id, T.starttime, T.endtime, T.room, WEEKDAY(T.date) FROM (SELECT course_id FROM Study WHERE student_id = '%s') AS courseids, Tutorial T 
	WHERE courseids.course_id = T.course_id AND YEARWEEK(T.date) = YEARWEEK('%s');""" % (current_student_id, d))
    ret2 = cursor.fetchall()

    ret = []
    for i in ret1:
        j = (i[0], i[1], i[2], i[3], i[4], 1)
        ret.append(j)

    for i in ret2:
        j = (i[0], i[1], i[2], i[3], i[4], 0)
        ret.append(j)

    return ret


# -----------------------------------------

# --------check for classes in a hour-------
# index:0: course_id, 1: class_id, 2: date, 3: starttime, 4: endtime, 5: room, 6: zoom_link, 7: news_announcement(list), 8. note_link (list), 9: course_teacher (2D list), 10: class_teacher (tuple), 11: class type
def checkclass(current_student_id):
    cursor.execute("""SELECT L.course_id, L.class_id, L.date, L.starttime, L.endtime, L.room, L.zoom_link FROM (SELECT course_id FROM Study WHERE student_id = '%s') AS courseids, Lecture L WHERE courseids.course_id = L.course_id
	AND L.date = CURRENT_DATE
	AND TIMEDIFF(L.starttime, CURRENT_TIME) >= '00:00:00'
	AND TIMEDIFF(L.starttime, CURRENT_TIME) <= '00:59:59';""" % current_student_id)
    ret = cursor.fetchall()
    if not ret:
        cursor.execute("""SELECT T.course_id, T.class_id, T.date, T.starttime, T.endtime, T.room, T.zoom_link FROM (SELECT course_id FROM Study WHERE student_id = '%s') AS courseids, Tutorial T WHERE courseids.course_id = T.course_id
		AND T.date = CURRENT_DATE
		AND TIMEDIFF(T.starttime, CURRENT_TIME) >= '00:00:00'
		AND TIMEDIFF(T.starttime, CURRENT_TIME) <= '00:59:59';""" % current_student_id)
        ret = cursor.fetchall()
        if not ret:
            return None
        courseid = ret[0][0]
        cursor.execute(
            """SELECT news_announcement FROM news_announcement WHERE course_id = '%s' ORDER BY update_time DESC LIMIT 5;""" % courseid)
        ret2 = cursor.fetchall()
        classid = ret[0][1]
        cursor.execute(
            """SELECT note_link FROM Tutorial_Note WHERE course_id = '%s'AND class_id = '%s';"""%(courseid, classid))
        ret3 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM `Lecturer` WHERE course_id = '%s' UNION SELECT DISTINCT teacher_id FROM `Tutor` WHERE course_id = '%s') AS TL
        WHERE Tch.teacher_id = TL.teacher_id;""" % (courseid, courseid))
        ret4 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM Tutor WHERE course_id = '%s' AND class_id = '%s') AS T
        WHERE Tch.teacher_id = T.teacher_id;""" % (courseid, classid))
        ret5 = cursor.fetchone()
        ret[0] = (*ret[0], ret2, ret3, ret4, ret5, "Tutorial")
    else:
        courseid = ret[0][0]
        cursor.execute(
            """SELECT news_announcement FROM news_announcement WHERE course_id = '%s' ORDER BY update_time DESC LIMIT 5;""" % courseid)
        ret2 = cursor.fetchall()
        classid = ret[0][1]
        cursor.execute(
            """SELECT note_link FROM Lecture_Note WHERE course_id = '%s'AND class_id = '%s';"""%(courseid, classid))
        ret3 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM `Lecturer` WHERE course_id = '%s' UNION SELECT DISTINCT teacher_id FROM `Tutor` WHERE course_id = '%s') AS TL
        WHERE Tch.teacher_id = TL.teacher_id;""" % (courseid, courseid))
        ret4 = cursor.fetchall()
        cursor.execute("""SELECT Tch.teacher_id,Tch.name, Tch.email,Tch.office FROM Teacher Tch, (SELECT DISTINCT teacher_id FROM Lecturer WHERE course_id = '%s' AND class_id = '%s') AS L
        WHERE Tch.teacher_id = L.teacher_id;""" % (courseid, classid))
        ret5 = cursor.fetchone()
        ret[0] = (*ret[0], ret2, ret3, ret4, ret5, "Lecture")
    return ret


# ----------------------------------------

# -------create log (right after login)-------------
def addLog(current_student_id, logintime):
    cursor.execute(
        "SELECT log_id FROM Log WHERE Log.student_id = '%s' ORDER BY login_time DESC LIMIT 1;" % current_student_id)
    results = cursor.fetchall()
    currentlog = results[0][0] + 1
    cursor.execute(
        "INSERT INTO Log VALUES (%s,'%s','%s','%s');" % (currentlog, current_student_id, logintime, datetime.now()))
    db_connection.commit()


# ----------------------------------------


# -------update log-----------------
# update logout_time when user log out AND EVERY SMALL TIME INTERVAL (use a while loop with sleep()) !!!!!!!!!!!!!!!
# def updateLog(current_student_id):
#     cursor.execute("UPDATE Log SET logout_time = %s WHERE log_id = %s;" % (datetime.now(), currentlog))
#     db_connection.commit()


# ---------------------------------

# ----------get log-------

def getLog(current_student_id):
    cursor.execute(
        """SELECT log_id, login_time, logout_time, TIMEDIFF(logout_time,login_time) AS Duration FROM Log WHERE student_id = '%s' ORDER BY login_time DESC;""" % (
            current_student_id))
    results = cursor.fetchall()
    return results


# -----------get last log-------------

def getLastLog(current_student_id):
    cursor.execute(
        "SELECT login_time FROM Log WHERE Log.student_id = '%s' ORDER BY login_time DESC LIMIT 1;" % current_student_id)
    results = cursor.fetchall()
    return results


def getStudentInfo(current_student_id):
    cursor.execute("SELECT student_id, email_address FROM Student WHERE student_id = '%s';" % current_student_id)
    print('getStudentInfo query: ', "SELECT student_id, email_address FROM Student WHERE student_id = '%s';" % current_student_id)
    results = cursor.fetchall()
    return results
