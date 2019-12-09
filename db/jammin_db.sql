/* Create our database */
CREATE DATABASE jammin_db CHARACTER SET utf8;

/* Setup permissions for the server */
CREATE USER 'main_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON scalica.* TO 'appserver'@'localhost';