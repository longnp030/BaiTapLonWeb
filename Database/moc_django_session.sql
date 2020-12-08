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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1mtkz6otxho9roj6sptkrcx4iqaa5x64','.eJxVjDsOwjAQBe_iGlmLf7Ep6TmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVF6CBOv2NCeua6E35gvTdJrS7zlOSuyIN2eWucX9fD_Tso2MtWG_BMZ2WBaXADGlTGeB90Hlk5shrcqF1AA4CZvAqYdFLJQibiDbL4fAH3Izf4:1klNa0:4uTpRAq9YdtpomQWPRIaxExP53aQ5s9nLXEPXMdPsHs','2020-12-19 02:45:48.226898'),('6nar75hw4hurlh1b0i4eesy6d10hadza','.eJxVjDsOwjAQBe_iGlmLf7Ep6TmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVF6CBOv2NCeua6E35gvTdJrS7zlOSuyIN2eWucX9fD_Tso2MtWG_BMZ2WBaXADGlTGeB90Hlk5shrcqF1AA4CZvAqYdFLJQibiDbL4fAH3Izf4:1kmdoW:oYV0eApiWjRUUzM-dse3nwrdaCoWRjaBAmpwuc0Gd0U','2020-12-22 14:18:00.608016'),('a1awqonv2ho78mjcya94ygmseputfjdh','.eJxVjMsOwiAQRf-FtSEwA3Rw6d5vIMOjUjU0Ke3K-O_apAvd3nPOfYnA21rD1ssSpizOwmhx-h0jp0dpO8l3brdZprmtyxTlrsiDdnmdc3leDvfvoHKv39pr5Q0n9pAUFzOmQQOSRSYayMYBLRbtKGsclQNClzJBNgDgrRnRiPcH5vE2vQ:1kmek1:StXKd8IU3wcVZBW4rf7r98m_jb4xax2e0XPJLWRcqGo','2020-12-22 15:17:25.560210'),('bvmxb0vqolfu4ok4c9khr8duftppm9ix','.eJxVjM0OwiAQhN-FsyECXbp49O4zkGUXpGpK0p-T8d1tkx40c_vmm3mrSOtS4zrnKQ6iLsoFdfqFifiZx72RB433prmNyzQkvSv6aGd9a5Jf18P9O6g0122NQMWzDQ6FMpCjEsCfrQs9y4YNAne-E1MAMIMtuMV6YxIjhr5j9fkCCqA30w:1khqbj:mZqU7yBORt9nvYJrE0aeedLGUbt0ZkRtcbbRee2yuUU','2020-12-09 08:56:59.874185'),('copdfvlqwsmpadhprb22sct5oybqrqs5','.eJxVjMsOwiAQRf-FtSGFwgAu3fsNzQwzSNXQpI-V8d-1SRe6veec-1IDbmsdtkXmYWR1Vs6q0-9ImB_SdsJ3bLdJ56mt80h6V_RBF32dWJ6Xw_07qLjUbw3BY0bxoQgk6FJ0lpCTZCBvYifBEUGxACyRyUQsRbgn7tk5CgbU-wMkdDkL:1klNWo:V9Jt4rOWjXeQo9vt48sgnDw1kFij7YI7-WDmsoL9oiA','2020-12-19 02:42:30.404359'),('exdvsh3zonjfj33rt3us3mphlp3r0prt','.eJxVjDsOwjAQBe_iGlmx499S0nMGa-3d4ACypTipEHeHSCmgfTPzXiLitpa4dV7iTOIszChOv2PC_OC6E7pjvTWZW12XOcldkQft8tqIn5fD_Tso2Mu3HpJzOYTMygMikFVWjU7ZNCUaA04avEccNDjUzrI12hvwlBCACYHF-wMDBTgd:1khqrj:7nWHI6UbvHE43q-bCwG2vfpJtHfolZsRDO_2yIr3RIw','2020-12-09 09:13:31.285582'),('ld3z7xuoo1mkkfqel9hg2m64xzj5fxie','.eJxVjDsOwjAQBe_iGlmLf7Ep6TmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVF6CBOv2NCeua6E35gvTdJrS7zlOSuyIN2eWucX9fD_Tso2MtWG_BMZ2WBaXADGlTGeB90Hlk5shrcqF1AA4CZvAqYdFLJQibiDbL4fAH3Izf4:1kmUwv:GyhASuh2bnsZebnHntTgfrHCLwdT7NG_W9NtgQ4iGbY','2020-12-22 04:50:05.239817'),('yfkwqh604b70hkodlx3icmw59l9u4oxw','.eJxVjDsOwjAQBe_iGllOvP4sJX3OYPmzxgFkS3FSIe5OIqWAdmbeezPnt7W4rdPi5sSuDCy7_MLg45PqYdLD13vjsdV1mQM_En7azqeW6HU727-D4nvZ16jQZpSa0ERlksdBIUAiGqSKMEoLOQlJABDzTrQVRmaJ5IPGUaNgny_yKjdL:1kmeqt:S24TVzsYg5ciiIxSmhQZGC1vtAOAxsXZFCQe_K8pE0A','2020-12-22 15:24:31.131083');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
