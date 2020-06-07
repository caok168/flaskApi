# coding:utf8
from flask import Blueprint
inference = Blueprint("inference", __name__)
import app.inference.api
