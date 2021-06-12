-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: mydbpaem
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `acesso_permitido`
--

DROP TABLE IF EXISTS `acesso_permitido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `acesso_permitido` (
  `id_acesso_permitido` int NOT NULL,
  `id_solicitacao_acesso` int NOT NULL,
  `temperatura` float DEFAULT NULL,
  `hora_entrada` time DEFAULT NULL,
  `hora_saida` time DEFAULT NULL,
  PRIMARY KEY (`id_acesso_permitido`),
  KEY `fk_acesso_permitido_solicitacao_acesso1_idx` (`id_solicitacao_acesso`),
  CONSTRAINT `fk_acesso_permitido_solicitacao_acesso1` FOREIGN KEY (`id_solicitacao_acesso`) REFERENCES `solicitacao_acesso` (`id_solicitacao_acesso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `acesso_permitido`
--

LOCK TABLES `acesso_permitido` WRITE;
/*!40000 ALTER TABLE `acesso_permitido` DISABLE KEYS */;
/*!40000 ALTER TABLE `acesso_permitido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campus`
--

DROP TABLE IF EXISTS `campus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campus` (
  `id_campus` int NOT NULL AUTO_INCREMENT,
  `ano_fundacao` date DEFAULT NULL,
  `nome` varchar(45) NOT NULL,
  `direcao_id_direcao` int DEFAULT NULL,
  PRIMARY KEY (`id_campus`),
  KEY `fk_campus_direcao1_idx` (`direcao_id_direcao`),
  CONSTRAINT `fk_campus_direcao1` FOREIGN KEY (`direcao_id_direcao`) REFERENCES `direcao` (`id_direcao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campus`
--

LOCK TABLES `campus` WRITE;
/*!40000 ALTER TABLE `campus` DISABLE KEYS */;
/*!40000 ALTER TABLE `campus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coordenacao`
--

DROP TABLE IF EXISTS `coordenacao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coordenacao` (
  `id_coordenacao` int NOT NULL AUTO_INCREMENT,
  `data_entrada` date NOT NULL,
  `curso_id_curso` int NOT NULL,
  `docente_id_docente` int NOT NULL,
  PRIMARY KEY (`id_coordenacao`),
  KEY `fk_coordenacao_curso1_idx` (`curso_id_curso`),
  KEY `fk_coordenacao_docente1_idx` (`docente_id_docente`),
  CONSTRAINT `fk_coordenacao_curso1` FOREIGN KEY (`curso_id_curso`) REFERENCES `curso` (`id_curso`),
  CONSTRAINT `fk_coordenacao_docente1` FOREIGN KEY (`docente_id_docente`) REFERENCES `docente` (`id_docente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coordenacao`
--

LOCK TABLES `coordenacao` WRITE;
/*!40000 ALTER TABLE `coordenacao` DISABLE KEYS */;
/*!40000 ALTER TABLE `coordenacao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curso`
--

DROP TABLE IF EXISTS `curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curso` (
  `id_curso` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `data_fundacao` date DEFAULT NULL,
  `campus_id_campus` int NOT NULL,
  PRIMARY KEY (`id_curso`),
  KEY `fk_curso_campus1_idx` (`campus_id_campus`),
  CONSTRAINT `fk_curso_campus1` FOREIGN KEY (`campus_id_campus`) REFERENCES `campus` (`id_campus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curso`
--

LOCK TABLES `curso` WRITE;
/*!40000 ALTER TABLE `curso` DISABLE KEYS */;
/*!40000 ALTER TABLE `curso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direcao`
--

DROP TABLE IF EXISTS `direcao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `direcao` (
  `id_direcao` int NOT NULL AUTO_INCREMENT,
  `data_entrada` date NOT NULL,
  `docente_id_docente` int DEFAULT NULL,
  PRIMARY KEY (`id_direcao`),
  KEY `fk_direcao_docente1_idx` (`docente_id_docente`),
  CONSTRAINT `fk_direcao_docente1` FOREIGN KEY (`docente_id_docente`) REFERENCES `docente` (`id_docente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcao`
--

LOCK TABLES `direcao` WRITE;
/*!40000 ALTER TABLE `direcao` DISABLE KEYS */;
/*!40000 ALTER TABLE `direcao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discente`
--

DROP TABLE IF EXISTS `discente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discente` (
  `id_discente` int NOT NULL AUTO_INCREMENT,
  `matricula` varchar(45) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `cpf` varchar(15) DEFAULT NULL,
  `entrada` varchar(6) NOT NULL,
  `semestre` int DEFAULT NULL,
  `endereco` varchar(45) DEFAULT NULL,
  `grupo_risco` tinyint DEFAULT NULL,
  `status_covid` tinyint DEFAULT NULL,
  `status_permissao` tinyint DEFAULT NULL,
  `curso_id_curso` int NOT NULL,
  `usuario_id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_discente`),
  UNIQUE KEY `matricula_UNIQUE` (`matricula`),
  KEY `fk_discente_curso1_idx` (`curso_id_curso`),
  KEY `fk_discente_usuario1_idx` (`usuario_id_usuario`),
  CONSTRAINT `fk_discente_curso1` FOREIGN KEY (`curso_id_curso`) REFERENCES `curso` (`id_curso`),
  CONSTRAINT `fk_discente_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discente`
--

LOCK TABLES `discente` WRITE;
/*!40000 ALTER TABLE `discente` DISABLE KEYS */;
/*!40000 ALTER TABLE `discente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina`
--

DROP TABLE IF EXISTS `disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina` (
  `id_disciplina` int NOT NULL,
  `codigo_sigaa` varchar(45) DEFAULT NULL,
  `semestre` varchar(20) DEFAULT NULL,
  `curso_id_curso` int NOT NULL,
  PRIMARY KEY (`id_disciplina`),
  KEY `fk_disciplina_curso1_idx` (`curso_id_curso`),
  CONSTRAINT `fk_disciplina_curso1` FOREIGN KEY (`curso_id_curso`) REFERENCES `curso` (`id_curso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina`
--

LOCK TABLES `disciplina` WRITE;
/*!40000 ALTER TABLE `disciplina` DISABLE KEYS */;
/*!40000 ALTER TABLE `disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disciplina_has_discente`
--

DROP TABLE IF EXISTS `disciplina_has_discente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disciplina_has_discente` (
  `disciplina_id_disciplina` int NOT NULL,
  `discente_id_discente` int NOT NULL,
  `data` date NOT NULL,
  PRIMARY KEY (`disciplina_id_disciplina`,`discente_id_discente`),
  KEY `fk_disciplina_has_discente_disciplina1_idx` (`disciplina_id_disciplina`),
  KEY `fk_disciplina_has_discente_discente1_idx` (`discente_id_discente`),
  CONSTRAINT `fk_disciplina_has_discente_discente1` FOREIGN KEY (`discente_id_discente`) REFERENCES `discente` (`id_discente`),
  CONSTRAINT `fk_disciplina_has_discente_disciplina1` FOREIGN KEY (`disciplina_id_disciplina`) REFERENCES `disciplina` (`id_disciplina`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disciplina_has_discente`
--

LOCK TABLES `disciplina_has_discente` WRITE;
/*!40000 ALTER TABLE `disciplina_has_discente` DISABLE KEYS */;
/*!40000 ALTER TABLE `disciplina_has_discente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docente`
--

DROP TABLE IF EXISTS `docente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `docente` (
  `id_docente` int NOT NULL AUTO_INCREMENT,
  `siape` varchar(45) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `status_covid` tinyint DEFAULT NULL,
  `status_afastamento` tinyint DEFAULT NULL,
  `escolaridade` varchar(45) DEFAULT NULL,
  `situacao` varchar(45) DEFAULT NULL,
  `usuario_id_usuario` int DEFAULT NULL,
  `curso_id_curso` int DEFAULT NULL,
  PRIMARY KEY (`id_docente`),
  UNIQUE KEY `siape_UNIQUE` (`siape`),
  KEY `fk_docente_curso1_idx` (`curso_id_curso`) /*!80000 INVISIBLE */,
  KEY `fk_docente_usuario1_idx` (`usuario_id_usuario`),
  CONSTRAINT `fk_docente_curso1` FOREIGN KEY (`curso_id_curso`) REFERENCES `curso` (`id_curso`),
  CONSTRAINT `fk_docente_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docente`
