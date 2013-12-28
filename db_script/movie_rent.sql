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

INSERT INTO price VALUES(10);
INSERT INTO price VALUES(15);
INSERT INTO price VALUES(20);
INSERT INTO price VALUES(25);
INSERT INTO price VALUES(30);
INSERT INTO price VALUES(35);
INSERT INTO price VALUES(40);


INSERT INTO penalty VALUES(5);
INSERT INTO penalty VALUES(10);
INSERT INTO penalty VALUES(20);
INSERT INTO penalty VALUES(40);
INSERT INTO penalty VALUES(75);
INSERT INTO penalty VALUES(100);


INSERT INTO no_of_days VALUES(1);
INSERT INTO no_of_days VALUES(2);
INSERT INTO no_of_days VALUES(3);
INSERT INTO no_of_days VALUES(4);
INSERT INTO no_of_days VALUES(5);
INSERT INTO no_of_days VALUES(6);


INSERT INTO customer VALUES(1, 'llantos','orven', 'rakista', 'iligan city', 40, 'male', 09175543241 );
INSERT INTO customer VALUES(2, 'madarang','susa', 'ortega', 'cebu city', 41, 'female', 09175543242 );
INSERT INTO customer VALUES(3, 'pilongo','adonis maynard', 'balboa', 'pagadian city', 30, 'male', 09175663241 );
INSERT INTO customer VALUES(4, 'balbutin','shirley', 'iligan', 'ozamis city', 34, 'female', 09286241516 );


INSERT INTO cd VALUES(1, 'white house down', 2012, 'dvd', 'action', 'bruce willis', 40, 1, 75 );
INSERT INTO cd VALUES(2, 'oblivion', 2011, 'dvd', 'friction', 'tom cruse', 40, 2, 40 );
INSERT INTO cd VALUES(3, 'world war z', 2013, 'dvd', 'horror', 'brad pitt', 40, 2, 20 );


INSERT INTO category VALUES('lovestory');
INSERT INTO category VALUES('friction');
INSERT INTO category VALUES('action');
INSERT INTO category VALUES('adventure');
INSERT INTO category VALUES('animation');
INSERT INTO category VALUES('biography');
INSERT INTO category VALUES('comedy');
INSERT INTO category VALUES('crime');
INSERT INTO category VALUES('drama');
INSERT INTO category VALUES('horror');


INSERT INTO casting VALUES('angel locsin');
INSERT INTO casting VALUES('brad pitt ');
INSERT INTO casting VALUES('bruce willis');
INSERT INTO casting VALUES('derrick ramsey');
INSERT INTO casting VALUES('tom cruse');


INSERT INTO typename VALUES('cd');
INSERT INTO typename VALUES('dvd');

