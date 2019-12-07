
-- How to modify global_settings in Django
-- /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/django
-- —> conf
-- —> global_settings.py
-- 1. modify DATABASE
-- 2. modify TIME_ZONE = 'America/New_York'

-- create a new user & role
CREATE USER main_user SUPERUSER PASSWORD 'password';

SET ROLE main_user;

-- create 2 db, called: others & songs
-- Others db: stores Musician, Downloads, Listener tables; others_schema.songstable foreign table, which references Songstable in the other db.
-- Songs db: stores Songstable table


CREATE DATABASE others;
CREATE DATABASE songs;
\c songs main_user
CREATE SCHEMA songs_schema;
CREATE TABLE songs_schema.songstable (
	sid char(100) primary key,
	mid char(100),
	name char(100),
	published timestamptz,
	dl_count integer check (dl_count>0),
	last_dl timestamptz
);
\c others main_user
CREATE EXTENSION postgres_fdw;
CREATE SERVER songs_server 
    FOREIGN DATA WRAPPER postgres_fdw
    OPTIONS (host 'localhost', dbname 'songs', port '5432');
CREATE USER MAPPING FOR main_user 
    SERVER songs_server
    OPTIONS (user 'main_user', password 'password');
CREATE SCHEMA others_schema;        
CREATE FOREIGN TABLE others_schema.songstable(
	sid char(100) not null,
	mid char(100),
	name char(100),
	published timestamptz,
	dl_count integer,
	last_dl timestamptz
) SERVER songs_server OPTIONS (schema_name 'songs_schema', table_name 'songstable');
SELECT * FROM others_schema.songstable;


create table Musician (
	mid char(100) primary key,
	name char(100)
);


create table Listeners (
	lid char(100) primary key,
	sid char(100) --allow this to be null. Need to write a Trigger: when song deleted, sid within a Listener entry is deleted (becomes NUL). DO NOT delete the Listeners entry
);


create table Downloads(
	state boolean not null,
	did char(100) primary key,
	sid char(100) not null,  --Need to write Trigger: when song deleted, ENTIRE Download entry is deleted. 
	mid char(100) references Musician(mid) on delete cascade
);



--- Unsure how to proceed: attempted to write Trigger but dont' know how to pass input parameter. 
-- i.e. unsure how to acquire the value of entry being deleted from the foreign table.
-- possible workaround that's very very inefficient: make additional table to store the value of entry about to be deleted
-- i.e. use BEFORE DELETE trigger



CREATE OR REPLACE FUNCTION delete_from_downloads(sid char) RETURNS TRIGGER AS  -- but how the fuck to get the sid?????
$BODY$
BEGIN
    delete from Downloads
    where Downloads.sid== sid 
END;
$BODY$
language plpgsql;




CREATE TRIGGER trig_delete_from_downloads
     before delete on songstable
     FOR EACH ROW
     EXECUTE PROCEDURE delete_from_downloads();


