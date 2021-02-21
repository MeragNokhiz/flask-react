from app import app, db
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import psycopg2 

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/ninja"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

conn = psycopg2.connect(database="ninja", user="postgres", password="postgres")


db.create_all()

class Ninja(db.Model):
    __tablename__ = 'ninja'

    id = db.Column(db.Integer, primary_key=True)
    firma = db.Column(db.String())
    volltext = db.Column(db.String())
    plz_arbeitsor = db.Column(db.Integer())
    arbeitsort = db.Column(db.String())

    def __init__(self, name, model, doors):
        self.firma = firma
        self.volltext = volltext
        self.plz_arbeitsor = plz_arbeitsor
        self.arbeitsort = arbeitsort


mirgrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()