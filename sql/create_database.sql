CREATE DATABASE Oppdrag_UtviklingOppdrag_Utvikling 

CREATE USER 'the name you want'@'%' IDENTIFIED BY 'the password you want';
GRANT INSERT, SELECT ON the name you want.* TO 'the name you want'@'%';

FLUSH PRIVILEGES;