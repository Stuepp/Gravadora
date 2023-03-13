create table musico(
	nro_registro int primary key,
	endereço varchar(200),
	telefone varchar(25) not null
);

create table instrumento(
	id_instrumento int primary key,
	nome varchar(50) not null
);

create table disco(
	id_disco int primary key,
	titulo varchar(75),
	formato varchar(75),
	data date,
	fk_musico int,
	fk_banda int,
	foreign key(fk_musico) references musico,
	foreign key(fk_banda) references banda
);

create table produtor(
	id_produtor int primary key
	nome varchar(50) not null,
);

create table musica(
	id_musica int primary key
	titulo varchar(50) not null,
	autores varchar(150)
);

create table banda(
	id_banda int primary key
	nome varchar(75) not null
);

create table own(
	id_own int primary key,
	fk_musico int,
	fk_banda int,
	foreign key(fk_musico) references musico,
	foreign key(fk_banda) references banda
);

create table toca(
	id_toca int primary key,
	fk_musico int,
	fk_instrumento int,
	foreign key(fk_musico) references musico,
	foreign key(fk_instrumento) references instrumento
);

create table produz(
	id_produz int primary key,
	fk_disco int,
	fk_produtor int,
	foreign key(fk_disco) references disco,
	foreign key(fk_produtor) references produtor
);

create table aparece(
	id_aparece int primary key,
	fk_disco int,
	fk_musica int,
	foreign key(fk_disco) references disco,
	foreign key(fk_musica) references musica
);

create table esta(
	id_esta int primary key,
	fk_musico int,
	fk_banda int,
	foreign key(fk_musico) references musico,
	foreign key(fk_banda) references banda
);

create table participa(
	id_participa int primary key,
	fk_own int,
	fk_musica int,
	foreign key(fk_own) references own,
	foreign key(fk_musica) references musica
);