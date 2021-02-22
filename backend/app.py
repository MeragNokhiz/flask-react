from flask import Flask
from flask_cors import CORS
from urllib.request import Request, urlopen
import xmltodict
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/ninja"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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


@app.route('/hello')
def home():
    #serve(app, host="0.0.0.0", port=8080)
    return {'result': "Hello oooooo"}

@app.route('/api')
def api():
    file = urlopen('https://s3.eu-central-1.amazonaws.com/jobninja-backend-feeds-prod/81856f12-e317-4d51-a203-1884aa31ca64/jobs_feed.xml')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data

@app.route('/apiC')
def apiC():
    file = urlopen('https://random-data-api.com/api/cannabis/random_cannabis?size=2&is_xml=true')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    return data

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)

    