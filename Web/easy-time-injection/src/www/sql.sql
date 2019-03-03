create database blind_time_injection;
use blind_time_injection;
create table users (
id int(6) unsigned auto_increment primary key,
name varchar(20) not null,
email varchar(30) not null,
salary int(8) unsigned not null );

INSERT INTO users VALUES(1,'Lucia','Lucia@aurora.com',3000);
INSERT INTO users VALUES(2,'Danny','Danny@aurora.com',4500);
INSERT INTO users VALUES(3,'Alina','Alina@aurora.com',2700);
INSERT INTO users VALUES(4,'Jameson','Jameson@aurora.com',10000);
INSERT INTO users VALUES(5,'Allie','Allie@aurora.com',6000);

create table Notice (flag varchar(50) not null);
INSERT INTO Notice VALUES('ACTF{Time_B1ind_InJect1oN}');