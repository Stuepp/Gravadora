-- d
create table own(
    id int primary key,
    fk_musico int,
    fk_banda int,
);
--entities
create table musico(
    id int primary key, -- fk de own
    name varchar(50),
    phone varchar(20),
    address varchar(150),
    foreign key(id) references own
);
create table instrumento(
    id int primary key,
    name varchar(50)
);
create table banda(
    id int primary key, -- e fk de own
    name varchar(50),
    foreign key(id) references own
);
create table produtor(
    id int primary key,
    name varchar(50)
);
create table disco(
    id int primary key,
    titulo varchar(50),
    data date, -- yyyy-mm-dd
    format varchar(50),
    fk_produtor int,
    fk_musico int,
    fk_banda int,
    foreign key(fk_produtor) references produtor,
    foreign key(fk_musico) references musico,
    foreign key(fk_banda) references banda
);
create table musica(
    id int primary key,
    titulo varchar(50),
    autores varchar(800),
    song_file varchar(200),
    img_file varchar(200)
);
-- relations
create table participa( -- bandas/artistas que participaram na música
    id int primary key,
    fk_own int,
    fk_musica int,
    foreign key(fk_own) references own,
    foreign key(fk_musica) references musica
);
create table aparece( -- musicas que aparecem no disco
    id int primary key,
    fk_musica int,
    fk_disco int,
    foreign key(fk_musica) references musica,
    foreign key(fk_disco) references disco
);
create table esta( -- música está dentro de uma ou mais bandas e uma banda pode ter mais de um músico
    id int primary key,
    fk_musico int,
    fk_banda int,
    foreign key(fk_musico) references musico,
    foreign key(fk_banda) references banda
);
create table toca( -- músico toca um ou mais instrumento, e instrumentos são tocados por um ou mais músicos
    id int primary key,
    fk_musico int,
    fk_instrumento int,
    foreign key(fk_musico) references musico,
    foreign key(fk_instrumento) references instrumento
);