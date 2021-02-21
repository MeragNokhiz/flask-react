Flask - React - App:
__________________________

rootdirc:

        npm i

cd frontend

        npm i


cd backend

        pip3 install
        flask db migrate  

rootdirc:   

        npm start

__________________________

Setup:

FrontEnd:

        mkdir frontend
        cd frontend 
        npx create-react-app .

Add in package.json:

         "proxy": "http://localhost:5000"


BackEnd: 

        mkdir backend
        cd backend 

        python3 -m venv venv

        pip3 freeze > requirements.txt

        source venv/bin/activate

        (venv) $ pip install flask python-dotenv
        (venv) $ pip install -U flask-cors

DataBase: Run a PostGreSQL Docker:

        docker run --name postgresql-container -p 5432:5432 -e POSTGRES_PASSWORD=somePassword -d postgres

or Run for docker-compose.yml: 

        docker-compose up -d

How to get in the PostgrasCLI:

        docker exec -it 94f4bb9788fd bash

        psql -U postgres

        Quit:   \q

Run PgAdmin

Config: If import in app.py is buggy add in .vscode/settings.json::

        "python.pythonPath": "/path/to/your/venv/bin/python"

Init & Migrate DB with Flask-Migrate (flask db)

        flask db init
        flask db migrate  

        
