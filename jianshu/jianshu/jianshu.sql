/*
Navicat MySQL Data Transfer

Source Server         : 本地mysql
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : jianshu

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2020-07-09 09:56:44
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `content` longtext,
  `author` varchar(255) DEFAULT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `pub_time` datetime DEFAULT NULL,
  `origin_url` varchar(255) DEFAULT NULL,
  `article_id` varchar(20) DEFAULT NULL,
  `read_count` bigint(20) DEFAULT NULL,
  `like_count` bigint(20) DEFAULT NULL,
  `word_count` bigint(20) DEFAULT NULL,
  `subjects` text,
  `commit_count` int(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8;
