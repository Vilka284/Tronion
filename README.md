
1.Clone the code into a fresh folder.

2.Create a Virtual Environment and install Dependencies.
    
    $ virtualenv venv
    
Activated linux: 
    
    $ source venv/bin/activate

Win:
    
    > .\venv\scripts\activate
    
3.Install the project dependencies, which are listed in requirements.txt.
    
    (venv) $ pip install -r requirements.txt
    
4. Make sure you have installed up to date version of [PostgreSQL](https://www.postgresql.org/download/).
Before launching project you also have to configure database access. 
All you need to do it's **make .env file** and place this text into it:
```
DATABASE_HOST = "localhost"
DATABASE_USERNAME = "username of db owner"
DATABASE_PASSWORD = "password of db owner"
DATABASE_NAME = "tronion"
DATABASE_PORT = "5432"


SECRET_KEY = "create your secret key"
```
