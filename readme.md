# book-libary 
jeg har et proskjekt med login og create account og man skal skrive hvilket bok man vil ha og hvordan man skal oversette det

for å bruke proskjekte så må man først clone proskjekt

`git clone https://github.com/Knut123456/Oppdrag---Utvikling.git`

etterpå skrive dette i terminal som installere alle libary jeg har brukt for dette proskjekte

`pip install -r requirements.txt`

dette vil laste ned alt man vil ha 



endre alt til det du vil

i sql filen i sql folderen kopier du og adder den til mariadb
når du har laget database og endre det over meg så kan du bare runne sql.py som vil lage tabeller

i sql foldern create user så må du ha username i plassene som her nede og password burde du ha i plassen her ned du kan velge hva slags passord og brukernavn
```
    CREATE USER 'username'@'%' IDENTIFIED BY 'password';    
    GRANT INSERT, SELECT ON BokLibary.* TO 'username'@'%';
    FLUSH PRIVILEGES;
```
så kjører du det i mariadb

create a secret.py i flask folderen
skrive denne kode
in username and password du brukte i create user sql fil
```
    database = {
        "host": "ip din til mariadb",
        "user": "username",
        "password": "password", 
        "database": "BokLibary",
        "port": 3306 
    }
```



