-- Criação do banco de dados
CREATE DATABASE ENADE;

-- Utilização do banco de dados
USE ENADE;

-- Criação da tabela TipoQuestao
CREATE TABLE TipoQuestao (
    idTipoQuestao INT PRIMARY KEY,
    nomeTipoQuestao VARCHAR(45)
);

-- Criação da tabela TipoUsuario
CREATE TABLE TipoUsuario (
    idTipoUsuario INT PRIMARY KEY,
    nomeTipoUsuario VARCHAR(9)
);

-- Criação da tabela Prova
CREATE TABLE Prova (
    idProva INT PRIMARY KEY,
    dataProva DATE
);

-- Criação da tabela Usuario
CREATE TABLE Usuario (
    idUsuario INT PRIMARY KEY,
    nome VARCHAR(45),
    email VARCHAR(255),
    senha VARCHAR(255),
    TipoUsuario_idTipoUsuario INT
);

-- Criação da tabela Questao
CREATE TABLE Questao (
    idQuestao INT PRIMARY KEY,
    descricaoQuestao VARCHAR(45),
    alternativaA VARCHAR(45),
    alternativaB VARCHAR(45),
    alternativaC VARCHAR(45),
    alternativaD VARCHAR(45),
    alternativaE VARCHAR(45),
    questaoCorreta CHAR(1),
    estadoQuestao TINYINT,
    TipoQuestao_idTipoQuestao INT
);

-- Criação da tabela Prova_has_Questao
CREATE TABLE Prova_has_Questao (
    Prova_idProva INT,
    Questao_idQuestao INT
);

-- Criação da tabela Resultado
CREATE TABLE Resultado (
    idResultado INT PRIMARY KEY,
    valorObtido DOUBLE,
    Usuario_idUsuario INT,
    Prova_idProva INT
);