--

LOCK TABLES `docente` WRITE;
/*!40000 ALTER TABLE `docente` DISABLE KEYS */;
/*!40000 ALTER TABLE `docente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `docente_has_disciplina`
--

DROP TABLE IF EXISTS `docente_has_disciplina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `docente_has_disciplina` (
  `docente_siape` varchar(45) NOT NULL,
  `disciplina_id_disciplina` int NOT NULL,
  `data` date NOT NULL,
  PRIMARY KEY (`docente_siape`,`disciplina_id_disciplina`),
  KEY `fk_docente_has_disciplina_disciplina1_idx` (`disciplina_id_disciplina`),
  KEY `fk_docente_has_disciplina_docente1_idx` (`docente_siape`),
  CONSTRAINT `fk_docente_has_disciplina_disciplina1` FOREIGN KEY (`disciplina_id_disciplina`) REFERENCES `disciplina` (`id_disciplina`),
  CONSTRAINT `fk_docente_has_disciplina_docente1` FOREIGN KEY (`docente_siape`) REFERENCES `docente` (`siape`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `docente_has_disciplina`
--

LOCK TABLES `docente_has_disciplina` WRITE;
/*!40000 ALTER TABLE `docente_has_disciplina` DISABLE KEYS */;
/*!40000 ALTER TABLE `docente_has_disciplina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portaria`
--

DROP TABLE IF EXISTS `portaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `portaria` (
  `id_portaria` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `cpf` varchar(15) NOT NULL,
  `data_nascimento` date NOT NULL,
  `funcao` varchar(45) NOT NULL,
  `turno_trabalho` tinyint NOT NULL,
  `campus_id_campus` int NOT NULL,
  `usuario_id_usuario` int NOT NULL,
  PRIMARY KEY (`id_portaria`),
  UNIQUE KEY `cpf_UNIQUE` (`cpf`),
  KEY `fk_portaria_campus1_idx` (`campus_id_campus`),
  KEY `fk_portaria_usuario1_idx` (`usuario_id_usuario`),
  CONSTRAINT `fk_portaria_campus1` FOREIGN KEY (`campus_id_campus`) REFERENCES `campus` (`id_campus`),
  CONSTRAINT `fk_portaria_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portaria`
--

LOCK TABLES `portaria` WRITE;
/*!40000 ALTER TABLE `portaria` DISABLE KEYS */;
/*!40000 ALTER TABLE `portaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recurso_campus`
--

DROP TABLE IF EXISTS `recurso_campus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recurso_campus` (
  `id_recurso_campus` int NOT NULL AUTO_INCREMENT,
  `nome` text NOT NULL,
  `capacidade` int NOT NULL,
  `descricao` text NOT NULL,
  `inicio_horario_funcionamento` time DEFAULT NULL,
  `fim_horario_funcionamento` time DEFAULT NULL,
  `campus_id_campus` int NOT NULL,
  PRIMARY KEY (`id_recurso_campus`),
  KEY `fk_recurso_campus_campus1_idx` (`campus_id_campus`),
  CONSTRAINT `fk_recurso_campus_campus1` FOREIGN KEY (`campus_id_campus`) REFERENCES `campus` (`id_campus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recurso_campus`
--

LOCK TABLES `recurso_campus` WRITE;
/*!40000 ALTER TABLE `recurso_campus` DISABLE KEYS */;
/*!40000 ALTER TABLE `recurso_campus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserva_recurso_servidores`
--

DROP TABLE IF EXISTS `reserva_recurso_servidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserva_recurso_servidores` (
  `id_reserva_recurso_servidores` int NOT NULL AUTO_INCREMENT,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_final` time NOT NULL,
  `descricao` varchar(45) NOT NULL,
  `usuario_id_usuario` int NOT NULL,
  PRIMARY KEY (`id_reserva_recurso_servidores`,`data_fim`),
  KEY `fk_reserva_recurso_servidores_usuario1_idx` (`usuario_id_usuario`),
  CONSTRAINT `fk_reserva_recurso_servidores_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserva_recurso_servidores`
--

LOCK TABLES `reserva_recurso_servidores` WRITE;
/*!40000 ALTER TABLE `reserva_recurso_servidores` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserva_recurso_servidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solicitacao_acesso`
--

DROP TABLE IF EXISTS `solicitacao_acesso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitacao_acesso` (
  `id_solicitacao_acesso` int NOT NULL AUTO_INCREMENT,
  `id_recurso_campus` int NOT NULL,
  `para_si` tinyint NOT NULL,
  `data` date NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fim` time NOT NULL,
  `status_acesso` tinyint DEFAULT NULL COMMENT 'Esse campo será preenchido quando pelo usuário do tipo Técnico avaliar se o discente terá acesso ou não ao recurso do campus que deseja. Ex: Biblioteca, Sala Inteligente, Espaço de Estudos',
  `usuario_id_usuario` int DEFAULT NULL,
  `discente_id_discente` int NOT NULL,
  `fone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_solicitacao_acesso`),
  KEY `fk_solicitacao_acesso_recurso_campus1_idx` (`id_recurso_campus`),
  KEY `fk_solicitacao_acesso_usuario1_idx` (`usuario_id_usuario`),
  KEY `fk_solicitacao_acesso_discente1_idx` (`discente_id_discente`),
  CONSTRAINT `fk_solicitacao_acesso_discente1` FOREIGN KEY (`discente_id_discente`) REFERENCES `discente` (`id_discente`),
  CONSTRAINT `fk_solicitacao_acesso_recurso_campus1` FOREIGN KEY (`id_recurso_campus`) REFERENCES `recurso_campus` (`id_recurso_campus`),
  CONSTRAINT `fk_solicitacao_acesso_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitacao_acesso`
--

LOCK TABLES `solicitacao_acesso` WRITE;
/*!40000 ALTER TABLE `solicitacao_acesso` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitacao_acesso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tecnico`
--

DROP TABLE IF EXISTS `tecnico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tecnico` (
  `id_tecnico` int NOT NULL AUTO_INCREMENT,
  `siape` varchar(45) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `data_nascimento` date DEFAULT NULL,
  `cargo` varchar(45) DEFAULT NULL,
  `status_covid` tinyint DEFAULT NULL,
  `status_afastamento` tinyint DEFAULT NULL,
  `campus_id_campus` int NOT NULL,
  `usuario_id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_tecnico`),
  UNIQUE KEY `siape_UNIQUE` (`siape`),
  KEY `fk_tecnico_campus1_idx` (`campus_id_campus`),
  KEY `fk_tecnico_usuario1_idx` (`usuario_id_usuario`),
  CONSTRAINT `fk_tecnico_campus1` FOREIGN KEY (`campus_id_campus`) REFERENCES `campus` (`id_campus`),
  CONSTRAINT `fk_tecnico_usuario1` FOREIGN KEY (`usuario_id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tecnico`
--

LOCK TABLES `tecnico` WRITE;
/*!40000 ALTER TABLE `tecnico` DISABLE KEYS */;
/*!40000 ALTER TABLE `tecnico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `login` varchar(45) NOT NULL,
  `senha` text NOT NULL,
  `email` varchar(45) NOT NULL,
  `tipo` int NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf32;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-28 21:48:14
