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
  `current_login_time` datetime NOT NULL,
  `email_address` varchar(50) NOT NULL,
  PRIMARY KEY(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- sample value
INSERT INTO Student (student_id, name, current_login_time, email_address)
VALUES ("0001", "Jeff", NOW() , "comp3278grp19@gmail.com");

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
VALUES ("COMP3278_1A", "Introduction to database management systems", "This course studies the principles, design, administration, and implementation of database management systems. Topics include: entity-relationship model, relational model, relational algebra, database design and normalization, database query languages, indexing schemes, integrity and concurrency control."),
("COMP3230_1A", "Principles of operating systems","Operating system structures, process and thread, CPU scheduling, process synchronization, deadlocks, memory management, file systems, I/O systems and device driver, mass-storage structure and disk scheduling, case studies.");


DROP TABLE IF EXISTS `news_announcement`;

-- Create TABLE 'news_announcement'
CREATE TABLE `news_announcement` (
  `course_id` varchar(12) NOT NULL,
  `news_announcement` varchar(1000) NOT NULL,
  PRIMARY KEY(course_id, news_announcement),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO news_announcement (course_id, news_announcement)
VALUES ("COMP3278_1A","Dear students, We will resume face-to-face teaching tomorrow."),
("COMP3230_1A","Hi all,

The attached file is the summary of the mid-term exam. If you have any questions, please feel free to contact me.

Best,

Xie ZHANG");

DROP TABLE IF EXISTS `Log`;

-- Create TABLE 'Log'
CREATE TABLE `Log` (
  `log_id` varchar(10) NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `login_time` datetime NOT NULL,
  `logout_time` datetime NOT NULL,
  PRIMARY KEY(log_id),
  FOREIGN KEY(student_id) REFERENCES Student(student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
VALUES ("0001", "COMP3230_1A"), ("0001", "COMP3278_1A");

DROP TABLE IF EXISTS `Lecture`;

-- Create TABLE 'Lecture'
CREATE TABLE `Lecture` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(100),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Lecture (class_id, course_id, `date`, `starttime`, `endtime`, room, zoom_link)
VALUES ("COMP3278_1A", "1",'22/11/2022', '13:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3278_1A", "2", '29/11/2022', '13:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09"),
("COMP3230_1A", "1", '21/11/2022', '10:30', '12:30', "CYCP-2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9"),
("COMP3230_1A", "2", '24/11/2022', '10:30', '12:30', "CYCP-2", "https://hku.zoom.us/rec/share/rxQkV5qC5cKvF4psOFDUiQXXbXrccKlDfSb5OFohnnSKnv1Cn4ayZ1mrB-yvALLg.OQ2Ia3-JEzVJoGf9");


DROP TABLE IF EXISTS `Tutorial`;

-- Create TABLE 'Tutorial'
CREATE TABLE `Tutorial` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `date` date NOT NULL,
  `starttime` time NOT NULL,
  `endtime` time NOT NULL,
  `room` varchar(10),
  `zoom_link` varchar(100),
  PRIMARY KEY(class_id, course_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Tutorial (class_id, course_id, `date`, `starttime`, `endtime`, room, zoom_link)
VALUES ("COMP3278_1A", "1", '24/11/2022', '14:30', '15:30', "MWT2", "https://hku.zoom.us/j/96226740999?pwd=ZER1UUdxSVVhQzNXbXFkUDd3WjRBdz09");

DROP TABLE IF EXISTS `Lecture_Note`;

-- Create TABLE 'Lecture_Note'
CREATE TABLE `Lecture_Note` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(100),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Lecture(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Lecture (class_id, course_id, note_link)
VALUES ("COMP3278_1A", "1", "https://moodle.hku.hk/mod/resource/view.php?id=2665229"),
("COMP3278_1A", "2", "https://moodle.hku.hk/mod/resource/view.php?id=2694930"),
("COMP3230_1A", "1", "https://moodle.hku.hk/mod/resource/view.php?id=2639596"),
("COMP3230_1A", "2", "https://moodle.hku.hk/mod/resource/view.php?id=2639597");

DROP TABLE IF EXISTS `Tutorial_Note`;

-- Create TABLE 'Tutorial_Note'
CREATE TABLE `Tutorial_Note` (
  `course_id` varchar(12) NOT NULL,
  `class_id` varchar(3) NOT NULL,
  `note_link` varchar(100),
  PRIMARY KEY(class_id, course_id, note_link),
  FOREIGN KEY(class_id) REFERENCES Tutorial(class_id),
  FOREIGN KEY(course_id) REFERENCES Course(course_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO Tutorial (class_id, course_id, note_link)
VALUES ("COMP3278_1A", "1", "https://moodle.hku.hk/mod/resource/view.php?id=2668112");

-- # Create TABLE 'Course'
-- # Create TABLE 'Classroom'
-- # Create other TABLE...


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
