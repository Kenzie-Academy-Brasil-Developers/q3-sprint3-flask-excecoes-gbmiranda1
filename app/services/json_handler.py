import json
from json import JSONDecodeError
import os
from app.exception.userException import EmailExistError

FILEPATH = os.getenv("FILEPATH")

def read_json(filepath: str) -> list:
    print(filepath)
    try:
        with open(filepath, "r") as json_file:
            return json.load(json_file)

    except JSONDecodeError:
        with open(filepath, "w") as file:
            json.dump({"data": []}, file)
        return {"data": []}

    except FileNotFoundError:
        os.mknod(filepath)
        with open(filepath, "w") as file:
            json.dump({"data": []}, file)

        return {"data": []}

    


def write_json(filepath: str, payload: dict):
    json_list = read_json(filepath)
    json_list["data"].append(payload)

    print(f"{json_list=}")

    with open(filepath, "w") as json_file:
        json.dump(json_list, json_file, indent=2)

        return payload

def checkEmailExists(email):
    data = read_json(FILEPATH)
    if len(data["data"]) > 0:
        for i in data["data"]:
            if email.lower() == i["email"]:
                raise EmailExistError

def checkIsUpper(name, email):
    nameSplit = name.split(" ")
    result = ""
    for i in range(0, len(nameSplit)):
        result += str(nameSplit[i][0].upper()) + nameSplit[i][1:] + " "
    return (result[0:-1], email.lower())

def checkId():
    data = read_json(FILEPATH)
    maior = 0
    for i in data["data"]:
        if maior < int(i["id"]):
            maior = int(i["id"])
    return maior+1