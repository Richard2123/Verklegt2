drop table if exists items;
drop table if exists sales;
drop table if exists users;
drop table if exists people;
drop table if exists location;

create table location (
	zip int not null,
	lname varchar(50) not null,
	primary key(zip)
);

create table people (
	uid integer not null,
	pname varchar(100),
	zip integer,
	primary key(uid),
	foreign key(zip) references location(zip)
 );

create table users (
	uid integer not null,
	uname varchar(15) not null,
	email varchar(50) not null,
	password varchar(200) not null,
	primary key(uid, uname, email),
	foreign key(uid) references people(uid)
);

create table items (
	iid integer not null,
	uid integer not null,
    item_name varchar(50),
	start_bid float not null,
	condition varchar(20),
	description varchar(350),
	main_image varchar(100),
	image2 varchar(100),
	image3 varchar(100),
	image4 varchar(100),
	image5 varchar(100),
	primary key(iid),
	foreign key(uid) references people(uid)
);

create table sales (
	iid integer not null,
	sell_price float not null,
	highest_bid float not null,
	primary key(iid),
	foreign key(iid) references items(iid)
);
