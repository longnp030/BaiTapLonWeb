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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (39,'pbkdf2_sha256$216000$C7OdRDxLXq6k$b9mw6kqtE3/HZIObF+SJbEfxHA7/NBCD5nKtHHfzu+Y=','2020-12-08 15:09:05.649358','thepql37@gmail.com',1,1,1),(40,'pbkdf2_sha256$216000$7L3jDrHvao8a$YgymNF3O8XG0nmZ+f3c72ir5rQqyDUbM68BrB63xzUA=','2020-11-19 03:34:17.179086','thepho@gmail.com',1,0,0),(41,'pbkdf2_sha256$216000$iW1SJtoYpMgz$riS30ERMOmEZ7cnzpo41Sjczc3HkfUOtoKWz/LcX+fQ=','2020-12-08 15:17:25.556220','thao@gmail.com',1,1,0),(42,'pbkdf2_sha256$216000$9CuanfvSeSrz$+VDuFRyLT42mN58li+Wt5jiN2mwNgkmP4mA0RUONu2Y=','2020-12-08 14:05:19.140821','duong@gmail.com',1,0,0),(44,'pbkdf2_sha256$216000$IZkjKvepLLR9$k3XUkDEGvzyC/EgITBSy1xv2e736UEsi9xBB6NchzUg=','2020-11-25 16:59:53.031511','thepqlna@gmail.com',1,0,0),(45,'pbkdf2_sha256$216000$PQa7kgueLKMW$/glN9DEls3AftcYanKoiJA5qdzZNJdTAFQZIxYPHEA8=','2020-12-07 08:17:35.161866','huan@gmail.com',1,0,0),(46,'pbkdf2_sha256$216000$WW0SZxIEYcN5$ojCcw9tEMTKsLdTeh9G/1tTRZiaWQA+LFuoaaN+1xKU=','2020-11-26 16:00:24.265860','phuong@gmail.com',1,0,0),(47,'pbkdf2_sha256$216000$afXFTV6TfxW5$xMU205bfLCKOnW1qT55nVaaz1LTLCjOEXfFP72dIyQc=','2020-12-08 14:23:14.351476','nhung@gmail.com',1,0,0),(48,'pbkdf2_sha256$216000$0nAMJGhly6CS$RmtTXZkfMH0gjVY6hbmCssKocKWp5t8HmWyTcK0YBO0=','2020-12-08 15:24:31.121110','plong@gmail.com',1,1,0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 22:45:46
