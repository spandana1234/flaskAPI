from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://spandana:spandanaabc@192.168.43.108/spandana_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Employee(db.Model):

    emp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emp_name = db.Column(db.String(70))
    email = db.Column(db.String(100))

    def __init__(self, emp_name, email):
        self.emp_name = emp_name
        self.email = email


db.create_all()


class EmpSchema(ma.Schema):
    class Meta:
        fields = ('emp_id', 'emp_name', 'email')
