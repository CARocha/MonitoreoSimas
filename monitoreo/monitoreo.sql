-- MySQL dump 10.13  Distrib 5.1.52, for redhat-linux-gnu (i386)
--
-- Host: localhost    Database: monitoreo
-- ------------------------------------------------------
-- Server version	5.1.52

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_tools_dashboard_preferences`
--

DROP TABLE IF EXISTS `admin_tools_dashboard_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_tools_dashboard_preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `data` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_tools_dashboard_preferences_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_tools_dashboard_preferences`
--

LOCK TABLES `admin_tools_dashboard_preferences` WRITE;
/*!40000 ALTER TABLE `admin_tools_dashboard_preferences` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_tools_dashboard_preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin_tools_menu_bookmark`
--

DROP TABLE IF EXISTS `admin_tools_menu_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_tools_menu_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_tools_menu_bookmark_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_tools_menu_bookmark`
--

LOCK TABLES `admin_tools_menu_bookmark` WRITE;
/*!40000 ALTER TABLE `admin_tools_menu_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `admin_tools_menu_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'zonas');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_425ae3c4` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,32),(2,1,33),(3,1,34),(4,1,35),(5,1,36),(6,1,37),(7,1,38),(8,1,39),(9,1,43),(10,1,44),(11,1,45),(12,1,46),(13,1,47),(14,1,48),(15,1,49),(16,1,50),(17,1,51),(18,1,31);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_403f60f` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=286 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add bookmark',1,'add_bookmark'),(2,'Can change bookmark',1,'change_bookmark'),(3,'Can delete bookmark',1,'delete_bookmark'),(4,'Can add dashboard preferences',2,'add_dashboardpreferences'),(5,'Can change dashboard preferences',2,'change_dashboardpreferences'),(6,'Can delete dashboard preferences',2,'delete_dashboardpreferences'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add user',5,'add_user'),(14,'Can change user',5,'change_user'),(15,'Can delete user',5,'delete_user'),(16,'Can add message',6,'add_message'),(17,'Can change message',6,'change_message'),(18,'Can delete message',6,'delete_message'),(19,'Can add content type',7,'add_contenttype'),(20,'Can change content type',7,'change_contenttype'),(21,'Can delete content type',7,'delete_contenttype'),(22,'Can add session',8,'add_session'),(23,'Can change session',8,'change_session'),(24,'Can delete session',8,'delete_session'),(25,'Can add site',9,'add_site'),(26,'Can change site',9,'change_site'),(27,'Can delete site',9,'delete_site'),(28,'Can add log entry',10,'add_logentry'),(29,'Can change log entry',10,'change_logentry'),(30,'Can delete log entry',10,'delete_logentry'),(31,'Can add departamento',11,'add_departamento'),(32,'Can change departamento',11,'change_departamento'),(33,'Can delete departamento',11,'delete_departamento'),(34,'Can add municipio',12,'add_municipio'),(35,'Can change municipio',12,'change_municipio'),(36,'Can delete municipio',12,'delete_municipio'),(37,'Can add comunidad',13,'add_comunidad'),(38,'Can change comunidad',13,'change_comunidad'),(39,'Can delete comunidad',13,'delete_comunidad'),(40,'Can add migration history',14,'add_migrationhistory'),(41,'Can change migration history',14,'change_migrationhistory'),(42,'Can delete migration history',14,'delete_migrationhistory'),(43,'Can add recolector',15,'add_recolector'),(44,'Can change recolector',15,'change_recolector'),(45,'Can delete recolector',15,'delete_recolector'),(46,'Can add organizaciones',16,'add_organizaciones'),(47,'Can change organizaciones',16,'change_organizaciones'),(48,'Can delete organizaciones',16,'delete_organizaciones'),(49,'Can add encuesta',17,'add_encuesta'),(50,'Can change encuesta',17,'change_encuesta'),(51,'Can delete encuesta',17,'delete_encuesta'),(52,'Can add tenencia',18,'add_tenencia'),(53,'Can change tenencia',18,'change_tenencia'),(54,'Can delete tenencia',18,'delete_tenencia'),(55,'Can add org gremiales',19,'add_orggremiales'),(56,'Can change org gremiales',19,'change_orggremiales'),(57,'Can delete org gremiales',19,'delete_orggremiales'),(58,'Can add beneficios obtenido',20,'add_beneficiosobtenido'),(59,'Can change beneficios obtenido',20,'change_beneficiosobtenido'),(60,'Can delete beneficios obtenido',20,'delete_beneficiosobtenido'),(61,'Can add ser miembro',21,'add_sermiembro'),(62,'Can change ser miembro',21,'change_sermiembro'),(63,'Can delete ser miembro',21,'delete_sermiembro'),(64,'Can add organizacion gremial',22,'add_organizaciongremial'),(65,'Can change organizacion gremial',22,'change_organizaciongremial'),(66,'Can delete organizacion gremial',22,'delete_organizaciongremial'),(67,'Can add org comunitarias',23,'add_orgcomunitarias'),(68,'Can change org comunitarias',23,'change_orgcomunitarias'),(69,'Can delete org comunitarias',23,'delete_orgcomunitarias'),(70,'Can add beneficio org comunitaria',24,'add_beneficioorgcomunitaria'),(71,'Can change beneficio org comunitaria',24,'change_beneficioorgcomunitaria'),(72,'Can delete beneficio org comunitaria',24,'delete_beneficioorgcomunitaria'),(73,'Can add no organizado',25,'add_noorganizado'),(74,'Can change no organizado',25,'change_noorganizado'),(75,'Can delete no organizado',25,'delete_noorganizado'),(76,'Can add organizacion comunitaria',26,'add_organizacioncomunitaria'),(77,'Can change organizacion comunitaria',26,'change_organizacioncomunitaria'),(78,'Can delete organizacion comunitaria',26,'delete_organizacioncomunitaria'),(79,'Can add uso',27,'add_uso'),(80,'Can change uso',27,'change_uso'),(81,'Can delete uso',27,'delete_uso'),(82,'Can add uso tierra',28,'add_usotierra'),(83,'Can change uso tierra',28,'change_usotierra'),(84,'Can delete uso tierra',28,'delete_usotierra'),(85,'Can add maderable',29,'add_maderable'),(86,'Can change maderable',29,'change_maderable'),(87,'Can delete maderable',29,'delete_maderable'),(88,'Can add forrajero',30,'add_forrajero'),(89,'Can change forrajero',30,'change_forrajero'),(90,'Can delete forrajero',30,'delete_forrajero'),(91,'Can add energetico',31,'add_energetico'),(92,'Can change energetico',31,'change_energetico'),(93,'Can delete energetico',31,'delete_energetico'),(94,'Can add frutal',32,'add_frutal'),(95,'Can change frutal',32,'change_frutal'),(96,'Can delete frutal',32,'delete_frutal'),(97,'Can add existencia arboles',33,'add_existenciaarboles'),(98,'Can change existencia arboles',33,'change_existenciaarboles'),(99,'Can delete existencia arboles',33,'delete_existenciaarboles'),(100,'Can add actividad',34,'add_actividad'),(101,'Can change actividad',34,'change_actividad'),(102,'Can delete actividad',34,'delete_actividad'),(103,'Can add reforestacion',35,'add_reforestacion'),(104,'Can change reforestacion',35,'change_reforestacion'),(105,'Can delete reforestacion',35,'delete_reforestacion'),(106,'Can add animales',36,'add_animales'),(107,'Can change animales',36,'change_animales'),(108,'Can delete animales',36,'delete_animales'),(109,'Can add producto animal',37,'add_productoanimal'),(110,'Can change producto animal',37,'change_productoanimal'),(111,'Can delete producto animal',37,'delete_productoanimal'),(112,'Can add animales finca',38,'add_animalesfinca'),(113,'Can change animales finca',38,'change_animalesfinca'),(114,'Can delete animales finca',38,'delete_animalesfinca'),(115,'Can add cultivos',39,'add_cultivos'),(116,'Can change cultivos',39,'change_cultivos'),(117,'Can delete cultivos',39,'delete_cultivos'),(118,'Can add cultivos finca',40,'add_cultivosfinca'),(119,'Can change cultivos finca',40,'change_cultivosfinca'),(120,'Can delete cultivos finca',40,'delete_cultivosfinca'),(121,'Can add manejo agro',41,'add_manejoagro'),(122,'Can change manejo agro',41,'change_manejoagro'),(123,'Can delete manejo agro',41,'delete_manejoagro'),(124,'Can add opciones manejo',42,'add_opcionesmanejo'),(125,'Can change opciones manejo',42,'change_opcionesmanejo'),(126,'Can delete opciones manejo',42,'delete_opcionesmanejo'),(127,'Can add cultivos variedad',43,'add_cultivosvariedad'),(128,'Can change cultivos variedad',43,'change_cultivosvariedad'),(129,'Can delete cultivos variedad',43,'delete_cultivosvariedad'),(130,'Can add variedades',44,'add_variedades'),(131,'Can change variedades',44,'change_variedades'),(132,'Can delete variedades',44,'delete_variedades'),(133,'Can add semilla',45,'add_semilla'),(134,'Can change semilla',45,'change_semilla'),(135,'Can delete semilla',45,'delete_semilla'),(136,'Can add textura',46,'add_textura'),(137,'Can change textura',46,'change_textura'),(138,'Can delete textura',46,'delete_textura'),(139,'Can add profundidad',47,'add_profundidad'),(140,'Can change profundidad',47,'change_profundidad'),(141,'Can delete profundidad',47,'delete_profundidad'),(142,'Can add densidad',48,'add_densidad'),(143,'Can change densidad',48,'change_densidad'),(144,'Can delete densidad',48,'delete_densidad'),(145,'Can add pendiente',49,'add_pendiente'),(146,'Can change pendiente',49,'change_pendiente'),(147,'Can delete pendiente',49,'delete_pendiente'),(148,'Can add drenaje',50,'add_drenaje'),(149,'Can change drenaje',50,'change_drenaje'),(150,'Can delete drenaje',50,'delete_drenaje'),(151,'Can add suelo',51,'add_suelo'),(152,'Can change suelo',51,'change_suelo'),(153,'Can delete suelo',51,'delete_suelo'),(154,'Can add preparar',52,'add_preparar'),(155,'Can change preparar',52,'change_preparar'),(156,'Can delete preparar',52,'delete_preparar'),(157,'Can add traccion',53,'add_traccion'),(158,'Can change traccion',53,'change_traccion'),(159,'Can delete traccion',53,'delete_traccion'),(160,'Can add fertilizacion',54,'add_fertilizacion'),(161,'Can change fertilizacion',54,'change_fertilizacion'),(162,'Can delete fertilizacion',54,'delete_fertilizacion'),(163,'Can add conservacion',55,'add_conservacion'),(164,'Can change conservacion',55,'change_conservacion'),(165,'Can delete conservacion',55,'delete_conservacion'),(166,'Can add manejo suelo',56,'add_manejosuelo'),(167,'Can change manejo suelo',56,'change_manejosuelo'),(168,'Can delete manejo suelo',56,'delete_manejosuelo'),(169,'Can add rubros',57,'add_rubros'),(170,'Can change rubros',57,'change_rubros'),(171,'Can delete rubros',57,'delete_rubros'),(172,'Can add ingreso familiar',58,'add_ingresofamiliar'),(173,'Can change ingreso familiar',58,'change_ingresofamiliar'),(174,'Can delete ingreso familiar',58,'delete_ingresofamiliar'),(175,'Can add fuentes',59,'add_fuentes'),(176,'Can change fuentes',59,'change_fuentes'),(177,'Can delete fuentes',59,'delete_fuentes'),(178,'Can add tipo trabajo',60,'add_tipotrabajo'),(179,'Can change tipo trabajo',60,'change_tipotrabajo'),(180,'Can delete tipo trabajo',60,'delete_tipotrabajo'),(181,'Can add otros ingresos',61,'add_otrosingresos'),(182,'Can change otros ingresos',61,'change_otrosingresos'),(183,'Can delete otros ingresos',61,'delete_otrosingresos'),(184,'Can add piso',62,'add_piso'),(185,'Can change piso',62,'change_piso'),(186,'Can delete piso',62,'delete_piso'),(187,'Can add techo',63,'add_techo'),(188,'Can change techo',63,'change_techo'),(189,'Can delete techo',63,'delete_techo'),(190,'Can add tipo casa',64,'add_tipocasa'),(191,'Can change tipo casa',64,'change_tipocasa'),(192,'Can delete tipo casa',64,'delete_tipocasa'),(193,'Can add detalle casa',65,'add_detallecasa'),(194,'Can change detalle casa',65,'change_detallecasa'),(195,'Can delete detalle casa',65,'delete_detallecasa'),(196,'Can add equipos',66,'add_equipos'),(197,'Can change equipos',66,'change_equipos'),(198,'Can delete equipos',66,'delete_equipos'),(199,'Can add infraestructuras',67,'add_infraestructuras'),(200,'Can change infraestructuras',67,'change_infraestructuras'),(201,'Can delete infraestructuras',67,'delete_infraestructuras'),(202,'Can add propiedades',68,'add_propiedades'),(203,'Can change propiedades',68,'change_propiedades'),(204,'Can delete propiedades',68,'delete_propiedades'),(205,'Can add nombre herramienta',69,'add_nombreherramienta'),(206,'Can change nombre herramienta',69,'change_nombreherramienta'),(207,'Can delete nombre herramienta',69,'delete_nombreherramienta'),(208,'Can add herramientas',70,'add_herramientas'),(209,'Can change herramientas',70,'change_herramientas'),(210,'Can delete herramientas',70,'delete_herramientas'),(211,'Can add nombre transporte',71,'add_nombretransporte'),(212,'Can change nombre transporte',71,'change_nombretransporte'),(213,'Can delete nombre transporte',71,'delete_nombretransporte'),(214,'Can add transporte',72,'add_transporte'),(215,'Can change transporte',72,'change_transporte'),(216,'Can delete transporte',72,'delete_transporte'),(217,'Can add ahorro pregunta',73,'add_ahorropregunta'),(218,'Can change ahorro pregunta',73,'change_ahorropregunta'),(219,'Can delete ahorro pregunta',73,'delete_ahorropregunta'),(220,'Can add ahorro',74,'add_ahorro'),(221,'Can change ahorro',74,'change_ahorro'),(222,'Can delete ahorro',74,'delete_ahorro'),(223,'Can add da credito',75,'add_dacredito'),(224,'Can change da credito',75,'change_dacredito'),(225,'Can delete da credito',75,'delete_dacredito'),(226,'Can add ocupa credito',76,'add_ocupacredito'),(227,'Can change ocupa credito',76,'change_ocupacredito'),(228,'Can delete ocupa credito',76,'delete_ocupacredito'),(229,'Can add credito',77,'add_credito'),(230,'Can change credito',77,'change_credito'),(231,'Can delete credito',77,'delete_credito'),(232,'Can add alimentos',78,'add_alimentos'),(233,'Can change alimentos',78,'change_alimentos'),(234,'Can delete alimentos',78,'delete_alimentos'),(235,'Can add seguridad',79,'add_seguridad'),(236,'Can change seguridad',79,'change_seguridad'),(237,'Can delete seguridad',79,'delete_seguridad'),(238,'Can add causa',80,'add_causa'),(239,'Can change causa',80,'change_causa'),(240,'Can delete causa',80,'delete_causa'),(241,'Can add fenomeno',81,'add_fenomeno'),(242,'Can change fenomeno',81,'change_fenomeno'),(243,'Can delete fenomeno',81,'delete_fenomeno'),(244,'Can add graves',82,'add_graves'),(245,'Can change graves',82,'change_graves'),(246,'Can delete graves',82,'delete_graves'),(247,'Can add vulnerable',83,'add_vulnerable'),(248,'Can change vulnerable',83,'change_vulnerable'),(249,'Can delete vulnerable',83,'delete_vulnerable'),(250,'Can add pregunta riesgo',84,'add_preguntariesgo'),(251,'Can change pregunta riesgo',84,'change_preguntariesgo'),(252,'Can delete pregunta riesgo',84,'delete_preguntariesgo'),(253,'Can add riesgos',85,'add_riesgos'),(254,'Can change riesgos',85,'change_riesgos'),(255,'Can delete riesgos',85,'delete_riesgos'),(256,'Can add educacion',86,'add_educacion'),(257,'Can change educacion',86,'change_educacion'),(258,'Can delete educacion',86,'delete_educacion'),(259,'Can add salud',87,'add_salud'),(260,'Can change salud',87,'change_salud'),(261,'Can delete salud',87,'delete_salud'),(262,'Can add pregunta energia',88,'add_preguntaenergia'),(263,'Can change pregunta energia',88,'change_preguntaenergia'),(264,'Can delete pregunta energia',88,'delete_preguntaenergia'),(265,'Can add energia',89,'add_energia'),(266,'Can change energia',89,'change_energia'),(267,'Can delete energia',89,'delete_energia'),(268,'Can add tipo cocina',90,'add_tipococina'),(269,'Can change tipo cocina',90,'change_tipococina'),(270,'Can delete tipo cocina',90,'delete_tipococina'),(271,'Can add cocina',91,'add_cocina'),(272,'Can change cocina',91,'change_cocina'),(273,'Can delete cocina',91,'delete_cocina'),(274,'Can add fuente',92,'add_fuente'),(275,'Can change fuente',92,'change_fuente'),(276,'Can delete fuente',92,'delete_fuente'),(277,'Can add tratamiento',93,'add_tratamiento'),(278,'Can change tratamiento',93,'change_tratamiento'),(279,'Can delete tratamiento',93,'delete_tratamiento'),(280,'Can add disponibilidad',94,'add_disponibilidad'),(281,'Can change disponibilidad',94,'change_disponibilidad'),(282,'Can delete disponibilidad',94,'delete_disponibilidad'),(283,'Can add agua',95,'add_agua'),(284,'Can change agua',95,'change_agua'),(285,'Can delete agua',95,'delete_agua');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'crocha','','','carlos@simas.org.ni','sha1$e2895$83b1523edc051a113144063c471848f5f00f3a84',1,1,1,'2010-11-22 14:02:23','2010-11-18 14:10:59'),(2,'digitador','','','','sha1$74b45$fa433ff63efac9adf4267ba4ce816db14a9d7f6e',1,1,0,'2010-11-18 20:55:10','2010-11-18 20:54:47'),(3,'unag','','','','sha1$ff052$b7970eec70d967135abdf9d438f20ae032bc1aa3',1,1,0,'2010-11-18 20:58:01','2010-11-18 20:57:41');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_403f60f` (`user_id`),
  KEY `auth_user_groups_425ae3c4` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,3,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_403f60f` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_403f60f` (`user_id`),
  KEY `django_admin_log_1bb8f392` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2010-11-18 20:54:18',1,4,'1','zonas',1,''),(2,'2010-11-18 20:54:47',1,5,'2','digitador',1,''),(3,'2010-11-18 20:55:00',1,5,'2','digitador',2,'Modificado/a is_staff y groups.'),(4,'2010-11-18 20:55:52',2,15,'1','Carlos Rocha',1,''),(5,'2010-11-18 20:56:20',2,13,'1','grande',1,''),(6,'2010-11-18 20:56:36',2,16,'1','Metaleros',1,''),(7,'2010-11-18 20:56:48',2,17,'1','jose peroes',1,''),(8,'2010-11-18 20:57:41',1,5,'3','unag',1,''),(9,'2010-11-18 20:57:50',1,5,'3','unag',2,'Modificado/a is_staff y groups.'),(10,'2010-11-18 20:58:52',3,16,'2','personal',1,''),(11,'2010-11-18 20:58:59',3,17,'2','yelba alfaro',1,''),(12,'2010-11-22 14:21:24',1,60,'1','nada',1,''),(13,'2010-11-22 14:21:55',1,17,'2','yelba alfaro',2,'Añadido/a \"Hombre mas de 18 años\" educacion. Añadido/a \"Mujeres mas de 18 años\" educacion. Añadido/a \"Hombre de 7 a 18 años\" educacion. Añadido/a \"Mujeres de 7 a 18 años\" educacion. Añadido/a \"Niños menos de 6 años\" educacion. Añadido/a \"Niñas menos de 6 años\" educacion. Añadido/a \"Hombre mas de 18 años\" salud. Añadido/a \"Mujeres mas de 18 años\" salud. Añadido/a \"Hombre de 7 a 18 años\" salud. Añadido/a \"Mujeres de 7 a 18 años\" salud. Añadido/a \"Niños menos de 6 años\" salud. Añadido/a \"Niñas menos de 6 años\" salud. Añadido/a \"Energia object\" energia. Añadido/a \"Energia object\" energia. Añadido/a \"Energia object\" energia. Añadido/a \"Energia object\" energia. Añadido/a \"Energia object\" energia. Añadido/a \"Cocina object\" cocina. Añadido/a \"Agua object\" agua. Añadido/a \"OrganizacionGremial object\" organizacion gremial. Añadido/a \"OrganizacionComunitaria object\" organizacion comunitaria. Añadido/a \"Propia con escritura pública\" tenencia. Añadido/a \"Área total\" uso tierra. Añadido/a \"Bosque\" uso tierra. Añadido/a \"Tacotales\" uso tierra. Añadido/a \"Cultivos anuales\" uso tierra. Añadido/a \"Plantaciones forestal\" uso tierra. Añadido/a \"Áreas de pasto abierto\" uso tierra. Añadido/a \"Áreas de pastos con árboles\" uso tierra. Añadido/a \"Cultivos perennes\" uso tierra. Añadido/a \"ExistenciaArboles object\" existencia arboles. Añadido/a \"Enriquecimiento de los bosques\" reforestacion. Añadido/a \"Establecimiento de cercas viva\" reforestacion. Añadido/a \"Siembra de árboles en potrero\" reforestacion. Añadido/a \"Parcelas frutales\" reforestacion. Añadido/a \"Vacas paridas\" animales finca. Añadido/a \"Vacas horras\" animales finca. Añadido/a \"Toros\" animales finca. Añadido/a \"Aguacate\" cultivos finca. Añadido/a \"Ajonjolí\" cultivos finca. Añadido/a \"Cacao\" cultivos finca. Añadido/a \"Biofertilizantes\" opciones manejo. Añadido/a \"Estiercoleras\" opciones manejo. Añadido/a \"Fungicida natural\" opciones manejo. Añadido/a \"Suelo object\" suelo. Añadido/a \"ManejoSuelo object\" manejo suelo. Añadido/a \"Ajonjolí\" ingreso familiar. Añadido/a \"Aves\" ingreso familiar. Añadido/a \"Salarios\" otros ingresos. Añadido/a \"Madera rolliza\" tipo casa. Añadido/a \"12\" detalle casa. Añadido/a \"Bomba de fumigar\" propiedades. Añadido/a \"Celular\" propiedades. Añadido/a \"Biodigestor\" propiedades. Añadido/a \"Coba\" herramientas. Añadido/a \"Piocha\" herramientas. Añadido/a \"Rastrillo\" herramientas. Añadido/a \"Carreta de bueyes o caballos\" transporte. Añadido/a \"Bicicleta\" transporte. Añadido/a \"Motocicleta\" transporte. Añadido/a \"¿Tiene ahorro en joyeria/prendas?\" ahorro. Añadido/a \"Si\" credito. Añadido/a \"Aceite\" seguridad. Añadido/a \"Avena\" seguridad. Añadido/a \"Vulnerable object\" vulnerable. Añadido/a \"Vulnerable object\" vulnerable. Añadido/a \"Riesgos object\" riesgos. Añadido/a \"Riesgos object\" riesgos.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'bookmark','menu','bookmark'),(2,'dashboard preferences','dashboard','dashboardpreferences'),(3,'permission','auth','permission'),(4,'group','auth','group'),(5,'user','auth','user'),(6,'message','auth','message'),(7,'content type','contenttypes','contenttype'),(8,'session','sessions','session'),(9,'site','sites','site'),(10,'log entry','admin','logentry'),(11,'departamento','lugar','departamento'),(12,'municipio','lugar','municipio'),(13,'comunidad','lugar','comunidad'),(14,'migration history','south','migrationhistory'),(15,'recolector','simas','recolector'),(16,'organizaciones','simas','organizaciones'),(17,'encuesta','simas','encuesta'),(18,'tenencia','simas','tenencia'),(19,'org gremiales','indicador02','orggremiales'),(20,'beneficios obtenido','indicador02','beneficiosobtenido'),(21,'ser miembro','indicador02','sermiembro'),(22,'organizacion gremial','indicador02','organizaciongremial'),(23,'org comunitarias','indicador02','orgcomunitarias'),(24,'beneficio org comunitaria','indicador02','beneficioorgcomunitaria'),(25,'no organizado','indicador02','noorganizado'),(26,'organizacion comunitaria','indicador02','organizacioncomunitaria'),(27,'uso','indicador05','uso'),(28,'uso tierra','indicador05','usotierra'),(29,'maderable','indicador06','maderable'),(30,'forrajero','indicador06','forrajero'),(31,'energetico','indicador06','energetico'),(32,'frutal','indicador06','frutal'),(33,'existencia arboles','indicador06','existenciaarboles'),(34,'actividad','indicador07','actividad'),(35,'reforestacion','indicador07','reforestacion'),(36,'animales','indicador08','animales'),(37,'producto animal','indicador08','productoanimal'),(38,'animales finca','indicador08','animalesfinca'),(39,'cultivos','indicador09','cultivos'),(40,'cultivos finca','indicador09','cultivosfinca'),(41,'manejo agro','indicador10','manejoagro'),(42,'opciones manejo','indicador10','opcionesmanejo'),(43,'cultivos variedad','indicador11','cultivosvariedad'),(44,'variedades','indicador11','variedades'),(45,'semilla','indicador11','semilla'),(46,'textura','indicador12','textura'),(47,'profundidad','indicador12','profundidad'),(48,'densidad','indicador12','densidad'),(49,'pendiente','indicador12','pendiente'),(50,'drenaje','indicador12','drenaje'),(51,'suelo','indicador12','suelo'),(52,'preparar','indicador12','preparar'),(53,'traccion','indicador12','traccion'),(54,'fertilizacion','indicador12','fertilizacion'),(55,'conservacion','indicador12','conservacion'),(56,'manejo suelo','indicador12','manejosuelo'),(57,'rubros','indicador13','rubros'),(58,'ingreso familiar','indicador13','ingresofamiliar'),(59,'fuentes','indicador14','fuentes'),(60,'tipo trabajo','indicador14','tipotrabajo'),(61,'otros ingresos','indicador14','otrosingresos'),(62,'piso','indicador15','piso'),(63,'techo','indicador15','techo'),(64,'tipo casa','indicador15','tipocasa'),(65,'detalle casa','indicador15','detallecasa'),(66,'equipos','indicador15','equipos'),(67,'infraestructuras','indicador15','infraestructuras'),(68,'propiedades','indicador15','propiedades'),(69,'nombre herramienta','indicador15','nombreherramienta'),(70,'herramientas','indicador15','herramientas'),(71,'nombre transporte','indicador15','nombretransporte'),(72,'transporte','indicador15','transporte'),(73,'ahorro pregunta','indicador16','ahorropregunta'),(74,'ahorro','indicador16','ahorro'),(75,'da credito','indicador17','dacredito'),(76,'ocupa credito','indicador17','ocupacredito'),(77,'credito','indicador17','credito'),(78,'alimentos','indicador18','alimentos'),(79,'seguridad','indicador18','seguridad'),(80,'causa','indicador19','causa'),(81,'fenomeno','indicador19','fenomeno'),(82,'graves','indicador19','graves'),(83,'vulnerable','indicador19','vulnerable'),(84,'pregunta riesgo','indicador20','preguntariesgo'),(85,'riesgos','indicador20','riesgos'),(86,'educacion','indicador01','educacion'),(87,'salud','indicador01','salud'),(88,'pregunta energia','indicador01','preguntaenergia'),(89,'energia','indicador01','energia'),(90,'tipo cocina','indicador01','tipococina'),(91,'cocina','indicador01','cocina'),(92,'fuente','indicador01','fuente'),(93,'tratamiento','indicador01','tratamiento'),(94,'disponibilidad','indicador01','disponibilidad'),(95,'agua','indicador01','agua');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ef598858e160f583ad75fb2404ebfa0f','gAJ9cQEoVQZkdWVuaW9xAlgAAAAAVQ1fYXV0aF91c2VyX2lkcQOKAQFVCWNvbXVuaWRhZHEETlUF\nZmVjaGFxBVgEAAAAMjAxMHEGVQxkZXBhcnRhbWVudG9xB05VDG9yZ2FuaXphY2lvbnEITlUGYWN0\naXZvcQmIVQVzb2Npb3EKWAAAAABVEl9hdXRoX3VzZXJfYmFja2VuZHELVSlkamFuZ28uY29udHJp\nYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEMVQVkZXNkZXENWAAAAABVCW11bmljaXBpb3EO\nTnUuNmM5NDJkZWEwYzQzZmIzMTBhNmQyNDFjMjczZjRjOTY=\n','2010-12-06 11:51:21'),('c094eeff5bdf695bcb129c9b34182f70','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS41MmRiMWNjYmY0N2QwZjc1NDAz\nNTUwMTVmYjUxMjAwZA==\n','2010-12-06 14:02:23');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_agua`
--

DROP TABLE IF EXISTS `indicador01_agua`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_agua` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador01_agua_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_agua`
--

LOCK TABLES `indicador01_agua` WRITE;
/*!40000 ALTER TABLE `indicador01_agua` DISABLE KEYS */;
INSERT INTO `indicador01_agua` VALUES (1,2);
/*!40000 ALTER TABLE `indicador01_agua` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_agua_disponible`
--

DROP TABLE IF EXISTS `indicador01_agua_disponible`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_agua_disponible` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agua_id` int(11) NOT NULL,
  `disponibilidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador01_agua_disponible_agua_id_12fb8923_uniq` (`agua_id`,`disponibilidad_id`),
  KEY `indicador01_agua_disponible_6f428616` (`agua_id`),
  KEY `indicador01_agua_disponible_3ac6f1ed` (`disponibilidad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_agua_disponible`
--

LOCK TABLES `indicador01_agua_disponible` WRITE;
/*!40000 ALTER TABLE `indicador01_agua_disponible` DISABLE KEYS */;
INSERT INTO `indicador01_agua_disponible` VALUES (1,1,2);
/*!40000 ALTER TABLE `indicador01_agua_disponible` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_agua_fuente`
--

DROP TABLE IF EXISTS `indicador01_agua_fuente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_agua_fuente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agua_id` int(11) NOT NULL,
  `fuente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador01_agua_fuente_agua_id_4a8fe7f_uniq` (`agua_id`,`fuente_id`),
  KEY `indicador01_agua_fuente_6f428616` (`agua_id`),
  KEY `indicador01_agua_fuente_7592e3f3` (`fuente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_agua_fuente`
--

LOCK TABLES `indicador01_agua_fuente` WRITE;
/*!40000 ALTER TABLE `indicador01_agua_fuente` DISABLE KEYS */;
INSERT INTO `indicador01_agua_fuente` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `indicador01_agua_fuente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_agua_trata`
--

