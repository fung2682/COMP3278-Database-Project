import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime

useremail = "comp3278grp19@gmail.com"


#0: name; 1: course_id, 2: class_id, 3: date, 4: starttime, 5: endtime, 6: room, 7: zoom_link, 8: news_announcement(list), 9. note_link (list), 10: course_teacher (2D list), 11: class_teacher (tuple), 12: class type
#def send_template(course_id, class_id, date, starttime, endtime, room, zoom_link, news_announcement, note_link, course_teacher, class_teacher, classtype):
def send_template(name, course_id, class_id, date, starttime, endtime, room, zoom_link, news_announcement, note_link, course_teacher, class_teacher, classtype):
    env = Environment(
        loader=FileSystemLoader(searchpath="./"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    temp = env.get_template('email_template.html')
    template1 = temp.render(**locals())
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"ICMS: Remember to attend {course_id} {classtype}-{class_id}"
    msg['From'] = "comp3278grp19@gmail.com"
    msg['To'] = useremail

    msg.attach(MIMEText(template1,'html'))
    
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()
    
    mail.login('comp3278grp19@gmail.com', 'qznqczmkjfzzdzyw')
    mail.sendmail('comp3278grp19@gmail.com', useremail, msg.as_string())
    mail.quit()
