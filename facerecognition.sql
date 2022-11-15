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
-- insert into Student (student_id, name, current_login_time, email_address)
-- values (0001, "Peter", NOW() , "peter1234@connect.hku.hk");

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