DROP TABLE IF EXISTS `indicador01_agua_trata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_agua_trata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `agua_id` int(11) NOT NULL,
  `tratamiento_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador01_agua_trata_agua_id_4f830ad3_uniq` (`agua_id`,`tratamiento_id`),
  KEY `indicador01_agua_trata_6f428616` (`agua_id`),
  KEY `indicador01_agua_trata_1bbf3ef3` (`tratamiento_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_agua_trata`
--

LOCK TABLES `indicador01_agua_trata` WRITE;
/*!40000 ALTER TABLE `indicador01_agua_trata` DISABLE KEYS */;
INSERT INTO `indicador01_agua_trata` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador01_agua_trata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_cocina`
--

DROP TABLE IF EXISTS `indicador01_cocina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_cocina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador01_cocina_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_cocina`
--

LOCK TABLES `indicador01_cocina` WRITE;
/*!40000 ALTER TABLE `indicador01_cocina` DISABLE KEYS */;
INSERT INTO `indicador01_cocina` VALUES (1,2);
/*!40000 ALTER TABLE `indicador01_cocina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_cocina_utiliza`
--

DROP TABLE IF EXISTS `indicador01_cocina_utiliza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_cocina_utiliza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cocina_id` int(11) NOT NULL,
  `tipococina_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador01_cocina_utiliza_cocina_id_78fe43d7_uniq` (`cocina_id`,`tipococina_id`),
  KEY `indicador01_cocina_utiliza_2f8ff5bf` (`cocina_id`),
  KEY `indicador01_cocina_utiliza_62ec1db3` (`tipococina_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_cocina_utiliza`
--

LOCK TABLES `indicador01_cocina_utiliza` WRITE;
/*!40000 ALTER TABLE `indicador01_cocina_utiliza` DISABLE KEYS */;
INSERT INTO `indicador01_cocina_utiliza` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador01_cocina_utiliza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_disponibilidad`
--

DROP TABLE IF EXISTS `indicador01_disponibilidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_disponibilidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_disponibilidad`
--

LOCK TABLES `indicador01_disponibilidad` WRITE;
/*!40000 ALTER TABLE `indicador01_disponibilidad` DISABLE KEYS */;
INSERT INTO `indicador01_disponibilidad` VALUES (1,'Todos los dias y todas las horas'),(2,'Todos los dias algunas horas'),(3,'Algunos dias algunas horas'),(4,'No confiable');
/*!40000 ALTER TABLE `indicador01_disponibilidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_educacion`
--

DROP TABLE IF EXISTS `indicador01_educacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_educacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sexo` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  `no_leer` int(11) NOT NULL,
  `p_incompleta` int(11) NOT NULL,
  `p_completa` int(11) NOT NULL,
  `s_incompleta` int(11) NOT NULL,
  `bachiller` int(11) NOT NULL,
  `universitario` int(11) NOT NULL,
  `f_comunidad` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador01_educacion_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_educacion`
