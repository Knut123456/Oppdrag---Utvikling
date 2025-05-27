DROP DATABASE IF EXISTS bok-libary;
CREATE DATABASE bok-libary;

CREATE USER 'hva du vil'@'%' IDENTIFIED BY 'passord til database';
GRANT INSERT, SELECT ON bok-libary.* TO 'hva du vil'@'%';

FLUSH PRIVILEGES;