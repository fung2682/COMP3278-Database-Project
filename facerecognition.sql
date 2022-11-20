-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

-- --------------------------------------------------------

--
-- Table structure for table `Student`


DROP TABLE IF EXISTS `Student`;

-- Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email_address` varchar(50) NOT NULL,
  PRIMARY KEY(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- sample value
INSERT INTO Student (student_id, name, email_address)
VALUES ("0001", "JEFF", "comp3278grp19@gmail.com");
INSERT INTO Student (student_id, name, email_address)
VALUES ("0002", "STEPHANIE", "comp3278grp19@gmail.com");

DROP TABLE IF EXISTS `Course`;

-- Create TABLE 'Course'
CREATE TABLE `Course` (
  `course_id` varchar(12) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(1000) NOT NULL,
  PRIMARY KEY(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


-- sample value
INSERT INTO Course (course_id, name, description)
VALUES ("COMP3278_1A", "Introduction to database management systems", "This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control.
Lectures and Tutorials:
every Thursday: 1:30pm-3:20pm (Lecture)
every Monday: 2:30pm-3:20pm (Tutorial)

Venue:  MWT2 and Zoom (F2F and online section will be conducted in parallel for all lectures and tutorials)

Office Hours	Dr. Ping Luo: Every Monday 10:00am-11:00am, CB-326 (By appointment)
* Please send me an email in advance so that we can better organize the consultation schedule for you.
Course Assessment:
2 written assignments (30%, that is 15% for each assignment).
1 group project (20%).
1 group SQL challenge (10% bonus).
Final examination (50%)."),
("COMP3230_1A", "Principles of operating systems","Operating system structures, process and thread, CPU scheduling, process 
 synchronization, deadlocks, memory management, file systems, I/O systems and device driver, mass-storage structure and disk scheduling, case studies."),
("COMP3353_1A", "Bioinformatics", "The goal of the course is for students to be grounded in basic bioinformatics concepts, 
 algorithms, tools, and databases. Students will be leaving the course with hands-on bioinformatics analysis experience and 
 empowered to conduct independent bioinformatics analyses. We will study: 1) algorithms, especially those for sequence alignment 
 and assembly, which comprise the foundation of the rapid development of bioinformatics and DNA sequencing; 2) the leading bioinformatics 
 tools for comparing and analyzing genomes starting from raw sequencing data; 3) the functions and organization of a few essential bioinformatics 
 databases and learn how they support various types of bioinformatics analysis.");


DROP TABLE IF EXISTS `news_announcement`;

-- Create TABLE 'news_announcement'
CREATE TABLE `news_announcement` (
  `course_id` varchar(12) NOT NULL,
  `news_announcement` varchar(1000) NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY(course_id, news_announcement),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO news_announcement (course_id, news_announcement, update_time)
VALUES ("COMP3278_1A","Dear students, We will resume face-to-face teaching tomorrow.", NOW()),
("COMP3230_1A","Hi all,
The attached file is the summary of the mid-term exam. If you have any questions, please feel free to contact me.
Best,
Xie ZHANG", NOW()),
("COMP3278_1A","Welcome to COMP3278A.", date('2022-8-25')),
("COMP3353_1A","Welcome to COMP3353A.", date('2022-8-24'));

DROP TABLE IF EXISTS `Log`;

-- Create TABLE 'Log'
CREATE TABLE `Log` (
  `log_id` int NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `login_time` datetime NOT NULL,
  `logout_time` datetime NOT NULL,
  PRIMARY KEY(log_id),
  FOREIGN KEY(student_id) REFERENCES Student(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Log VALUES (0,"0001",DATE('2022-10-20'),DATE('2022-10-21'));

DROP TABLE IF EXISTS `Study`;

-- Create TABLE 'Study'
CREATE TABLE `Study` (
  `student_id` varchar(10) NOT NULL,
  `course_id` varchar(12) NOT NULL,
  PRIMARY KEY(student_id, course_id),
  FOREIGN KEY(student_id) REFERENCES Student(student_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Study (student_id, course_id)
VALUES ("0001", "COMP3230_1A"), ("0001", "COMP3278_1A"), ("0001", "COMP3353_1A");

DROP TABLE IF EXISTS `Lecture`;

-- Create TABLE 'Lecture'
CREATE TABLE `Lecture` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(1000),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Lecture (course_id, class_id, `date`, `starttime`, `endtime`, room, zoom_link)
VALUES ("COMP3278_1A", "L1",'2022-11-22', '13:30', '15:30', "MWT5", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "L2", '2022-11-25', '13:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "L3", '2022-11-29', '13:30', '15:30', "MWT5", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "L4", '2022-12-02', '11:30', '12:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3230_1A", "L1", '2022-11-21', '10:30', '12:30', "CYCP-2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3230_1A", "L2", '2022-11-24', '11:30', '12:30', "CYCP-3", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3230_1A", "L1", '2022-11-28', '10:30', '12:30', "CYCP-2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3230_1A", "L1", '2022-12-01', '11:30', '12:30', "CYCP-3", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3353_1A", "L1", '2022-11-21', '12:30', '14:30', "CYCC", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3353_1A", "L2", '2022-11-25', '15:30', '16:30', "CYCA", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3353_1A", "L3", '2022-11-28', '12:30', '14:30', "CYCC", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3353_1A", "L4", '2022-12-02', '15:30', '16:30', "CYCA", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09");



DROP TABLE IF EXISTS `Tutorial`;

-- Create TABLE 'Tutorial'
CREATE TABLE `Tutorial` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(1000),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Tutorial (course_id, class_id, `date`, `starttime`, `endtime`, room, zoom_link)
VALUES ("COMP3278_1A", "T1", '2022-11-24', '14:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "T2", '2022-12-01', '14:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "T1", '2022-11-22', '11:30', '12:30', "MWT2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3278_1A", "T2", '2022-11-29', '11:30', '12:30', "MWT2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3353_1A", "T1", '2022-11-23', '13:30', '14:30', "CYCC", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3353_1A", "T2", '2022-11-23', '13:30', '14:30', "CYCC", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09");


DROP TABLE IF EXISTS `Lecture_Note`;

-- Create TABLE 'Lecture_Note'
CREATE TABLE `Lecture_Note` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(1000),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Lecture(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Lecture_Note (course_id, class_id, note_link)
VALUES ("COMP3278_1A", "L1", "https://moodle.hku.hk/mod/resource/view.php?id=2665229"),
("COMP3278_1A", "L2", "https://moodle.hku.hk/mod/resource/view.php?id=2694930"),
("COMP3230_1A", "L1", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3230_1A", "L2", "https://moodle.hku.hk/mod/resource/view.php?id=2639597"),
("COMP3278_1A", "L3", "https://moodle.hku.hk/mod/resource/view.php?id=2665229"),
("COMP3278_1A", "L4", "https://moodle.hku.hk/mod/resource/view.php?id=2694930"),
("COMP3230_1A", "L3", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3230_1A", "L4", "https://moodle.hku.hk/mod/resource/view.php?id=2639597"),
("COMP3353_1A", "L1", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3353_1A", "L2", "https://moodle.hku.hk/mod/resource/view.php?id=2639597"),
("COMP3353_1A", "L3", "https://moodle.hku.hk/mod/resource/view.php?id=2665229"),
("COMP3353_1A", "L4", "https://moodle.hku.hk/mod/resource/view.php?id=2694930");

DROP TABLE IF EXISTS `Tutorial_Note`;

-- Create TABLE 'Tutorial_Note'
CREATE TABLE `Tutorial_Note` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(1000),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Tutorial(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Tutorial_Note (course_id, class_id, note_link)
VALUES ("COMP3278_1A", "T1", "https://moodle.hku.hk/mod/resource/view.php?id=2668112"),
("COMP3278_1A", "T2", "https://moodle.hku.hk/mod/resource/view.php?id=2668112"),
("COMP3353_1A", "T1", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3353_1A", "T2", "https://moodle.hku.hk/mod/resource/view.php?id=2639597"),
("COMP3230_1A", "T1", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3230_1A", "T2", "https://moodle.hku.hk/mod/resource/view.php?id=2639597");

DROP TABLE IF EXISTS `Teacher`;

-- Create TABLE 'Teacher'
CREATE TABLE `Teacher` (
  `teacher_id` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `office` varchar(50),
  PRIMARY KEY(teacher_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Teacher (teacher_id, name, email, office)
VALUES ("cs1", "Ping Luo", "pluo@cs.hku.hk", "CB326"),
("cs2","Yao Mu", "muyao@connect.hku.hk","CB123"),
("cs3","Yao Lai","laiyao@connect.hku.hk", "CB123"),
("cs4","Yizhou Li", "liyizhuo@connect.hku.hk", "CB123"),
("cs5", "Luo Ruibang", "rbluo@cs.hku.hk","CYC422");


DROP TABLE IF EXISTS `Lecturer`;

-- Create TABLE 'Lecturer'
CREATE TABLE `Lecturer` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  PRIMARY KEY(course_id,class_id,teacher_id),
  FOREIGN KEY(class_id) REFERENCES Lecture(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Lecturer (course_id, class_id, teacher_id)
VALUES ("COMP3278_1A", "L1", "cs1"),
("COMP3278_1A", "L2", "cs1"),
("COMP3278_1A", "L3", "cs1"),
("COMP3278_1A", "L4", "cs1"),
("COMP3230_1A", "L1", "cs1"),
("COMP3230_1A", "L2", "cs1"),
("COMP3230_1A", "L3", "cs1"),
("COMP3230_1A", "L4", "cs1"),
("COMP3353_1A", "L1", "cs5"),
("COMP3353_1A", "L2", "cs5"),
("COMP3353_1A", "L3", "cs5"),
("COMP3353_1A", "L4", "cs5");

DROP TABLE IF EXISTS `Tutor`;

-- Create TABLE 'Tutor'
CREATE TABLE `Tutor` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `teacher_id` varchar(10) NOT NULL,
  PRIMARY KEY(course_id,class_id,teacher_id),
  FOREIGN KEY(class_id) REFERENCES Tutorial(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Tutor (course_id, class_id, teacher_id)
VALUES ("COMP3278_1A", "T1", "cs2"),
("COMP3278_1A", "T2", "cs2"),
("COMP3230_1A", "T1", "cs3"),
("COMP3230_1A", "T2", "cs3"),
("COMP3353_1A", "T1", "cs4"),
("COMP3353_1A", "T2", "cs4");


-- # Create TABLE 'Course'
-- # Create TABLE 'Classroom'
-- # Create other TABLE...


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