--

LOCK TABLES `indicador01_educacion` WRITE;
/*!40000 ALTER TABLE `indicador01_educacion` DISABLE KEYS */;
INSERT INTO `indicador01_educacion` VALUES (1,1,3,0,0,0,1,2,0,0,2),(2,2,1,0,0,0,0,0,1,1,2),(3,3,5,1,1,1,1,1,0,3,2),(4,4,2,0,0,0,0,2,0,0,2),(5,5,1,0,1,0,0,0,0,0,2),(6,6,1,1,0,0,0,0,0,0,2);
/*!40000 ALTER TABLE `indicador01_educacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_energia`
--

DROP TABLE IF EXISTS `indicador01_energia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_energia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta_id` int(11) NOT NULL,
  `respuesta` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador01_energia_37c55af2` (`pregunta_id`),
  KEY `indicador01_energia_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_energia`
--

LOCK TABLES `indicador01_energia` WRITE;
/*!40000 ALTER TABLE `indicador01_energia` DISABLE KEYS */;
INSERT INTO `indicador01_energia` VALUES (1,1,1,2),(2,2,2,2),(3,3,1,2),(4,4,2,2),(5,5,2,2);
/*!40000 ALTER TABLE `indicador01_energia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_fuente`
--

DROP TABLE IF EXISTS `indicador01_fuente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_fuente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_fuente`
--

LOCK TABLES `indicador01_fuente` WRITE;
/*!40000 ALTER TABLE `indicador01_fuente` DISABLE KEYS */;
INSERT INTO `indicador01_fuente` VALUES (1,'Río'),(2,'Ojo de agua'),(3,'Quebrada'),(4,'Pozo comunitario'),(5,'Pozo propio'),(6,'Agua entubada');
/*!40000 ALTER TABLE `indicador01_fuente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_preguntaenergia`
--

DROP TABLE IF EXISTS `indicador01_preguntaenergia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_preguntaenergia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_preguntaenergia`
--

LOCK TABLES `indicador01_preguntaenergia` WRITE;
/*!40000 ALTER TABLE `indicador01_preguntaenergia` DISABLE KEYS */;
INSERT INTO `indicador01_preguntaenergia` VALUES (1,'¿Tiene luz eléctrica?'),(2,'¿Tiene medidor de luz?'),(3,'¿Tiene panel solar?'),(4,'¿Tiene planta eléctrica?'),(5,'¿Usa lámpara kerosene?');
/*!40000 ALTER TABLE `indicador01_preguntaenergia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_salud`
--

DROP TABLE IF EXISTS `indicador01_salud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_salud` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sexo` int(11) NOT NULL,
  `b_salud` int(11) NOT NULL,
  `s_delicada` int(11) NOT NULL,
  `e_cronica` int(11) NOT NULL,
  `v_centro` int(11) NOT NULL,
  `v_medico` int(11) NOT NULL,
  `v_naturista` int(11) NOT NULL,
  `automedica` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador01_salud_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_salud`
--

LOCK TABLES `indicador01_salud` WRITE;
/*!40000 ALTER TABLE `indicador01_salud` DISABLE KEYS */;
INSERT INTO `indicador01_salud` VALUES (1,1,3,0,0,1,2,1,2,2),(2,2,1,0,0,1,1,1,1,2),(3,3,3,2,0,2,2,2,2,2),(4,4,1,1,0,1,2,2,1,2),(5,5,1,0,0,1,1,1,1,2),(6,6,1,0,0,2,2,2,2,2);
/*!40000 ALTER TABLE `indicador01_salud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_tipococina`
--

DROP TABLE IF EXISTS `indicador01_tipococina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_tipococina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_tipococina`
--

LOCK TABLES `indicador01_tipococina` WRITE;
/*!40000 ALTER TABLE `indicador01_tipococina` DISABLE KEYS */;
INSERT INTO `indicador01_tipococina` VALUES (1,'Gas'),(2,'Leña'),(3,'Carbón');
/*!40000 ALTER TABLE `indicador01_tipococina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador01_tratamiento`
--

DROP TABLE IF EXISTS `indicador01_tratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador01_tratamiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador01_tratamiento`
--

LOCK TABLES `indicador01_tratamiento` WRITE;
/*!40000 ALTER TABLE `indicador01_tratamiento` DISABLE KEYS */;
INSERT INTO `indicador01_tratamiento` VALUES (1,'No trata el agua'),(2,'Hierbe el agua'),(3,'Clora el agua'),(4,'Usa filtro de agua');
/*!40000 ALTER TABLE `indicador01_tratamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_beneficioorgcomunitaria`
--

DROP TABLE IF EXISTS `indicador02_beneficioorgcomunitaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_beneficioorgcomunitaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_beneficioorgcomunitaria`
--

LOCK TABLES `indicador02_beneficioorgcomunitaria` WRITE;
/*!40000 ALTER TABLE `indicador02_beneficioorgcomunitaria` DISABLE KEYS */;
INSERT INTO `indicador02_beneficioorgcomunitaria` VALUES (1,'Para aportar el desarrollo de comunidad'),(2,'Para recibir benficios de salud'),(3,'Para recibir mejores servicios'),(4,'Para mejorar la participación de las mujeres y jóvenes');
/*!40000 ALTER TABLE `indicador02_beneficioorgcomunitaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_beneficiosobtenido`
--

DROP TABLE IF EXISTS `indicador02_beneficiosobtenido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_beneficiosobtenido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_beneficiosobtenido`
--

LOCK TABLES `indicador02_beneficiosobtenido` WRITE;
/*!40000 ALTER TABLE `indicador02_beneficiosobtenido` DISABLE KEYS */;
INSERT INTO `indicador02_beneficiosobtenido` VALUES (1,'Obtener crédito para la producción'),(2,'Suministro de semilla'),(3,'Tener servicio de asistencia técnica'),(4,'Tener servicio de capacitaciones'),(5,'Fondos para retención de cosecha'),(6,'Comercializar mejor y obtener mejor precio'),(7,'Obtener mejores beneficios familiares'),(8,'Proyectos sociales'),(9,'Proyectos productivos');
/*!40000 ALTER TABLE `indicador02_beneficiosobtenido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_noorganizado`
--

DROP TABLE IF EXISTS `indicador02_noorganizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_noorganizado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_noorganizado`
--

LOCK TABLES `indicador02_noorganizado` WRITE;
/*!40000 ALTER TABLE `indicador02_noorganizado` DISABLE KEYS */;
INSERT INTO `indicador02_noorganizado` VALUES (1,'Pérdida de tiempo'),(2,'Hay corrupción'),(3,'Hay amiguismo');
/*!40000 ALTER TABLE `indicador02_noorganizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizacioncomunitaria`
--

DROP TABLE IF EXISTS `indicador02_organizacioncomunitaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizacioncomunitaria` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero` int(11) NOT NULL,
  `pertence` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador02_organizacioncomunitaria_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizacioncomunitaria`
--

LOCK TABLES `indicador02_organizacioncomunitaria` WRITE;
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria` DISABLE KEYS */;
INSERT INTO `indicador02_organizacioncomunitaria` VALUES (1,12,1,2);
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizacioncomunitaria_cual_beneficio`
--

DROP TABLE IF EXISTS `indicador02_organizacioncomunitaria_cual_beneficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizacioncomunitaria_cual_beneficio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacioncomunitaria_id` int(11) NOT NULL,
  `beneficioorgcomunitaria_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaci_organizacioncomunitaria_id_2ec80c0b_uniq` (`organizacioncomunitaria_id`,`beneficioorgcomunitaria_id`),
  KEY `indicador02_organizacioncomunitaria_cual_beneficio_3dcc15c7` (`organizacioncomunitaria_id`),
  KEY `indicador02_organizacioncomunitaria_cual_beneficio_454bee27` (`beneficioorgcomunitaria_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizacioncomunitaria_cual_beneficio`
--

LOCK TABLES `indicador02_organizacioncomunitaria_cual_beneficio` WRITE;
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_cual_beneficio` DISABLE KEYS */;
INSERT INTO `indicador02_organizacioncomunitaria_cual_beneficio` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_cual_beneficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizacioncomunitaria_cual_organizacion`
--

DROP TABLE IF EXISTS `indicador02_organizacioncomunitaria_cual_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizacioncomunitaria_cual_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacioncomunitaria_id` int(11) NOT NULL,
  `orgcomunitarias_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaci_organizacioncomunitaria_id_17362d57_uniq` (`organizacioncomunitaria_id`,`orgcomunitarias_id`),
  KEY `indicador02_organizacioncomunitaria_cual_organizacion_3dcc15c7` (`organizacioncomunitaria_id`),
  KEY `indicador02_organizacioncomunitaria_cual_organizacion_366ed468` (`orgcomunitarias_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizacioncomunitaria_cual_organizacion`
--

LOCK TABLES `indicador02_organizacioncomunitaria_cual_organizacion` WRITE;
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_cual_organizacion` DISABLE KEYS */;
INSERT INTO `indicador02_organizacioncomunitaria_cual_organizacion` VALUES (1,1,1),(2,1,4);
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_cual_organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizacioncomunitaria_no_organizado`
--

DROP TABLE IF EXISTS `indicador02_organizacioncomunitaria_no_organizado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizacioncomunitaria_no_organizado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacioncomunitaria_id` int(11) NOT NULL,
  `noorganizado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaci_organizacioncomunitaria_id_78e0868c_uniq` (`organizacioncomunitaria_id`,`noorganizado_id`),
  KEY `indicador02_organizacioncomunitaria_no_organizado_3dcc15c7` (`organizacioncomunitaria_id`),
  KEY `indicador02_organizacioncomunitaria_no_organizado_2a98a899` (`noorganizado_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizacioncomunitaria_no_organizado`
--

LOCK TABLES `indicador02_organizacioncomunitaria_no_organizado` WRITE;
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_no_organizado` DISABLE KEYS */;
INSERT INTO `indicador02_organizacioncomunitaria_no_organizado` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador02_organizacioncomunitaria_no_organizado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizaciongremial`
--

DROP TABLE IF EXISTS `indicador02_organizaciongremial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizaciongremial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desde_socio` int(11) NOT NULL,
  `miembro_gremial` int(11) NOT NULL,
  `desde_miembro` int(11) NOT NULL,
  `capacitacion` int(11) NOT NULL,
  `desde_capacitacion` int(11) NOT NULL,
  `asumir_cargo` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador02_organizaciongremial_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizaciongremial`
--

