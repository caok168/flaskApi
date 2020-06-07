# coding:utf8
from flask import Blueprint
train = Blueprint("train", __name__)
import app.train.api
