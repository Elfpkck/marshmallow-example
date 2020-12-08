from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['API_TITLE'] = 'My API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ma.sqlite3'
api = Api(app)
db = SQLAlchemy(app)


class Doc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text(2000), nullable=False)

    def __repr__(self):
        return self.type
