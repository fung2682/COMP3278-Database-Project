DROP TABLE IF EXISTS `Student`;

-- Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `current_login_time` datetime NOT NULL,
  `email_address` varchar(50) NOT NULL,
  PRIMARY KEY(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- sample value
insert into Student (student_id, name, current_login_time, email_address)
values (0001, "Peter", NOW() , "peter1234@connect.hku.hk");

DROP TABLE IF EXISTS `Course`;

-- Create TABLE 'Course'
CREATE TABLE `Course` (
  `course_id` varchar(8) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `news_announcement`;

-- Create TABLE 'news_announcement'
CREATE TABLE `news_announcement` (
  `course_id` varchar(8) NOT NULL,
  `news_announcement` varchar(1000) NOT NULL,
  PRIMARY KEY(course_id, news_announcement),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Log`;

-- Create TABLE 'Log'
CREATE TABLE `Log` (
  `log_id` int NOT NULL,
  `student_id` int NOT NULL,
  `login_time` datetime NOT NULL,
  `logout_time` datetime NOT NULL,
  PRIMARY KEY(log_id),
  FOREIGN KEY(student_id) REFERENCES Student(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Study`;

-- Create TABLE 'Study'
CREATE TABLE `Study` (
  `student_id` int NOT NULL,
  `course_id` varchar(8) NOT NULL,
  PRIMARY KEY(student_id, course_id),
  FOREIGN KEY(student_id) REFERENCES Student(student_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Lecture`;

-- Create TABLE 'Lecture'
CREATE TABLE `Lecture` (
  `class_id` varchar(3) NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(100),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Tutorial`;

-- Create TABLE 'Tutorial'
CREATE TABLE `Tutorial` (
  `class_id` varchar(3) NOT NULL,
  `course_id` varchar(8) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(100),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Lecture_Note`;

-- Create TABLE 'Lecture_Note'
CREATE TABLE `Lecture_Note` (
  `course_id` varchar(8) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(100),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Lecture(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS `Tutorial_Note`;

-- Create TABLE 'Tutorial_Note'
CREATE TABLE `Tutorial_Note` (
  `course_id` varchar(8) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(100),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Tutorial(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;