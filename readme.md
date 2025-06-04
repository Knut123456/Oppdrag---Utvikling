# book-libary 
jeg har et proskjekt med login og create account og man skal skrive hvilket bok man vil ha og hvordan man skal oversette det

for å bruke proskjekte så må man først clone proskjekt

`git clone https://github.com/Knut123456/Oppdrag---Utvikling.git`

etterpå skrive dette i terminal som installere alle libary jeg har brukt for dette proskjekte

ting du kan trenge og installere
[python](https://www.python.org/downloads/)
[mariadb](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.7.2&os=windows&cpu=x86_64&pkg=msi&mirror=dotsrc)
på linux kan du bare skrive sudo apt install mariadb

vis du vil kan du laste ned venv 

fra filen proskjekte kjøre
python -m venv venv 

for å aktivere venv på windeos
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1

# for linux 
source venv/bin/activate

`pip install -r requirements.txt`

dette vil laste ned alt man vil ha 

i linux ubuntu hvis du får noen problemer 
```
    sudo apt update
    sudo apt install libmariadb-dev-compat libmariadb-dev
    sudo apt install pkg-config
```
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
    SECRET_KEY = "heaoawdwadwakdæoangsuhdaøodlsmnfjdadiowaldaudsadgf8wapødjiwo"
```