LOCK TABLES `indicador02_organizaciongremial` WRITE;
/*!40000 ALTER TABLE `indicador02_organizaciongremial` DISABLE KEYS */;
INSERT INTO `indicador02_organizaciongremial` VALUES (1,1,1,2,2,3,1,2);
/*!40000 ALTER TABLE `indicador02_organizaciongremial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizaciongremial_beneficio`
--

DROP TABLE IF EXISTS `indicador02_organizaciongremial_beneficio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizaciongremial_beneficio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizaciongremial_id` int(11) NOT NULL,
  `beneficiosobtenido_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaciongre_organizaciongremial_id_d7fcb4a_uniq` (`organizaciongremial_id`,`beneficiosobtenido_id`),
  KEY `indicador02_organizaciongremial_beneficio_24996942` (`organizaciongremial_id`),
  KEY `indicador02_organizaciongremial_beneficio_71594ca7` (`beneficiosobtenido_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizaciongremial_beneficio`
--

LOCK TABLES `indicador02_organizaciongremial_beneficio` WRITE;
/*!40000 ALTER TABLE `indicador02_organizaciongremial_beneficio` DISABLE KEYS */;
INSERT INTO `indicador02_organizaciongremial_beneficio` VALUES (1,1,2),(2,1,6);
/*!40000 ALTER TABLE `indicador02_organizaciongremial_beneficio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizaciongremial_miembro_junta`
--

DROP TABLE IF EXISTS `indicador02_organizaciongremial_miembro_junta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizaciongremial_miembro_junta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizaciongremial_id` int(11) NOT NULL,
  `sermiembro_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaciongr_organizaciongremial_id_6b6c4272_uniq` (`organizaciongremial_id`,`sermiembro_id`),
  KEY `indicador02_organizaciongremial_miembro_junta_24996942` (`organizaciongremial_id`),
  KEY `indicador02_organizaciongremial_miembro_junta_795c7415` (`sermiembro_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizaciongremial_miembro_junta`
--

LOCK TABLES `indicador02_organizaciongremial_miembro_junta` WRITE;
/*!40000 ALTER TABLE `indicador02_organizaciongremial_miembro_junta` DISABLE KEYS */;
INSERT INTO `indicador02_organizaciongremial_miembro_junta` VALUES (1,1,1),(2,1,2),(3,1,4);
/*!40000 ALTER TABLE `indicador02_organizaciongremial_miembro_junta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_organizaciongremial_socio`
--

DROP TABLE IF EXISTS `indicador02_organizaciongremial_socio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_organizaciongremial_socio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizaciongremial_id` int(11) NOT NULL,
  `orggremiales_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador02_organizaciongr_organizaciongremial_id_4f9c5ee5_uniq` (`organizaciongremial_id`,`orggremiales_id`),
  KEY `indicador02_organizaciongremial_socio_24996942` (`organizaciongremial_id`),
  KEY `indicador02_organizaciongremial_socio_7bafd1b3` (`orggremiales_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_organizaciongremial_socio`
--

LOCK TABLES `indicador02_organizaciongremial_socio` WRITE;
/*!40000 ALTER TABLE `indicador02_organizaciongremial_socio` DISABLE KEYS */;
INSERT INTO `indicador02_organizaciongremial_socio` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador02_organizaciongremial_socio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_orgcomunitarias`
--

DROP TABLE IF EXISTS `indicador02_orgcomunitarias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_orgcomunitarias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_orgcomunitarias`
--

LOCK TABLES `indicador02_orgcomunitarias` WRITE;
/*!40000 ALTER TABLE `indicador02_orgcomunitarias` DISABLE KEYS */;
INSERT INTO `indicador02_orgcomunitarias` VALUES (1,'Comite de agua potable y saneamiento CAPS'),(2,'Comité de salud'),(3,'Asociación de padres de familia'),(4,'Asociación de iglesia'),(5,'CPC'),(6,'Movimiento de mujeres');
/*!40000 ALTER TABLE `indicador02_orgcomunitarias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_orggremiales`
--

DROP TABLE IF EXISTS `indicador02_orggremiales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_orggremiales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_orggremiales`
--

LOCK TABLES `indicador02_orggremiales` WRITE;
/*!40000 ALTER TABLE `indicador02_orggremiales` DISABLE KEYS */;
INSERT INTO `indicador02_orggremiales` VALUES (1,'Cooperativa'),(2,'Asociación'),(3,'Empresa'),(4,'Grupo'),(5,'Ninguno');
/*!40000 ALTER TABLE `indicador02_orggremiales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador02_sermiembro`
--

DROP TABLE IF EXISTS `indicador02_sermiembro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador02_sermiembro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador02_sermiembro`
--

LOCK TABLES `indicador02_sermiembro` WRITE;
/*!40000 ALTER TABLE `indicador02_sermiembro` DISABLE KEYS */;
INSERT INTO `indicador02_sermiembro` VALUES (1,'Para apoyar a las organizaciones'),(2,'Para asegurar que todo marche bien'),(3,'Para asegurar la participación de la mujeres'),(4,'Para defender derecho de las mujeres y jóvenes');
/*!40000 ALTER TABLE `indicador02_sermiembro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador05_uso`
--

DROP TABLE IF EXISTS `indicador05_uso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador05_uso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador05_uso`
--

LOCK TABLES `indicador05_uso` WRITE;
/*!40000 ALTER TABLE `indicador05_uso` DISABLE KEYS */;
INSERT INTO `indicador05_uso` VALUES (1,'Área total'),(2,'Bosque'),(3,'Tacotales'),(4,'Cultivos anuales'),(5,'Plantaciones forestal'),(6,'Áreas de pasto abierto'),(7,'Áreas de pastos con árboles'),(8,'Cultivos perennes');
/*!40000 ALTER TABLE `indicador05_uso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador05_usotierra`
--

DROP TABLE IF EXISTS `indicador05_usotierra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador05_usotierra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tierra_id` int(11) NOT NULL,
  `area` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador05_usotierra_2483c647` (`tierra_id`),
  KEY `indicador05_usotierra_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador05_usotierra`
--

