-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: moc
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (13,'2020-11-19 03:02:01.240374','38','philongg2000@gmail.com',3,'',25,39),(14,'2020-11-19 03:28:54.532703','0','Thao',1,'[{\"added\": {}}]',8,39),(15,'2020-11-19 03:31:13.346689','1','Math',1,'[{\"added\": {}}]',7,39),(16,'2020-11-19 03:31:44.368689','7','Division',1,'[{\"added\": {}}]',21,39),(17,'2020-11-19 03:38:15.994814','5','thao@gmail.com-Math',1,'[{\"added\": {}}]',26,39),(18,'2020-11-25 08:57:55.913945','41','thao@gmail.com',2,'[{\"changed\": {\"fields\": [\"Is staff\"]}}]',25,39),(19,'2020-12-05 02:40:58.270716','2','database',1,'[{\"added\": {}}]',7,39),(20,'2020-12-05 02:44:09.741455','43','philongg2000@gmail.com',3,'',25,39),(21,'2020-12-08 14:18:52.094530','5','thao@gmail.com-database',2,'[{\"changed\": {\"fields\": [\"Course\"]}}]',26,39),(22,'2020-12-08 14:19:08.773778','6','thao@gmail.com-Math',1,'[{\"added\": {}}]',26,39),(23,'2020-12-08 14:50:03.835653','41','Thao',3,'',23,41),(24,'2020-12-08 15:08:13.518917','48','plong@gmail.com',1,'[{\"added\": {}}]',25,39),(25,'2020-12-08 15:09:10.397810','48','plong@gmail.com',2,'[{\"changed\": {\"fields\": [\"Is staff\"]}}]',25,39),(26,'2020-12-08 15:12:53.619759','2','long',1,'[{\"added\": {}}]',8,39),(27,'2020-12-08 15:37:13.690172','4','1001 tu the',3,'',7,48),(28,'2020-12-08 15:37:13.694448','3','1001 chuyen co tich',3,'',7,48),(29,'2020-12-08 15:39:01.217099','7','alibaba',3,'',7,48),(30,'2020-12-08 15:39:01.221091','6','alibaba',3,'',7,48),(31,'2020-12-08 15:39:01.226074','5','alibaba',3,'',7,48);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 22:45:45
