import email
import string
from traceback import print_tb
from click import MissingParameter
from flask import Flask, jsonify, request
import os
import json
from app.services.json_handler import checkEmailExists, checkId, checkIsUpper, read_json, write_json
from app.exception.userException import EmailExistError, IsNumericError

FILEPATH = os.getenv("FILEPATH")
app = Flask(__name__)

@app.get("/user")
def getUser():
    data = read_json(FILEPATH)
    return jsonify(data), 200 

@app.post("/user")
def postUser():
    try:
        data = request.get_json()
        if "name" in data and "email" in data:
            name = data["name"]
            email = data["email"]
        else:
            return {"error": "faltam parametros"}, 405
        if(type(name) == str and type(email) == str):
            checkEmailExists(email)
            print(data)
            result = checkIsUpper(name, email)
            idUser = checkId()
            return write_json(FILEPATH, {"id": idUser,"name": result[0], "email": result[1]})
        else:
            return jsonify({"wrong fields":[{"name": str(type(data["name"]))[8:-2]}, {"email": str(type(data["email"]))[8:-2]}]}), 400
    except EmailExistError as e:
        return {"error": e.message}, e.status_code