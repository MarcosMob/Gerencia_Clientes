create database mecanica;
use mecanica;

create table clientes(
	CPF varchar(15),
    NOME varchar(50),
    TELEFONE varchar(15),
    Endereco varchar(100),
    placa varchar(10),
    obs varchar(300)
);

update clientes set telefone = '' where cpf = '';
ALTER TABLE clientes
ADD PRIMARY KEY (CPF);
delete from clientes where telefone = '';
select * from clientes;