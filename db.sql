/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 5.5.5-10.1.13-MariaDB : Database - rice_crop_leaf
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`rice_crop_leaf` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `rice_crop_leaf`;

/*Table structure for table `chatting` */

DROP TABLE IF EXISTS `chatting`;

CREATE TABLE `chatting` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `sender_email` varchar(100) DEFAULT NULL,
  `receiver_email` varchar(100) DEFAULT NULL,
  `chat_date` varchar(100) DEFAULT NULL,
  `chat_time` varchar(100) DEFAULT NULL,
  `msg` varchar(100) DEFAULT NULL,
  `farmer_name` varchar(100) DEFAULT NULL,
  `farmer_email` varchar(100) DEFAULT NULL,
  `expert_email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `user_Type` varchar(100) DEFAULT NULL,
  `user_Name` varchar(100) DEFAULT NULL,
  `user_Email` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `user_Phone` varchar(100) DEFAULT NULL,
  `user_Addr` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
