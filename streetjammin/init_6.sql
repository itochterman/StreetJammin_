-- create a new user & role
CREATE USER main_user SUPERUSER PASSWORD 'password';

SET ROLE main_user;

create database jammin_db;
\c jammin_db main_user

create table Musicians (
	mid char(100) primary key,
	name char(100)
);


CREATE TABLE Songs (
	sid char(100),
	mid char(100) references Musician(mid) on delete cascade,
	name char(100),
	published timestamptz,
	dl_count integer check (dl_count>0),
	last_dl timestamptz
	primary key (mid, sid)
);


create table Downloads(
	state boolean not null,
	mid char(100) references Musician(mid) on delete cascade,
	did char(100),
	sid char(100) references Songs(sid) on delete cascade,
	primary key (mid, sid, did)
);
