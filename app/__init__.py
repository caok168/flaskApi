# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
postgresql:
1. sudo apt install libpq-dev
2. pip3 install psyconpg2
"""

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@127.0.0.1:3306/test"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://lynxi:lynxi@127.0.0.1:5433/pca"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "1c0049e9387f42f2a5da2ec692f3c6d0"
app.debug = True

db = SQLAlchemy(app)

from app.inference import inference as inference_blueprint
from app.train import train as train_blueprint

app.register_blueprint(inference_blueprint, url_prefix='/inference')
app.register_blueprint(train_blueprint, url_prefix='/train')
