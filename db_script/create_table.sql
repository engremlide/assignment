CREATE TABLE borrow 
(
 transactionid serial not null,
 customerid serial not null,
 cdno serial not null, 
 payment int not null,
 PRIMARY KEY(transactionid) 
);

CREATE TABLE surrender 
(
 transactionid serial not null,
 customerid serial not null,
 cdno serial not null, 
 penalty int not null,
 PRIMARY KEY(transactionid)
);

CREATE TABLE customer
(
customerid serial  not null, 
lastname varchar(32) NOT NULL,
firstname varchar(32) ,
middlename varchar(32) ,
address varchar(64) ,
age int,
gender char(6),
mobile varchar(16) ,
PRIMARY KEY(customerid)
);

CREATE TABLE typename
(
 typenamedisk char(3) not null, 
 primary key (typenamedisk)
);

CREATE TABLE category
(
 categoryname varchar(32) not null,
 primary key (categoryname)
);

CREATE TABLE casting
(
castname varchar(60) not null,
primary key (castname)
);

CREATE TABLE penalty
(
 penaltyval numeric not null,
 primary key (penaltyval)
);

CREATE TABLE no_of_days
(
 days int not null,
 primary key (days)
);

CREATE TABLE price
(
 priceval numeric not null, 
 primary key (priceval)
);

CREATE TABLE cd
(
 cdno serial not null,
 title varchar(32) not null,
 year_release integer not null,
 typename char(3) not null,
 categoryname varchar(32) not null,
 castname varchar(60),
 priceval numeric not null,
 no_of_days int not null,
 penaltyval numeric not null, 
 primary key (cdno),
 Unique (cdno,title,year_release),
 Foreign Key (typename) references typename (typenamedisk),
 Foreign Key (categoryname) references category (categoryname),
 Foreign Key (castname) references casting (castname),
 Foreign Key (priceval) references price (priceval),
 Foreign Key (no_of_days) references no_of_days (days),
 Foreign Key (penaltyval) references penalty (penaltyval)
);


 