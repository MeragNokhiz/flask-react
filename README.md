Flask - React - App:
__________________________

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

DataBase: (Install Docker) & Run a PostGreSQL Cointainer:

        docker run --name postgresql-container -p 5432:5432 -e POSTGRES_PASSWORD=somePassword -d postgres

or Run for docker-compose.yml: 

        docker-compose up -d

To get in the PostgrasCLI:

        docker exec -it 94f4bb9788fd bash

        psql -U postgres

 Quit   \q

Run PgAdmin

Config: If import in app.py is buggy add in .vscode/settings.json::

        "python.pythonPath": "/path/to/your/venv/bin/python"

Installing and Configuring Flask-Migrate
