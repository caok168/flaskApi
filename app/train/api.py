from . import train
from flask import json, request, jsonify
from app.models import Label
from app import db


@train.route("/")
def home():
    return "home"


def listToJson(lst):
    import json
    import numpy as np
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, indent=2, ensure_ascii=False)  # json转为string
    return str_json


@train.route("/label", methods=["GET"])
def get_label_list():
    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        labels = Label.query.all()
        datas = []
        for item in labels:
            data = {}
            data["name"] = item.name
            data["type"] = item.type
            datas.append(data)

        res["data"] = datas

    except Exception as e:
        res["code"] = 10000
        res["message"] = str(e)

    return jsonify(res)


@train.route("/label/<int:id>", methods=["GET"])
def get_label(id):
    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        labels = Label.query.all()
        data = {}
        for item in labels:
            if id == item.id:
                data["name"] = item.name
                data["type"] = item.type
                break

        res["data"] = data

    except Exception as e:
        res["code"] = 10000
        res["message"] = str(e)

    return jsonify(res)


@train.route("/label/<int:id>", methods=["PUT"])
def update_label(id):
    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        label = Label.query.filter_by(id=id).first()
        label.name = request.json['name']
        label.type = request.json['type']
        db.session.add(label)
        db.session.commit()

    except Exception as e:
        res["code"] = 10000
        res["message"] = str(e)

    return jsonify(res)


@train.route("/label/<int:id>", methods=["DELETE"])
def delete_label(id):
    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        label = Label.query.filter_by(id=id).first()
        db.session.delete(label)
        db.session.commit()

    except Exception as e:
        res["code"] = 10000
        res["message"] = str(e)

    return jsonify(res)


@train.route("/label", methods=["POST"])
def add_label():
    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        name = request.json['name']
        type = request.json['type']
        label = Label(
            name=name,
            type=type
        )
        db.session.add(label)
        db.session.commit()

    except Exception as e:
        res["code"] = 10000
        res["message"] = str(e)

    return jsonify(res)


