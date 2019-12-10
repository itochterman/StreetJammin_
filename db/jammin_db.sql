/* Create our database */
CREATE DATABASE jammin_db CHARACTER SET utf8;

/* Setup permissions for the server */
CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON jammin_db.* TO 'root'@'localhost';