LOCK TABLES `indicador05_usotierra` WRITE;
/*!40000 ALTER TABLE `indicador05_usotierra` DISABLE KEYS */;
INSERT INTO `indicador05_usotierra` VALUES (1,1,20,2),(2,2,1,2),(3,3,1,2),(4,4,2,2),(5,5,1,2),(6,6,5,2),(7,7,5,2),(8,8,5,2);
/*!40000 ALTER TABLE `indicador05_usotierra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_energetico`
--

DROP TABLE IF EXISTS `indicador06_energetico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_energetico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_energetico`
--

LOCK TABLES `indicador06_energetico` WRITE;
/*!40000 ALTER TABLE `indicador06_energetico` DISABLE KEYS */;
INSERT INTO `indicador06_energetico` VALUES (1,'neem'),(2,'quebracho'),(3,'carao'),(4,'tiguilote'),(5,'guanacaste blanco'),(6,'miliguiste'),(7,'eucalipto');
/*!40000 ALTER TABLE `indicador06_energetico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_existenciaarboles`
--

DROP TABLE IF EXISTS `indicador06_existenciaarboles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_existenciaarboles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cantidad_maderable` int(11) NOT NULL,
  `cantidad_forrajero` int(11) NOT NULL,
  `cantidad_energetico` int(11) NOT NULL,
  `cantidad_frutal` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador06_existenciaarboles_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_existenciaarboles`
--

LOCK TABLES `indicador06_existenciaarboles` WRITE;
/*!40000 ALTER TABLE `indicador06_existenciaarboles` DISABLE KEYS */;
INSERT INTO `indicador06_existenciaarboles` VALUES (1,23,2,23,12,2);
/*!40000 ALTER TABLE `indicador06_existenciaarboles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_existenciaarboles_energetico`
--

DROP TABLE IF EXISTS `indicador06_existenciaarboles_energetico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_existenciaarboles_energetico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `existenciaarboles_id` int(11) NOT NULL,
  `energetico_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador06_existenciaarbole_existenciaarboles_id_2fc7c3ac_uniq` (`existenciaarboles_id`,`energetico_id`),
  KEY `indicador06_existenciaarboles_energetico_134d880e` (`existenciaarboles_id`),
  KEY `indicador06_existenciaarboles_energetico_341a3373` (`energetico_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_existenciaarboles_energetico`
--

LOCK TABLES `indicador06_existenciaarboles_energetico` WRITE;
/*!40000 ALTER TABLE `indicador06_existenciaarboles_energetico` DISABLE KEYS */;
INSERT INTO `indicador06_existenciaarboles_energetico` VALUES (1,1,1),(2,1,3),(3,1,4);
/*!40000 ALTER TABLE `indicador06_existenciaarboles_energetico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_existenciaarboles_forrajero`
--

DROP TABLE IF EXISTS `indicador06_existenciaarboles_forrajero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_existenciaarboles_forrajero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `existenciaarboles_id` int(11) NOT NULL,
  `forrajero_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador06_existenciaarbole_existenciaarboles_id_7006ad5c_uniq` (`existenciaarboles_id`,`forrajero_id`),
  KEY `indicador06_existenciaarboles_forrajero_134d880e` (`existenciaarboles_id`),
  KEY `indicador06_existenciaarboles_forrajero_6b935d81` (`forrajero_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_existenciaarboles_forrajero`
--

LOCK TABLES `indicador06_existenciaarboles_forrajero` WRITE;
/*!40000 ALTER TABLE `indicador06_existenciaarboles_forrajero` DISABLE KEYS */;
INSERT INTO `indicador06_existenciaarboles_forrajero` VALUES (1,1,1),(2,1,4),(3,1,5);
/*!40000 ALTER TABLE `indicador06_existenciaarboles_forrajero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_existenciaarboles_frutal`
--

DROP TABLE IF EXISTS `indicador06_existenciaarboles_frutal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_existenciaarboles_frutal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `existenciaarboles_id` int(11) NOT NULL,
  `frutal_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador06_existenciaarbole_existenciaarboles_id_30a0eda8_uniq` (`existenciaarboles_id`,`frutal_id`),
  KEY `indicador06_existenciaarboles_frutal_134d880e` (`existenciaarboles_id`),
  KEY `indicador06_existenciaarboles_frutal_2c15f212` (`frutal_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_existenciaarboles_frutal`
--

LOCK TABLES `indicador06_existenciaarboles_frutal` WRITE;
/*!40000 ALTER TABLE `indicador06_existenciaarboles_frutal` DISABLE KEYS */;
INSERT INTO `indicador06_existenciaarboles_frutal` VALUES (1,1,8),(2,1,2),(3,1,6),(4,1,7);
/*!40000 ALTER TABLE `indicador06_existenciaarboles_frutal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_existenciaarboles_maderable`
--

DROP TABLE IF EXISTS `indicador06_existenciaarboles_maderable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_existenciaarboles_maderable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `existenciaarboles_id` int(11) NOT NULL,
  `maderable_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador06_existenciaarbole_existenciaarboles_id_295d0d20_uniq` (`existenciaarboles_id`,`maderable_id`),
  KEY `indicador06_existenciaarboles_maderable_134d880e` (`existenciaarboles_id`),
  KEY `indicador06_existenciaarboles_maderable_12e2f46` (`maderable_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_existenciaarboles_maderable`
--

LOCK TABLES `indicador06_existenciaarboles_maderable` WRITE;
/*!40000 ALTER TABLE `indicador06_existenciaarboles_maderable` DISABLE KEYS */;
INSERT INTO `indicador06_existenciaarboles_maderable` VALUES (1,1,1),(2,1,3),(3,1,6);
/*!40000 ALTER TABLE `indicador06_existenciaarboles_maderable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_forrajero`
--

DROP TABLE IF EXISTS `indicador06_forrajero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_forrajero` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_forrajero`
--

LOCK TABLES `indicador06_forrajero` WRITE;
/*!40000 ALTER TABLE `indicador06_forrajero` DISABLE KEYS */;
INSERT INTO `indicador06_forrajero` VALUES (1,'madero negro'),(2,'tiguilote'),(3,'acasia'),(4,'guasimo'),(5,'leucaena'),(6,'marango'),(7,'genizaro'),(8,'guanacaste');
/*!40000 ALTER TABLE `indicador06_forrajero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_frutal`
--

DROP TABLE IF EXISTS `indicador06_frutal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_frutal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_frutal`
--

LOCK TABLES `indicador06_frutal` WRITE;
/*!40000 ALTER TABLE `indicador06_frutal` DISABLE KEYS */;
INSERT INTO `indicador06_frutal` VALUES (1,'naranja'),(2,'mango'),(3,'marañon'),(4,'limón'),(5,'limón agrio'),(6,'aguacate'),(7,'mamón'),(8,'guayaba'),(9,'jocote'),(10,'zapote'),(11,'nispero'),(12,'tamarindo'),(13,'papaya');
/*!40000 ALTER TABLE `indicador06_frutal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador06_maderable`
--

DROP TABLE IF EXISTS `indicador06_maderable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador06_maderable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador06_maderable`
--

LOCK TABLES `indicador06_maderable` WRITE;
/*!40000 ALTER TABLE `indicador06_maderable` DISABLE KEYS */;
INSERT INTO `indicador06_maderable` VALUES (1,'teca'),(2,'cedro'),(3,'pochote'),(4,'laurel'),(5,'guanacaste'),(6,'genizaro'),(7,'roble'),(8,'pino'),(9,'melina'),(10,'caoba'),(11,'frijolillo');
/*!40000 ALTER TABLE `indicador06_maderable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador07_actividad`
--

DROP TABLE IF EXISTS `indicador07_actividad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador07_actividad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador07_actividad`
--

LOCK TABLES `indicador07_actividad` WRITE;
/*!40000 ALTER TABLE `indicador07_actividad` DISABLE KEYS */;
INSERT INTO `indicador07_actividad` VALUES (1,'Enriquecimiento de los bosques'),(2,'Protección de fuente de agua'),(3,'Establecimiento de cercas viva'),(4,'Plantaciones foretales'),(5,'Siembra de árboles en potrero'),(6,'Siembra de árboles en cafetales'),(7,'Establecimiento de viveros'),(8,'Parcelas frutales'),(9,'Huerto de patio');
/*!40000 ALTER TABLE `indicador07_actividad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador07_reforestacion`
--

DROP TABLE IF EXISTS `indicador07_reforestacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador07_reforestacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reforestacion_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador07_reforestacion_751e20c3` (`reforestacion_id`),
  KEY `indicador07_reforestacion_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador07_reforestacion`
--

LOCK TABLES `indicador07_reforestacion` WRITE;
/*!40000 ALTER TABLE `indicador07_reforestacion` DISABLE KEYS */;
INSERT INTO `indicador07_reforestacion` VALUES (1,1,12,2),(2,3,1,2),(3,5,23,2),(4,8,12,2);
/*!40000 ALTER TABLE `indicador07_reforestacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador08_animales`
--

DROP TABLE IF EXISTS `indicador08_animales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador08_animales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador08_animales`
--

LOCK TABLES `indicador08_animales` WRITE;
/*!40000 ALTER TABLE `indicador08_animales` DISABLE KEYS */;
INSERT INTO `indicador08_animales` VALUES (1,'Vacas paridas'),(2,'Vacas horras'),(3,'Vaquillas'),(4,'Ternero de desarrollo'),(5,'Novillo'),(6,'Toros'),(7,'Pelibuey'),(8,'Cerdos'),(9,'Aves de corral'),(10,'Colmenas'),(11,'Bueyes'),(12,'Bestias');
/*!40000 ALTER TABLE `indicador08_animales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador08_animalesfinca`
--

DROP TABLE IF EXISTS `indicador08_animalesfinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador08_animalesfinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `animales_id` int(11) NOT NULL,
  `cantidad` double NOT NULL,
  `produccion_id` int(11) NOT NULL,
  `total_produccion` int(11) DEFAULT NULL,
  `consumo` double NOT NULL,
  `venta_libre` double NOT NULL,
  `venta_organizada` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador08_animalesfinca_528f57b8` (`animales_id`),
  KEY `indicador08_animalesfinca_4153c39a` (`produccion_id`),
  KEY `indicador08_animalesfinca_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador08_animalesfinca`
--

LOCK TABLES `indicador08_animalesfinca` WRITE;
/*!40000 ALTER TABLE `indicador08_animalesfinca` DISABLE KEYS */;
INSERT INTO `indicador08_animalesfinca` VALUES (1,1,12,1,1,1,1,1,2),(2,2,2,2,1,23,3,34,2),(3,6,1,2,1,1,1,1,2);
/*!40000 ALTER TABLE `indicador08_animalesfinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador08_productoanimal`
--

DROP TABLE IF EXISTS `indicador08_productoanimal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador08_productoanimal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `unidad` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador08_productoanimal`
--

LOCK TABLES `indicador08_productoanimal` WRITE;
/*!40000 ALTER TABLE `indicador08_productoanimal` DISABLE KEYS */;
INSERT INTO `indicador08_productoanimal` VALUES (1,'Leche','Litro'),(2,'Carne de res','Cabeza'),(3,'carne pelibuey','Cabeza'),(4,'Huevo','Docena'),(5,'No tiene','No tiene');
/*!40000 ALTER TABLE `indicador08_productoanimal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador09_cultivos`
--

DROP TABLE IF EXISTS `indicador09_cultivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador09_cultivos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `unidad` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador09_cultivos`
--

LOCK TABLES `indicador09_cultivos` WRITE;
/*!40000 ALTER TABLE `indicador09_cultivos` DISABLE KEYS */;
INSERT INTO `indicador09_cultivos` VALUES (1,'Aguacate','Cien'),(2,'Ajonjolí','Quintales'),(3,'Arroz','Quintales'),(4,'Cacao','Quintales'),(5,'Café','Quintales'),(6,'Cebolla','Libras'),(7,'Chiltoma','Libras'),(8,'Frijol','Quintales'),(9,'Guineo','Cabeza'),(10,'Jocote','Lata'),(11,'Limón','Cien'),(12,'Maíz','Libras'),(13,'Malanga','Quintales'),(14,'Mango','Cien'),(15,'Millón','Quintales'),(16,'Naranja','Cien'),(17,'Pepino','Docena'),(18,'Plátano','Cabeza'),(19,'Quequisque','Quintales'),(20,'Sorgo','Quintales'),(21,'Tomate','Libras'),(22,'Yuca','Quintales');
/*!40000 ALTER TABLE `indicador09_cultivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador09_cultivosfinca`
--

DROP TABLE IF EXISTS `indicador09_cultivosfinca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador09_cultivosfinca` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivos_id` int(11) NOT NULL,
  `area` double NOT NULL,
  `total` double NOT NULL,
  `consumo` double NOT NULL,
  `venta_libre` double NOT NULL,
  `venta_organizada` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador09_cultivosfinca_168c2801` (`cultivos_id`),
  KEY `indicador09_cultivosfinca_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador09_cultivosfinca`
--

LOCK TABLES `indicador09_cultivosfinca` WRITE;
/*!40000 ALTER TABLE `indicador09_cultivosfinca` DISABLE KEYS */;
INSERT INTO `indicador09_cultivosfinca` VALUES (1,1,1,1,1,1,1,2),(2,2,1,1,1,1,1,2),(3,4,1,1,1,1,1,2);
/*!40000 ALTER TABLE `indicador09_cultivosfinca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador10_manejoagro`
--

DROP TABLE IF EXISTS `indicador10_manejoagro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador10_manejoagro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `unidad` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador10_manejoagro`
--

LOCK TABLES `indicador10_manejoagro` WRITE;
/*!40000 ALTER TABLE `indicador10_manejoagro` DISABLE KEYS */;
INSERT INTO `indicador10_manejoagro` VALUES (1,'Biofertilizantes','Litros'),(2,'Estiercoleras','Quintales'),(3,'Insecticida natural','Litros'),(4,'Fungicida natural','Litros'),(5,'Conservaciones de semilla','Libras'),(6,'Selección de semilla nativa','Libras'),(7,'Cerca viva','Varas'),(8,'Cortina rompe viento','varas'),(9,'Abonos verdes','Libras'),(10,'Curva a nivel','Varas'),(11,'Acequia','Varas'),(12,'Barrera viva','Varas'),(13,'Barrera muerta','Varas'),(14,'Cosecha de agua','Litros'),(15,'Cultivo asociado','Manzana'),(16,'Incorporación de rastrojo','Manzana');
/*!40000 ALTER TABLE `indicador10_manejoagro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador10_opcionesmanejo`
--

DROP TABLE IF EXISTS `indicador10_opcionesmanejo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador10_opcionesmanejo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uso_id` int(11) NOT NULL,
  `nivel` int(11) NOT NULL,
  `menor_escala` int(11) NOT NULL,
  `mayor_escala` int(11) NOT NULL,
  `volumen` double NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador10_opcionesmanejo_7b812cfc` (`uso_id`),
  KEY `indicador10_opcionesmanejo_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador10_opcionesmanejo`
--

LOCK TABLES `indicador10_opcionesmanejo` WRITE;
/*!40000 ALTER TABLE `indicador10_opcionesmanejo` DISABLE KEYS */;
INSERT INTO `indicador10_opcionesmanejo` VALUES (1,1,1,1,1,1,2),(2,2,2,1,1,1,2),(3,4,3,2,2,1,2);
/*!40000 ALTER TABLE `indicador10_opcionesmanejo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador11_cultivosvariedad`
--

DROP TABLE IF EXISTS `indicador11_cultivosvariedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador11_cultivosvariedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivo` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador11_cultivosvariedad`
--

LOCK TABLES `indicador11_cultivosvariedad` WRITE;
/*!40000 ALTER TABLE `indicador11_cultivosvariedad` DISABLE KEYS */;
INSERT INTO `indicador11_cultivosvariedad` VALUES (1,'Maíz'),(2,'Frijol'),(3,'Arroz'),(4,'Sorgo'),(5,'Yuca'),(6,'Quequisque'),(7,'Guineo'),(8,'Plátano'),(9,'Tomate'),(10,'Chiltoma'),(11,'Cebolla'),(12,'Malanga');
/*!40000 ALTER TABLE `indicador11_cultivosvariedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador11_semilla`
--

DROP TABLE IF EXISTS `indicador11_semilla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador11_semilla` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivo_id` int(11) NOT NULL,
  `origen` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador11_semilla_60687df5` (`cultivo_id`),
  KEY `indicador11_semilla_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador11_semilla`
--

LOCK TABLES `indicador11_semilla` WRITE;
/*!40000 ALTER TABLE `indicador11_semilla` DISABLE KEYS */;
/*!40000 ALTER TABLE `indicador11_semilla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador11_variedades`
--

DROP TABLE IF EXISTS `indicador11_variedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador11_variedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cultivo_id` int(11) NOT NULL,
  `variedad` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador11_variedades_60687df5` (`cultivo_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador11_variedades`
--

LOCK TABLES `indicador11_variedades` WRITE;
/*!40000 ALTER TABLE `indicador11_variedades` DISABLE KEYS */;
/*!40000 ALTER TABLE `indicador11_variedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_conservacion`
--

DROP TABLE IF EXISTS `indicador12_conservacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_conservacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_conservacion`
--

LOCK TABLES `indicador12_conservacion` WRITE;
/*!40000 ALTER TABLE `indicador12_conservacion` DISABLE KEYS */;
INSERT INTO `indicador12_conservacion` VALUES (1,'Barrera viva'),(2,'Barrera muerta'),(3,'Terraza'),(4,'Acequia'),(5,'Curva a nivel');
/*!40000 ALTER TABLE `indicador12_conservacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_densidad`
--

DROP TABLE IF EXISTS `indicador12_densidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_densidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_densidad`
--

LOCK TABLES `indicador12_densidad` WRITE;
/*!40000 ALTER TABLE `indicador12_densidad` DISABLE KEYS */;
INSERT INTO `indicador12_densidad` VALUES (1,'Alta'),(2,'Media'),(3,'Baja');
/*!40000 ALTER TABLE `indicador12_densidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_drenaje`
--

DROP TABLE IF EXISTS `indicador12_drenaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_drenaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_drenaje`
--

LOCK TABLES `indicador12_drenaje` WRITE;
/*!40000 ALTER TABLE `indicador12_drenaje` DISABLE KEYS */;
INSERT INTO `indicador12_drenaje` VALUES (1,'Bueno'),(2,'Regular'),(3,'Malo');
/*!40000 ALTER TABLE `indicador12_drenaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_fertilizacion`
--

DROP TABLE IF EXISTS `indicador12_fertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_fertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_fertilizacion`
--

LOCK TABLES `indicador12_fertilizacion` WRITE;
/*!40000 ALTER TABLE `indicador12_fertilizacion` DISABLE KEYS */;
INSERT INTO `indicador12_fertilizacion` VALUES (1,'Química'),(2,'Orgánica'),(3,'Ninguna');
/*!40000 ALTER TABLE `indicador12_fertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_manejosuelo`
--

DROP TABLE IF EXISTS `indicador12_manejosuelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_manejosuelo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `analisis` int(11) NOT NULL,
  `practica` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador12_manejosuelo_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_manejosuelo`
--

LOCK TABLES `indicador12_manejosuelo` WRITE;
/*!40000 ALTER TABLE `indicador12_manejosuelo` DISABLE KEYS */;
INSERT INTO `indicador12_manejosuelo` VALUES (1,1,1,2);
/*!40000 ALTER TABLE `indicador12_manejosuelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_manejosuelo_fertilizacion`
--

DROP TABLE IF EXISTS `indicador12_manejosuelo_fertilizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_manejosuelo_fertilizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejosuelo_id` int(11) NOT NULL,
  `fertilizacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_manejosuelo_fertilizac_manejosuelo_id_4ddcc4a9_uniq` (`manejosuelo_id`,`fertilizacion_id`),
  KEY `indicador12_manejosuelo_fertilizacion_3956c85` (`manejosuelo_id`),
  KEY `indicador12_manejosuelo_fertilizacion_587f4b8a` (`fertilizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_manejosuelo_fertilizacion`
--

LOCK TABLES `indicador12_manejosuelo_fertilizacion` WRITE;
/*!40000 ALTER TABLE `indicador12_manejosuelo_fertilizacion` DISABLE KEYS */;
INSERT INTO `indicador12_manejosuelo_fertilizacion` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_manejosuelo_fertilizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_manejosuelo_obra`
--

DROP TABLE IF EXISTS `indicador12_manejosuelo_obra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_manejosuelo_obra` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejosuelo_id` int(11) NOT NULL,
  `conservacion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_manejosuelo_obra_manejosuelo_id_1375ed9f_uniq` (`manejosuelo_id`,`conservacion_id`),
  KEY `indicador12_manejosuelo_obra_3956c85` (`manejosuelo_id`),
  KEY `indicador12_manejosuelo_obra_36336b1a` (`conservacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_manejosuelo_obra`
--

LOCK TABLES `indicador12_manejosuelo_obra` WRITE;
/*!40000 ALTER TABLE `indicador12_manejosuelo_obra` DISABLE KEYS */;
INSERT INTO `indicador12_manejosuelo_obra` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_manejosuelo_obra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_manejosuelo_preparan`
--

DROP TABLE IF EXISTS `indicador12_manejosuelo_preparan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_manejosuelo_preparan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejosuelo_id` int(11) NOT NULL,
  `preparar_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_manejosuelo_preparan_manejosuelo_id_6d55cc91_uniq` (`manejosuelo_id`,`preparar_id`),
  KEY `indicador12_manejosuelo_preparan_3956c85` (`manejosuelo_id`),
  KEY `indicador12_manejosuelo_preparan_69bb60f9` (`preparar_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_manejosuelo_preparan`
--

LOCK TABLES `indicador12_manejosuelo_preparan` WRITE;
/*!40000 ALTER TABLE `indicador12_manejosuelo_preparan` DISABLE KEYS */;
INSERT INTO `indicador12_manejosuelo_preparan` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_manejosuelo_preparan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_manejosuelo_traccion`
--

DROP TABLE IF EXISTS `indicador12_manejosuelo_traccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_manejosuelo_traccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `manejosuelo_id` int(11) NOT NULL,
  `traccion_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_manejosuelo_traccion_manejosuelo_id_2018b54b_uniq` (`manejosuelo_id`,`traccion_id`),
  KEY `indicador12_manejosuelo_traccion_3956c85` (`manejosuelo_id`),
  KEY `indicador12_manejosuelo_traccion_5818a66d` (`traccion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_manejosuelo_traccion`
--

LOCK TABLES `indicador12_manejosuelo_traccion` WRITE;
/*!40000 ALTER TABLE `indicador12_manejosuelo_traccion` DISABLE KEYS */;
INSERT INTO `indicador12_manejosuelo_traccion` VALUES (1,1,2),(2,1,3);
/*!40000 ALTER TABLE `indicador12_manejosuelo_traccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_pendiente`
--

DROP TABLE IF EXISTS `indicador12_pendiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_pendiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_pendiente`
--

LOCK TABLES `indicador12_pendiente` WRITE;
/*!40000 ALTER TABLE `indicador12_pendiente` DISABLE KEYS */;
INSERT INTO `indicador12_pendiente` VALUES (1,'Plana'),(2,'Inclinada'),(3,'Muy inclinada');
/*!40000 ALTER TABLE `indicador12_pendiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_preparar`
--

DROP TABLE IF EXISTS `indicador12_preparar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_preparar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_preparar`
--

LOCK TABLES `indicador12_preparar` WRITE;
/*!40000 ALTER TABLE `indicador12_preparar` DISABLE KEYS */;
INSERT INTO `indicador12_preparar` VALUES (1,'Tala y Quema'),(2,'Trabaja en crudo'),(3,'Arado'),(4,'Usa cobertura');
/*!40000 ALTER TABLE `indicador12_preparar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_profundidad`
--

DROP TABLE IF EXISTS `indicador12_profundidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_profundidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_profundidad`
--

LOCK TABLES `indicador12_profundidad` WRITE;
/*!40000 ALTER TABLE `indicador12_profundidad` DISABLE KEYS */;
INSERT INTO `indicador12_profundidad` VALUES (1,'Muy profunda'),(2,'Media profunda'),(3,'Poca profunda');
/*!40000 ALTER TABLE `indicador12_profundidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo`
--

DROP TABLE IF EXISTS `indicador12_suelo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador12_suelo_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo`
--

LOCK TABLES `indicador12_suelo` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo` DISABLE KEYS */;
INSERT INTO `indicador12_suelo` VALUES (1,2);
/*!40000 ALTER TABLE `indicador12_suelo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_densidad`
--

DROP TABLE IF EXISTS `indicador12_suelo_densidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_densidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `densidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_densidad_suelo_id_5f454559_uniq` (`suelo_id`,`densidad_id`),
  KEY `indicador12_suelo_densidad_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_densidad_44546348` (`densidad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_densidad`
--

LOCK TABLES `indicador12_suelo_densidad` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_densidad` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_densidad` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `indicador12_suelo_densidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_drenaje`
--

DROP TABLE IF EXISTS `indicador12_suelo_drenaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_drenaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `drenaje_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_drenaje_suelo_id_23215169_uniq` (`suelo_id`,`drenaje_id`),
  KEY `indicador12_suelo_drenaje_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_drenaje_427b6580` (`drenaje_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_drenaje`
--

LOCK TABLES `indicador12_suelo_drenaje` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_drenaje` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_drenaje` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_suelo_drenaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_lombrices`
--

DROP TABLE IF EXISTS `indicador12_suelo_lombrices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_lombrices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `densidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_lombrices_suelo_id_2e431f66_uniq` (`suelo_id`,`densidad_id`),
  KEY `indicador12_suelo_lombrices_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_lombrices_44546348` (`densidad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_lombrices`
--

LOCK TABLES `indicador12_suelo_lombrices` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_lombrices` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_lombrices` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_suelo_lombrices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_materia`
--

DROP TABLE IF EXISTS `indicador12_suelo_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_materia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `densidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_materia_suelo_id_5f65d223_uniq` (`suelo_id`,`densidad_id`),
  KEY `indicador12_suelo_materia_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_materia_44546348` (`densidad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_materia`
--

LOCK TABLES `indicador12_suelo_materia` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_materia` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_materia` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_suelo_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_pendiente`
--

DROP TABLE IF EXISTS `indicador12_suelo_pendiente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_pendiente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `pendiente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_pendiente_suelo_id_2af4c6e7_uniq` (`suelo_id`,`pendiente_id`),
  KEY `indicador12_suelo_pendiente_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_pendiente_51b95eb3` (`pendiente_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_pendiente`
--

LOCK TABLES `indicador12_suelo_pendiente` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_pendiente` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_pendiente` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `indicador12_suelo_pendiente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_profundidad`
--

DROP TABLE IF EXISTS `indicador12_suelo_profundidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_profundidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `profundidad_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_profundidad_suelo_id_3196ac35_uniq` (`suelo_id`,`profundidad_id`),
  KEY `indicador12_suelo_profundidad_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_profundidad_2bed5269` (`profundidad_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_profundidad`
--

LOCK TABLES `indicador12_suelo_profundidad` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_profundidad` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_profundidad` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `indicador12_suelo_profundidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_suelo_textura`
--

DROP TABLE IF EXISTS `indicador12_suelo_textura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_suelo_textura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `suelo_id` int(11) NOT NULL,
  `textura_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador12_suelo_textura_suelo_id_4b51e833_uniq` (`suelo_id`,`textura_id`),
  KEY `indicador12_suelo_textura_4f42a16f` (`suelo_id`),
  KEY `indicador12_suelo_textura_2aab50da` (`textura_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_suelo_textura`
--

LOCK TABLES `indicador12_suelo_textura` WRITE;
/*!40000 ALTER TABLE `indicador12_suelo_textura` DISABLE KEYS */;
INSERT INTO `indicador12_suelo_textura` VALUES (1,1,1),(2,1,3);
/*!40000 ALTER TABLE `indicador12_suelo_textura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_textura`
--

DROP TABLE IF EXISTS `indicador12_textura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_textura` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_textura`
--

LOCK TABLES `indicador12_textura` WRITE;
/*!40000 ALTER TABLE `indicador12_textura` DISABLE KEYS */;
INSERT INTO `indicador12_textura` VALUES (1,'Arcilloso'),(2,'Limoso'),(3,'Arenoso');
/*!40000 ALTER TABLE `indicador12_textura` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador12_traccion`
--

DROP TABLE IF EXISTS `indicador12_traccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador12_traccion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador12_traccion`
--

LOCK TABLES `indicador12_traccion` WRITE;
/*!40000 ALTER TABLE `indicador12_traccion` DISABLE KEYS */;
INSERT INTO `indicador12_traccion` VALUES (1,'Animal'),(2,'Humano'),(3,'Tractor'),(4,'Ninguna');
/*!40000 ALTER TABLE `indicador12_traccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador13_ingresofamiliar`
--

DROP TABLE IF EXISTS `indicador13_ingresofamiliar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador13_ingresofamiliar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rubro_id` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `quien_vendio` int(11) DEFAULT NULL,
  `maneja_negocio` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador13_ingresofamiliar_3d65a305` (`rubro_id`),
  KEY `indicador13_ingresofamiliar_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador13_ingresofamiliar`
--

LOCK TABLES `indicador13_ingresofamiliar` WRITE;
/*!40000 ALTER TABLE `indicador13_ingresofamiliar` DISABLE KEYS */;
INSERT INTO `indicador13_ingresofamiliar` VALUES (1,2,1,1,2,1,2),(2,4,1,1,1,1,2);
/*!40000 ALTER TABLE `indicador13_ingresofamiliar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador13_rubros`
--

DROP TABLE IF EXISTS `indicador13_rubros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador13_rubros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `unidad` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador13_rubros`
--

LOCK TABLES `indicador13_rubros` WRITE;
/*!40000 ALTER TABLE `indicador13_rubros` DISABLE KEYS */;
INSERT INTO `indicador13_rubros` VALUES (1,'Aguacate','Cien'),(2,'Ajonjolí','Quintales'),(3,'Arroz','Quintales'),(4,'Aves','Unidad'),(5,'Cacao','Quintales'),(6,'café','Quintales'),(7,'Cebolla','Libras'),(8,'Chiltoma','Libras'),(9,'Cuajada','Libras'),(10,'Frijol','Quintales'),(11,'Guineo','Cabeza'),(12,'Huevos','Docena'),(13,'Jocote','Lata'),(14,'Leche','Litros'),(15,'Limón','Cien'),(16,'Maíz','Quintales'),(17,'Malanga','Quintales'),(18,'Mango','Cien'),(19,'Millón','Quintales'),(20,'Naranja','Cien'),(21,'Pepino','Docena'),(22,'Plátano','Cabeza'),(23,'Quequisque','Quintales'),(24,'Queso','Libras'),(25,'Sorgo','Quintales'),(26,'Ternero de desarrollo','Cabeza'),(27,'Tomate','Libras'),(28,'Vaca','Cabeza'),(29,'Yuca','Quintales');
/*!40000 ALTER TABLE `indicador13_rubros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador14_fuentes`
--

DROP TABLE IF EXISTS `indicador14_fuentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador14_fuentes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador14_fuentes`
--

LOCK TABLES `indicador14_fuentes` WRITE;
/*!40000 ALTER TABLE `indicador14_fuentes` DISABLE KEYS */;
INSERT INTO `indicador14_fuentes` VALUES (1,'Salarios'),(2,'Negocios'),(3,'Remesas'),(4,'Alquiler');
/*!40000 ALTER TABLE `indicador14_fuentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador14_otrosingresos`
--

DROP TABLE IF EXISTS `indicador14_otrosingresos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador14_otrosingresos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fuente_id` int(11) NOT NULL,
  `tipo_id` int(11) NOT NULL,
  `meses` int(11) DEFAULT NULL,
  `ingreso` int(11) DEFAULT NULL,
  `tiene_ingreso` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador14_otrosingresos_7592e3f3` (`fuente_id`),
  KEY `indicador14_otrosingresos_27e4f492` (`tipo_id`),
  KEY `indicador14_otrosingresos_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador14_otrosingresos`
--

LOCK TABLES `indicador14_otrosingresos` WRITE;
/*!40000 ALTER TABLE `indicador14_otrosingresos` DISABLE KEYS */;
INSERT INTO `indicador14_otrosingresos` VALUES (1,1,1,2,2,1,2);
/*!40000 ALTER TABLE `indicador14_otrosingresos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador14_tipotrabajo`
--

DROP TABLE IF EXISTS `indicador14_tipotrabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador14_tipotrabajo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador14_tipotrabajo`
--

LOCK TABLES `indicador14_tipotrabajo` WRITE;
/*!40000 ALTER TABLE `indicador14_tipotrabajo` DISABLE KEYS */;
INSERT INTO `indicador14_tipotrabajo` VALUES (1,'nada');
/*!40000 ALTER TABLE `indicador14_tipotrabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_detallecasa`
--

DROP TABLE IF EXISTS `indicador15_detallecasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_detallecasa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tamano` int(11) DEFAULT NULL,
  `ambientes` int(11) DEFAULT NULL,
  `letrina` int(11) DEFAULT NULL,
  `lavadero` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador15_detallecasa_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_detallecasa`
--

LOCK TABLES `indicador15_detallecasa` WRITE;
/*!40000 ALTER TABLE `indicador15_detallecasa` DISABLE KEYS */;
INSERT INTO `indicador15_detallecasa` VALUES (1,12,1,1,1,2);
/*!40000 ALTER TABLE `indicador15_detallecasa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_equipos`
--

DROP TABLE IF EXISTS `indicador15_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_equipos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_equipos`
--

LOCK TABLES `indicador15_equipos` WRITE;
/*!40000 ALTER TABLE `indicador15_equipos` DISABLE KEYS */;
INSERT INTO `indicador15_equipos` VALUES (1,'Arado'),(2,'Bomba de fumigar'),(3,'Bomba de motor'),(4,'Carreta'),(5,'Moto sierra'),(6,'Motor de riego'),(7,'Panel solar'),(8,'Picadora'),(9,'Silos metalicos'),(10,'Plancha'),(11,'Radio'),(12,'TV'),(13,'DVD'),(14,'Celular'),(15,'Licuadora'),(16,'Refrigeradora'),(17,'Muebles'),(18,'Biodigestor');
/*!40000 ALTER TABLE `indicador15_equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_herramientas`
--

DROP TABLE IF EXISTS `indicador15_herramientas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_herramientas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `herramienta_id` int(11) NOT NULL,
  `numero` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador15_herramientas_18dc765` (`herramienta_id`),
  KEY `indicador15_herramientas_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_herramientas`
--

LOCK TABLES `indicador15_herramientas` WRITE;
/*!40000 ALTER TABLE `indicador15_herramientas` DISABLE KEYS */;
INSERT INTO `indicador15_herramientas` VALUES (1,2,1,2),(2,3,1,2),(3,5,1,2);
/*!40000 ALTER TABLE `indicador15_herramientas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_infraestructuras`
--

DROP TABLE IF EXISTS `indicador15_infraestructuras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_infraestructuras` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_infraestructuras`
--

LOCK TABLES `indicador15_infraestructuras` WRITE;
/*!40000 ALTER TABLE `indicador15_infraestructuras` DISABLE KEYS */;
INSERT INTO `indicador15_infraestructuras` VALUES (1,'Pilas'),(2,'Corrales de vacas'),(3,'Corrales de cerdos'),(4,'Caseta de ternero'),(5,'Caseta de aves'),(6,'Comederos'),(7,'Silo forrajero'),(8,'Tanque de plástico'),(9,'Tanque de cemento'),(10,'Pozos');
/*!40000 ALTER TABLE `indicador15_infraestructuras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_nombreherramienta`
--

DROP TABLE IF EXISTS `indicador15_nombreherramienta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_nombreherramienta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_nombreherramienta`
--

LOCK TABLES `indicador15_nombreherramienta` WRITE;
/*!40000 ALTER TABLE `indicador15_nombreherramienta` DISABLE KEYS */;
INSERT INTO `indicador15_nombreherramienta` VALUES (1,'Machete'),(2,'Coba'),(3,'Piocha'),(4,'Pala'),(5,'Rastrillo'),(6,'Herramienta para poda'),(7,'Hacha'),(8,'Barra'),(9,'Carretilla');
/*!40000 ALTER TABLE `indicador15_nombreherramienta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_nombretransporte`
--

DROP TABLE IF EXISTS `indicador15_nombretransporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_nombretransporte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_nombretransporte`
--

LOCK TABLES `indicador15_nombretransporte` WRITE;
/*!40000 ALTER TABLE `indicador15_nombretransporte` DISABLE KEYS */;
INSERT INTO `indicador15_nombretransporte` VALUES (1,'Caballos o mulas'),(2,'Carreta de bueyes o caballos'),(3,'Bicicleta'),(4,'Motocicleta'),(5,'Camioneta o carro'),(6,'Tractor');
/*!40000 ALTER TABLE `indicador15_nombretransporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_piso`
--

DROP TABLE IF EXISTS `indicador15_piso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_piso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_piso`
--

LOCK TABLES `indicador15_piso` WRITE;
/*!40000 ALTER TABLE `indicador15_piso` DISABLE KEYS */;
INSERT INTO `indicador15_piso` VALUES (1,'Tierra'),(2,'Ladrillo de barro'),(3,'Embaldosado'),(4,'Cemento fino'),(5,'Cerámica');
/*!40000 ALTER TABLE `indicador15_piso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_propiedades`
--

DROP TABLE IF EXISTS `indicador15_propiedades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_propiedades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `equipo_id` int(11) DEFAULT NULL,
  `cantidad_equipo` int(11) DEFAULT NULL,
  `infraestructura_id` int(11) DEFAULT NULL,
  `cantidad_infra` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador15_propiedades_7f4dba11` (`equipo_id`),
  KEY `indicador15_propiedades_7b190813` (`infraestructura_id`),
  KEY `indicador15_propiedades_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_propiedades`
--

LOCK TABLES `indicador15_propiedades` WRITE;
/*!40000 ALTER TABLE `indicador15_propiedades` DISABLE KEYS */;
INSERT INTO `indicador15_propiedades` VALUES (1,2,1,1,1,2),(2,14,1,4,1,2),(3,18,1,4,1,2);
/*!40000 ALTER TABLE `indicador15_propiedades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_techo`
--

DROP TABLE IF EXISTS `indicador15_techo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_techo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_techo`
--

LOCK TABLES `indicador15_techo` WRITE;
/*!40000 ALTER TABLE `indicador15_techo` DISABLE KEYS */;
INSERT INTO `indicador15_techo` VALUES (1,'Plástico'),(2,'Paja'),(3,'Teja de madera'),(4,'Teja de barro'),(5,'Zinc');
/*!40000 ALTER TABLE `indicador15_techo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_tipocasa`
--

DROP TABLE IF EXISTS `indicador15_tipocasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_tipocasa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador15_tipocasa_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_tipocasa`
--

LOCK TABLES `indicador15_tipocasa` WRITE;
/*!40000 ALTER TABLE `indicador15_tipocasa` DISABLE KEYS */;
INSERT INTO `indicador15_tipocasa` VALUES (1,1,2);
/*!40000 ALTER TABLE `indicador15_tipocasa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_tipocasa_piso`
--

DROP TABLE IF EXISTS `indicador15_tipocasa_piso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_tipocasa_piso` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipocasa_id` int(11) NOT NULL,
  `piso_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador15_tipocasa_piso_tipocasa_id_93b84bc_uniq` (`tipocasa_id`,`piso_id`),
  KEY `indicador15_tipocasa_piso_3ea3b976` (`tipocasa_id`),
  KEY `indicador15_tipocasa_piso_6e78a6eb` (`piso_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_tipocasa_piso`
--

LOCK TABLES `indicador15_tipocasa_piso` WRITE;
/*!40000 ALTER TABLE `indicador15_tipocasa_piso` DISABLE KEYS */;
INSERT INTO `indicador15_tipocasa_piso` VALUES (1,1,2),(2,1,3),(3,1,5);
/*!40000 ALTER TABLE `indicador15_tipocasa_piso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_tipocasa_techo`
--

DROP TABLE IF EXISTS `indicador15_tipocasa_techo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_tipocasa_techo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipocasa_id` int(11) NOT NULL,
  `techo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador15_tipocasa_techo_tipocasa_id_787b2640_uniq` (`tipocasa_id`,`techo_id`),
  KEY `indicador15_tipocasa_techo_3ea3b976` (`tipocasa_id`),
  KEY `indicador15_tipocasa_techo_373c9b26` (`techo_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_tipocasa_techo`
--

LOCK TABLES `indicador15_tipocasa_techo` WRITE;
/*!40000 ALTER TABLE `indicador15_tipocasa_techo` DISABLE KEYS */;
INSERT INTO `indicador15_tipocasa_techo` VALUES (1,1,1),(2,1,3),(3,1,4);
/*!40000 ALTER TABLE `indicador15_tipocasa_techo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador15_transporte`
--

DROP TABLE IF EXISTS `indicador15_transporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador15_transporte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transporte_id` int(11) NOT NULL,
  `numero` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador15_transporte_4de90b82` (`transporte_id`),
  KEY `indicador15_transporte_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador15_transporte`
--

LOCK TABLES `indicador15_transporte` WRITE;
/*!40000 ALTER TABLE `indicador15_transporte` DISABLE KEYS */;
INSERT INTO `indicador15_transporte` VALUES (1,2,1,2),(2,3,1,2),(3,4,2,2);
/*!40000 ALTER TABLE `indicador15_transporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador16_ahorro`
--

DROP TABLE IF EXISTS `indicador16_ahorro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador16_ahorro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ahorro_id` int(11) NOT NULL,
  `respuesta` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador16_ahorro_15d5b4df` (`ahorro_id`),
  KEY `indicador16_ahorro_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador16_ahorro`
--

LOCK TABLES `indicador16_ahorro` WRITE;
/*!40000 ALTER TABLE `indicador16_ahorro` DISABLE KEYS */;
INSERT INTO `indicador16_ahorro` VALUES (1,2,1,2);
/*!40000 ALTER TABLE `indicador16_ahorro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador16_ahorropregunta`
--

DROP TABLE IF EXISTS `indicador16_ahorropregunta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador16_ahorropregunta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador16_ahorropregunta`
--

LOCK TABLES `indicador16_ahorropregunta` WRITE;
/*!40000 ALTER TABLE `indicador16_ahorropregunta` DISABLE KEYS */;
INSERT INTO `indicador16_ahorropregunta` VALUES (1,'¿Tiene ahorro en efectivo?'),(2,'¿Tiene ahorro en joyeria/prendas?'),(3,'Desde cuando ahorra'),(4,'Posee una cuenta de ahorro?'),(5,'Ahorra a nombre de quien?'),(6,'¿Si no tiene ahorro, está interesado en ahorrar en una cuenta de ahorro?');
/*!40000 ALTER TABLE `indicador16_ahorropregunta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador17_credito`
--

DROP TABLE IF EXISTS `indicador17_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador17_credito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recibe` int(11) DEFAULT NULL,
  `desde` int(11) DEFAULT NULL,
  `satisfaccion` int(11) DEFAULT NULL,
  `dia` int(11) DEFAULT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador17_credito_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador17_credito`
--

LOCK TABLES `indicador17_credito` WRITE;
/*!40000 ALTER TABLE `indicador17_credito` DISABLE KEYS */;
INSERT INTO `indicador17_credito` VALUES (1,1,1,2,1,2);
/*!40000 ALTER TABLE `indicador17_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador17_credito_ocupa_credito`
--

DROP TABLE IF EXISTS `indicador17_credito_ocupa_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador17_credito_ocupa_credito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `credito_id` int(11) NOT NULL,
  `ocupacredito_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador17_credito_ocupa_credito_credito_id_61891b52_uniq` (`credito_id`,`ocupacredito_id`),
  KEY `indicador17_credito_ocupa_credito_a3100cd` (`credito_id`),
  KEY `indicador17_credito_ocupa_credito_227cc9f8` (`ocupacredito_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador17_credito_ocupa_credito`
--

LOCK TABLES `indicador17_credito_ocupa_credito` WRITE;
/*!40000 ALTER TABLE `indicador17_credito_ocupa_credito` DISABLE KEYS */;
INSERT INTO `indicador17_credito_ocupa_credito` VALUES (1,1,8),(2,1,2),(3,1,3),(4,1,5);
/*!40000 ALTER TABLE `indicador17_credito_ocupa_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador17_credito_quien_credito`
--

DROP TABLE IF EXISTS `indicador17_credito_quien_credito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador17_credito_quien_credito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `credito_id` int(11) NOT NULL,
  `dacredito_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador17_credito_quien_credito_credito_id_d8c6e30_uniq` (`credito_id`,`dacredito_id`),
  KEY `indicador17_credito_quien_credito_a3100cd` (`credito_id`),
  KEY `indicador17_credito_quien_credito_6361b2e8` (`dacredito_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador17_credito_quien_credito`
--

LOCK TABLES `indicador17_credito_quien_credito` WRITE;
/*!40000 ALTER TABLE `indicador17_credito_quien_credito` DISABLE KEYS */;
INSERT INTO `indicador17_credito_quien_credito` VALUES (1,1,2),(2,1,3),(3,1,5);
/*!40000 ALTER TABLE `indicador17_credito_quien_credito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador17_dacredito`
--

DROP TABLE IF EXISTS `indicador17_dacredito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador17_dacredito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador17_dacredito`
--

LOCK TABLES `indicador17_dacredito` WRITE;
/*!40000 ALTER TABLE `indicador17_dacredito` DISABLE KEYS */;
INSERT INTO `indicador17_dacredito` VALUES (1,'Cooperativas'),(2,'Asociaciones'),(3,'Microfinancieras'),(4,'Bancos'),(5,'Proyectos'),(6,'Familiares'),(7,'Prestamistas');
/*!40000 ALTER TABLE `indicador17_dacredito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador17_ocupacredito`
--

DROP TABLE IF EXISTS `indicador17_ocupacredito`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador17_ocupacredito` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador17_ocupacredito`
--

LOCK TABLES `indicador17_ocupacredito` WRITE;
/*!40000 ALTER TABLE `indicador17_ocupacredito` DISABLE KEYS */;
INSERT INTO `indicador17_ocupacredito` VALUES (1,'Inversión agrícola'),(2,'Inversión ganadera (compra de ganado))'),(3,'Cultivos agrícolas'),(4,'Tierra y vivienda'),(5,'Mejora la infraestructura productiva'),(6,'Consumo'),(7,'Educación y salud'),(8,'Para pagar deuda');
/*!40000 ALTER TABLE `indicador17_ocupacredito` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador18_alimentos`
--

DROP TABLE IF EXISTS `indicador18_alimentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador18_alimentos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador18_alimentos`
--

LOCK TABLES `indicador18_alimentos` WRITE;
/*!40000 ALTER TABLE `indicador18_alimentos` DISABLE KEYS */;
INSERT INTO `indicador18_alimentos` VALUES (1,'Aceite'),(2,'Arroz'),(3,'Avena'),(4,'Azúcar'),(5,'Café'),(6,'Carne de cerdo'),(7,'Carne de res'),(8,'Crema'),(9,'Cuajada'),(10,'Frijol'),(11,'Frutas'),(12,'Guineo'),(13,'Huevos'),(14,'Leche'),(15,'Maíz'),(16,'Malanga'),(17,'Miel'),(18,'Millón'),(19,'Papa'),(20,'Plátano'),(21,'Pollo'),(22,'Quequisque'),(23,'Queso'),(24,'Sorgo'),(25,'Soya'),(26,'Verdura'),(27,'Yuca');
/*!40000 ALTER TABLE `indicador18_alimentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador18_seguridad`
--

DROP TABLE IF EXISTS `indicador18_seguridad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador18_seguridad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alimento_id` int(11) NOT NULL,
  `producen` int(11) NOT NULL,
  `compran` int(11) NOT NULL,
  `consumen` int(11) NOT NULL,
  `consumen_invierno` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador18_seguridad_7daf7119` (`alimento_id`),
  KEY `indicador18_seguridad_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador18_seguridad`
--

LOCK TABLES `indicador18_seguridad` WRITE;
/*!40000 ALTER TABLE `indicador18_seguridad` DISABLE KEYS */;
INSERT INTO `indicador18_seguridad` VALUES (1,1,1,1,2,2,2),(2,3,1,1,2,2,2);
/*!40000 ALTER TABLE `indicador18_seguridad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador19_causa`
--

DROP TABLE IF EXISTS `indicador19_causa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador19_causa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador19_causa`
--

LOCK TABLES `indicador19_causa` WRITE;
/*!40000 ALTER TABLE `indicador19_causa` DISABLE KEYS */;
INSERT INTO `indicador19_causa` VALUES (1,'Fenómenos naturales'),(2,'Razones agrícolas'),(3,'Razones de mercados'),(4,'Inversión');
/*!40000 ALTER TABLE `indicador19_causa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador19_fenomeno`
--

DROP TABLE IF EXISTS `indicador19_fenomeno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador19_fenomeno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `causa_id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador19_fenomeno_551feef0` (`causa_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador19_fenomeno`
--

LOCK TABLES `indicador19_fenomeno` WRITE;
/*!40000 ALTER TABLE `indicador19_fenomeno` DISABLE KEYS */;
INSERT INTO `indicador19_fenomeno` VALUES (1,1,'Sequía'),(2,1,'Inundación'),(3,1,'Vientos'),(4,1,'Deslizamiento'),(5,2,'Falta de semilla'),(6,2,'Mala calidad de semilla'),(7,2,'Plagas y enfermedades'),(8,3,'Bajo precio'),(9,3,'Falta de venta'),(10,3,'Estafa de contrato'),(11,3,'Falta de calidad de producto'),(12,4,'Falta de crédito'),(13,4,'Altos interés');
/*!40000 ALTER TABLE `indicador19_fenomeno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador19_graves`
--

DROP TABLE IF EXISTS `indicador19_graves`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador19_graves` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador19_graves`
--

LOCK TABLES `indicador19_graves` WRITE;
/*!40000 ALTER TABLE `indicador19_graves` DISABLE KEYS */;
INSERT INTO `indicador19_graves` VALUES (1,'Año con año'),(2,'Cada 5 años'),(3,'Cada 10 años'),(4,'Nunca');
/*!40000 ALTER TABLE `indicador19_graves` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador19_vulnerable`
--

DROP TABLE IF EXISTS `indicador19_vulnerable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador19_vulnerable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `motivo_id` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador19_vulnerable_2f34f19e` (`motivo_id`),
  KEY `indicador19_vulnerable_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador19_vulnerable`
--

LOCK TABLES `indicador19_vulnerable` WRITE;
/*!40000 ALTER TABLE `indicador19_vulnerable` DISABLE KEYS */;
INSERT INTO `indicador19_vulnerable` VALUES (1,2,2),(2,8,2);
/*!40000 ALTER TABLE `indicador19_vulnerable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador19_vulnerable_respuesta`
--

DROP TABLE IF EXISTS `indicador19_vulnerable_respuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador19_vulnerable_respuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vulnerable_id` int(11) NOT NULL,
  `graves_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `indicador19_vulnerable_respuesta_vulnerable_id_7b16efb1_uniq` (`vulnerable_id`,`graves_id`),
  KEY `indicador19_vulnerable_respuesta_9267f6e` (`vulnerable_id`),
  KEY `indicador19_vulnerable_respuesta_277be174` (`graves_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador19_vulnerable_respuesta`
--

LOCK TABLES `indicador19_vulnerable_respuesta` WRITE;
/*!40000 ALTER TABLE `indicador19_vulnerable_respuesta` DISABLE KEYS */;
INSERT INTO `indicador19_vulnerable_respuesta` VALUES (1,1,2),(2,2,3);
/*!40000 ALTER TABLE `indicador19_vulnerable_respuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador20_preguntariesgo`
--

DROP TABLE IF EXISTS `indicador20_preguntariesgo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador20_preguntariesgo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador20_preguntariesgo`
--

LOCK TABLES `indicador20_preguntariesgo` WRITE;
/*!40000 ALTER TABLE `indicador20_preguntariesgo` DISABLE KEYS */;
INSERT INTO `indicador20_preguntariesgo` VALUES (1,'¿Realiza monitoreo de plagas y enfermedades?'),(2,'¿Disponen suficiente recursos para manejo de finca?'),(3,'¿Cuenta con obras para almacenamiento de agua?'),(4,'¿Participan en cadena de distribución de productos?'),(5,'¿Cuenta con un contrato para la venta de productos?'),(6,'¿Dispone de tecnología para el secado y almacenamiento de cosecha?');
/*!40000 ALTER TABLE `indicador20_preguntariesgo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `indicador20_riesgos`
--

DROP TABLE IF EXISTS `indicador20_riesgos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `indicador20_riesgos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pregunta_id` int(11) NOT NULL,
  `respuesta` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `indicador20_riesgos_37c55af2` (`pregunta_id`),
  KEY `indicador20_riesgos_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indicador20_riesgos`
--

LOCK TABLES `indicador20_riesgos` WRITE;
/*!40000 ALTER TABLE `indicador20_riesgos` DISABLE KEYS */;
INSERT INTO `indicador20_riesgos` VALUES (1,1,1,2),(2,4,2,2);
/*!40000 ALTER TABLE `indicador20_riesgos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_comunidad`
--

DROP TABLE IF EXISTS `lugar_comunidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_comunidad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `municipio_id` int(11) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lugar_comunidad_cebc556` (`municipio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_comunidad`
--

LOCK TABLES `lugar_comunidad` WRITE;
/*!40000 ALTER TABLE `lugar_comunidad` DISABLE KEYS */;
INSERT INTO `lugar_comunidad` VALUES (1,5025,'grande');
/*!40000 ALTER TABLE `lugar_comunidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
INSERT INTO `lugar_departamento` VALUES (5,'Nueva Segovia','Nueva-segovia','3491.28'),(10,'Jinotega','jinotega','9222.40'),(20,'Madriz','madriz','1708.23'),(25,'Estelí','esteli','2229.69'),(30,'Chinandega','chinandega','4822.46'),(35,'León','leon','5138.03'),(40,'Matagalpa','matagalpa','6803.86'),(50,'Boaco','boaco','4176.68'),(55,'Managua','managua','3465.10'),(60,'Masaya','masaya','610.78'),(65,'Chontales','chontales','6481.27'),(70,'Granada','granada','1039.68'),(75,'Carazo','carazo','1081.40'),(80,'Rivas','rivas','2161.82'),(85,'Rí­o San Juan','Rio-san-juan','7540.90'),(91,'RAAN','RAAN','32819.68'),(93,'RAAS','RAAS','27546.32'),(99,'Cobertura Nacional','cobertura-nacional','333333.00');
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `latitud` decimal(8,5) DEFAULT NULL,
  `longitud` decimal(8,5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_779a4ea6` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
INSERT INTO `lugar_municipio` VALUES (505,5,'Jalapa','jalapa','0.00','13.92286','-86.12520'),(510,5,'Murra','murra','0.00','13.75900','-86.01799'),(515,5,'El Jí­caro','El-jicaro','0.00','13.72326','-86.13705'),(520,5,'San Fernando','San-fernando','0.00','13.67729','-86.31484'),(525,5,'Mozonte','mozonte','0.00','13.66168','-86.43706'),(530,5,'Dipilto','dipilto','0.00','13.72243','-86.50720'),(535,5,'Macuelizo','macuelizo','0.00','13.65239','-86.61380'),(540,5,'Santa Marí­a','santamaria','0.00','13.74753','-86.71077'),(545,5,'Ocotal','ocotal','0.00','13.63432','-86.47745'),(550,5,'Ciudad Antigua','Ciudad-antigua','0.00','13.64217','-86.30893'),(555,5,'Quilalí','quilali','0.00','13.56675','-86.02952'),(560,5,'Wiwili de Nueva Segovia','Wiwili-nuevasegovia','0.00','13.62667','-85.82369'),(1005,10,'Wiwilí','Wiwili','0.00','13.62130','-85.81864'),(1010,10,'El Cúa','El-cua','0.00','13.36764','-85.67330'),(1012,10,'San José Bocay','San-jose-bocay','0.00','13.61976','-85.50080'),(1015,10,'Sta. María de Pantasma','Santa-maria-pantasma','0.00','13.36667','-85.95000'),(1020,10,'San Rafael del Norte','San-rafael-del-norte','0.00','13.21391','-86.11043'),(1025,10,'San Sebastian de Yalí','yali','0.00','13.30500','-86.18636'),(1030,10,'La Concordia','La-concordia','0.00','13.19535','-86.16693'),(1035,10,'Jinotega','jinotega','0.00','13.09165','-86.00121'),(2005,20,'Somoto','somoto','0.00','13.48129','-86.58337'),(2010,20,'Totogalpa','totogalpa','0.00','13.56336','-86.49281'),(2015,20,'Telpaneca','telpaneca','0.00','13.53131','-86.28693'),(2020,20,'San Juan de Río Coco','San-juan-rio-coco','0.00','13.54458','-86.16537'),(2025,20,'Palacaguina','palacaguina','0.00','13.45597','-86.40710'),(2030,20,'Yalaguina','yalaguina','0.00','13.48351','-86.49344'),(2035,20,'San Lucas','San-lucas','0.00','13.41358','-86.61176'),(2040,20,'Las Sabanas','Las-sabanas','0.00','13.34324','-86.62194'),(2045,20,'San José de Cusmapa','San-jose-cusmapa','0.00','13.28847','-86.65489'),(2505,25,'Pueblo Nuevo','Pueblo-nuevo','0.00','13.37937','-86.48077'),(2510,25,'Condega','condega','0.00','13.36213','-86.39789'),(2515,25,'Estelí','esteli','0.00','13.08948','-86.35551'),(2520,25,'San Juan de Limay','Sanjuan-limay','0.00','13.17489','-86.61234'),(2525,25,'La Trinidad','trinidad','0.00','12.96823','-86.23604'),(2530,25,'San Nicolás','San-nicolas','0.00','12.93312','-86.34700'),(3005,30,'San Pedro del Norte','San-pedro-del-norte','0.00','13.27596','-86.87777'),(3010,30,'San Francisco del Norte','San-francisco-del-norte','0.00','13.20016','-86.77192'),(3015,30,'Cinco Pinos','Cinco-pinos','0.00','13.23036','-86.86719'),(3020,30,'Santo Tomás del Norte','Santo-tomas-del-norte','0.00','13.18701','-86.92352'),(3025,30,'El Viejo','El-viejo','0.00','12.66228','-87.16541'),(3030,30,'Pto. Morazán','Puerto-morazan','0.00','12.76721','-87.13388'),(3035,30,'Somotillo','somotillo','0.00','13.04495','-86.90499'),(3040,30,'Villanueva','villanueva','0.00','12.96391','-86.81468'),(3045,30,'Chinandega','chinandega','0.00','12.62872','-87.13149'),(3050,30,'El Realejo','El-realejo','0.00','12.54551','-87.16736'),(3055,30,'Corinto','corinto','0.00','12.48461','-87.17122'),(3060,30,'Chichigalpa','chichigalpa','0.00','12.57224','-87.02849'),(3065,30,'Posoltega','posotelga','0.00','12.54410','-86.98010'),(3505,35,'Achuapa','achuapa','0.00','13.05433','-86.59070'),(3510,35,'El Sauce','El-sauce','0.00','12.88694','-86.53952'),(3515,35,'Santa Rosa del Peñon','Santa-rosa-del-penon','0.00','12.80142','-86.37144'),(3520,35,'El Jicaral','El-jicaral','0.00','12.72672','-86.38134'),(3525,35,'Larreynaga','larreynaga','0.00','12.59311','-86.68015'),(3530,35,'Telica','telica','0.00','12.52152','-86.86030'),(3535,35,'Quezalguaque','quezalguaque','0.00','12.50614','-86.90366'),(3540,35,'León','leon','0.00','12.43481','-86.88174'),(3545,35,'La Paz Centro','La-paz-centro','0.00','12.34011','-86.67625'),(3550,35,'Nagarote','nagarote','0.00','12.26531','-86.56812'),(4005,40,'Rancho Grande','Rancho-grande','0.00','13.25352','-85.55268'),(4010,40,'Rí­o Blanco','Rio-blanco','0.00','12.93044','-85.22610'),(4015,40,'El Tuma - La Dalia','El-tuma','0.00','13.13735','-85.73788'),(4020,40,'San Isidro','San-isidro','0.00','12.92937','-86.19550'),(4025,40,'Sébaco','sebaco','0.00','12.85190','-86.09696'),(4030,40,'Matagalpa','matagalpa','0.00','12.92709','-85.91747'),(4035,40,'San Ramón','San-ramon','0.00','12.92254','-85.83968'),(4040,40,'Matiguás','matiguas','0.00','12.83710','-85.46079'),(4045,40,'Muy Muy','muymuy','0.00','12.76125','-85.63123'),(4050,40,'Esquipulas','esquipulas','0.00','12.66446','-85.78909'),(4055,40,'San Dionisio','San-dionisio','0.00','12.76190','-85.85091'),(4060,40,'Terrabona','terrabona','0.00','12.73009','-85.96487'),(4065,40,'Ciudad Darí­o','Ciudad-dario','0.00','12.73000','-86.12457'),(5005,50,'San José de los Remates','San-jose-de-los-remates','0.00','12.59748','-85.76253'),(5010,50,'Boaco','boaco','0.00','12.47160','-85.65952'),(5015,50,'Camoapa','camoapa','0.00','12.38377','-85.51465'),(5020,50,'Santa Lucía','Santa-lucia','0.00','12.53226','-85.71156'),(5025,50,'Teustepe','teustepe','0.00','12.41979','-85.79922'),(5030,50,'San  Lorenzo','San-lorenzo','0.00','12.37789','-85.66718'),(5505,55,'San Francisco Libre','San-francisco-libre','0.00','12.50458','-86.30105'),(5510,55,'Tipitapa','tipitapa','0.00','12.19662','-86.09682'),(5515,55,'Mateare','mateare','0.00','12.23536','-86.43013'),(5520,55,'Villa Carlos Fonseca','Villa-carlos-fonseca','0.00','11.97924','-86.50809'),(5522,55,'Ciudad Sandino','Ciudad-sandino','0.00','12.16082','-86.35004'),(5525,55,'Managua','managua','0.00','12.14746','-86.27339'),(5530,55,'Ticuantepe','ticuantepe','0.00','12.02125','-86.20288'),(5532,55,'El Crucero','El-crucero','0.00','11.97865','-86.31076'),(5535,55,'San Rafael del Sur','San-rafael-del-sur','0.00','11.84681','-86.43977'),(6005,60,'Nindirí','nindiri','0.00','12.00243','-86.12067'),(6010,60,'Masaya','masaya','0.00','11.97735','-86.09606'),(6015,60,'Tisma','tisma','0.00','12.08133','-86.01921'),(6020,60,'La Concepción','La-concepcion','0.00','11.93615','-86.19220'),(6025,60,'Masatepe','masatepe','0.00','11.91344','-86.14475'),(6030,60,'Nandasmo','nandasmo','0.00','11.90933','-86.13055'),(6035,60,'Catarina','catarina','0.00','11.91078','-86.07407'),(6040,60,'San Juan de Oriente','San-juan-de-oriente','0.00','11.90479','-86.07311'),(6045,60,'Niquinohomo','niquinomo','0.00','11.90408','-86.09472'),(6505,65,'Comalapa','comalapa','0.00','12.28340','-85.51142'),(6507,65,'San Francisco Cuapa','San-francisco-cuapa','0.00','12.26671','-85.38308'),(6510,65,'Juigalpa','juigalpa','0.00','12.10580','-85.36842'),(6515,65,'La Libertad','La-libertad','0.00','12.21539','-85.16549'),(6520,65,'Santo Domingo','Santo-domingo','0.00','12.26301','-85.08232'),(6525,65,'Santo Tomás','Santo-tomas','0.00','12.06902','-85.09340'),(6530,65,'San Pedro de Lóvago','San-pedro-de-lovago','0.00','12.12852','-85.11572'),(6535,65,'Acoyapa','acoyapa','0.00','11.96764','-85.17044'),(6540,65,'Villa Sandino','Villa-sandino','0.00','12.04779','-84.99334'),(6545,65,'El Coral','El-coral','0.00','11.91576','-84.65041'),(7005,70,'Diriá','diria','0.00','11.88416','-86.05565'),(7010,70,'Diriomo','diriomo','0.00','11.87494','-86.05110'),(7015,70,'Granada','granada','0.00','11.93095','-85.95696'),(7020,70,'Nandaime','nandaime','0.00','11.75630','-86.05345'),(7505,75,'San Marcos','San-marcos','0.00','11.90651','-86.20314'),(7510,75,'Jinotepe','jinotepe','0.00','11.84831','-86.19846'),(7515,75,'Dolores','dolores','0.00','11.85565','-86.21535'),(7520,75,'Diriamba','diriamba','0.00','11.85572','-86.24074'),(7525,75,'El Rosario','El-rosario','0.00','11.83224','-86.16484'),(7530,75,'La Paz de Carazo','La-paz-de-carazo','0.00','11.82206','-86.12750'),(7535,75,'Santa Teresa','Santa-tereza','0.00','11.80272','-86.16281'),(7540,75,'La Conquista','La-conquista','0.00','11.73336','-86.19297'),(8005,80,'Tola','tola','0.00','11.43868','-85.93907'),(8010,80,'Belén','belen','0.00','11.50081','-85.89014'),(8015,80,'Potosí','potosi','0.00','11.49320','-85.85709'),(8020,80,'Buenos Aires','Buenos-aires','0.00','11.46923','-85.81701'),(8025,80,'Moyogalpa','moyogalpa','0.00','11.53947','-85.69746'),(8030,80,'Altagracia','altagracia','0.00','11.56547','-85.57793'),(8035,80,'San Jorge','San-jorge','0.00','11.45532','-85.80074'),(8040,80,'Rivas','rivas','0.00','11.43975','-85.82880'),(8045,80,'San Juan del Sur','San-juan-del-sur','0.00','11.25384','-85.87177'),(8050,80,'Cárdenas','cardenas','0.00','11.19521','-85.50886'),(8505,85,'Morrito','morrito','0.00','11.62130','-85.08169'),(8510,85,'El Almendro','El-almendro','0.00','11.67684','-84.70362'),(8515,85,'San Miguelito','San-miguelito','0.00','11.40156','-84.90005'),(8520,85,'San Carlos','San-carlos','0.00','11.12088','-84.77837'),(8525,85,'El Castillo','El-castillo','0.00','11.03969','-84.47295'),(8530,85,'San Juan del Norte','San-juan-del-norte','0.00','10.94671','-83.73479'),(9105,91,'Waspán','waspan','0.00','14.74386','-83.96885'),(9110,91,'Puerto Cabezas','Puerto-cabezas','0.00','14.03313','-83.38223'),(9115,91,'Rosita','rosita','0.00','13.91060','-84.39153'),(9120,91,'Bonanza','bonanza','0.00','14.02584','-84.62088'),(9127,91,'Mulukuku','mulukuku','0.00','13.15000','-84.96667'),(9125,91,'Waslala','waslala','0.00','13.33465','-85.37099'),(9130,91,'Siuna','siuna','0.00','13.73857','-84.78491'),(9135,91,'Prinzapolka','prinzapolka','0.00','13.40611','-83.56229'),(9305,93,'Paiwas','paiwas','0.00','12.78548','-85.12402'),(9310,93,'La Cruz de Río Grande','La-cruz-rio-grande','0.00','13.11145','-84.18835'),(9312,93,'Desembocadura de Río Grande','Desembocadura-rio-grande','0.00','12.93208','-83.57697'),(9315,93,'Laguna de Perlas','Laguna-de-perlas','0.00','12.34096','-83.67052'),(9316,93,'El Tortuguero','El-tortuguero','0.00','12.82085','-84.19906'),(9320,93,'Rama','rama','0.00','12.16004','-84.21913'),(9323,93,'El Ayote','El-ayote','0.00','12.49486','-84.81943'),(9325,93,'Muelle de los Bueyes','Muelle-de-los-bueyes','0.00','12.06764','-84.53749'),(9330,93,'Kukra - Hill','Kukra-hill','0.00','12.24163','-83.74532'),(9335,93,'Corn Island','Corn-island','0.00','12.18017','-83.05975'),(9340,93,'Bluefields','bluefields','0.00','12.01144','-83.76388'),(9345,93,'Nueva Guinea','Nueva-guinea','0.00','11.68827','-84.45794'),(1040,10,'Altowangky','altowanky','0.00',NULL,NULL);
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simas_encuesta`
--

DROP TABLE IF EXISTS `simas_encuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `simas_encuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `recolector_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `cedula` varchar(200) DEFAULT NULL,
  `finca` varchar(200) NOT NULL,
  `comunidad_id` int(11) NOT NULL,
  `sexo` int(11) NOT NULL,
  `organizacion_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `simas_encuesta_656033f0` (`recolector_id`),
  KEY `simas_encuesta_62329ccf` (`comunidad_id`),
  KEY `simas_encuesta_48753264` (`organizacion_id`),
  KEY `simas_encuesta_403f60f` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simas_encuesta`
--

LOCK TABLES `simas_encuesta` WRITE;
/*!40000 ALTER TABLE `simas_encuesta` DISABLE KEYS */;
INSERT INTO `simas_encuesta` VALUES (1,'2010-11-01',1,'jose peroes','','Pedrito',1,1,1,2),(2,'2010-11-18',1,'yelba alfaro','','yelbita',1,2,2,3);
/*!40000 ALTER TABLE `simas_encuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simas_organizaciones`
--

DROP TABLE IF EXISTS `simas_organizaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `simas_organizaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `telefono` int(11) DEFAULT NULL,
  `fax` int(11) DEFAULT NULL,
  `celular` int(11) DEFAULT NULL,
  `direccion` longtext,
  `correo_electronico` varchar(75) DEFAULT NULL,
  `departamento_id` int(11) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `sitio_web` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `simas_organizaciones_779a4ea6` (`departamento_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simas_organizaciones`
--

LOCK TABLES `simas_organizaciones` WRITE;
/*!40000 ALTER TABLE `simas_organizaciones` DISABLE KEYS */;
INSERT INTO `simas_organizaciones` VALUES (1,'Metaleros',NULL,NULL,NULL,'','',NULL,'',''),(2,'personal',NULL,NULL,NULL,'','',NULL,'','');
/*!40000 ALTER TABLE `simas_organizaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simas_recolector`
--

DROP TABLE IF EXISTS `simas_recolector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `simas_recolector` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simas_recolector`
--

LOCK TABLES `simas_recolector` WRITE;
/*!40000 ALTER TABLE `simas_recolector` DISABLE KEYS */;
INSERT INTO `simas_recolector` VALUES (1,'Carlos Rocha');
/*!40000 ALTER TABLE `simas_recolector` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simas_tenencia`
--

DROP TABLE IF EXISTS `simas_tenencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `simas_tenencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parcela` int(11) NOT NULL,
  `solar` int(11) NOT NULL,
  `dueno` int(11) NOT NULL,
  `encuesta_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `simas_tenencia_1de70ac4` (`encuesta_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simas_tenencia`
--

LOCK TABLES `simas_tenencia` WRITE;
/*!40000 ALTER TABLE `simas_tenencia` DISABLE KEYS */;
INSERT INTO `simas_tenencia` VALUES (1,1,1,1,2);
/*!40000 ALTER TABLE `simas_tenencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'simas','0001_initial','2010-11-18 20:11:29'),(2,'indicador02','0001_initial','2010-11-18 20:12:08'),(3,'indicador05','0001_initial','2010-11-18 20:12:12'),(4,'indicador06','0001_initial','2010-11-18 20:12:17'),(5,'indicador07','0001_initial','2010-11-18 20:12:23'),(6,'indicador08','0001_initial','2010-11-18 20:12:28'),(7,'indicador09','0001_initial','2010-11-18 20:12:31'),(8,'indicador10','0001_initial','2010-11-18 20:12:37'),(9,'indicador11','0001_initial','2010-11-18 20:12:41'),(10,'indicador12','0001_initial','2010-11-18 20:12:49'),(11,'indicador13','0001_initial','2010-11-18 20:12:53'),(12,'indicador14','0001_initial','2010-11-18 20:12:58'),(13,'indicador15','0001_initial','2010-11-18 20:13:04'),(14,'indicador16','0001_initial','2010-11-18 20:13:08'),(15,'indicador17','0001_initial','2010-11-18 20:13:12'),(16,'indicador18','0001_initial','2010-11-18 20:13:20'),(17,'indicador19','0001_initial','2010-11-18 20:13:26'),(18,'indicador20','0001_initial','2010-11-18 20:13:30'),(19,'indicador01','0001_initial','2010-11-18 22:21:41');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2010-11-22 14:40:54
