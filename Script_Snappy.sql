create database snappy;
use snappy;

create table mesa(
	id_mesa int not null primary key auto_increment,
    numero_mesa int not null
);

create table comestible(
	id_comestible int not null primary key auto_increment,
    nombre_comesttible varchar(50) not null,
    precio_comestible int not null
);

create table bebestible(
	id_bebestible int not null primary key auto_increment,
    nombre_bebestible varchar(50) not null,
    precio_bebestible int not null
);

create table venta(
	id_venta int not null primary key  auto_increment,
    id_mesa int not null,
    total int,
    constraint fk_id_mesa foreign key(id_mesa) references mesa(id_mesa)
);

drop table venta;


insert into mesa values(1, 1);
insert into mesa values(2, 2);
insert into mesa values(3, 3);
insert into mesa values(4, 4);

insert into comestible values(1, 'Pescado Frito', 7500);
insert into comestible values(2, 'Bistec a lo pobre', 8000);
insert into comestible values(3, 'Cazuela de Vacuno', 5500);
insert into comestible values(4, 'Paila Marina', 6000);

insert into bebestible values(1, 'Coca-Cola', 600);
insert into bebestible values(2, 'Cerveza Kross', 1500);
insert into bebestible values(3, 'Vino Tinto Santa Rita', 8000);
insert into bebestible values(4, 'Pisco Sour', 5000);

select * from venta;

truncate table venta;