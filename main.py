import json

from flask import Flask, request

from DBHandler import DBHandler
from ResponseModel import ResponseModel

app = Flask(__name__)


@app.route('/students', methods=['POST','PUT','DELETE','GET'])
def students():
    print(request.json)
    response = ResponseModel()

    try:
        if request.method == 'POST':
            response = addStudent(request.json['data'])
        elif request.method == 'GET':
            response = getStudent(request.json['data'])


    except Exception as e:
        print(e)

    return json.dumps(response.__dict__)


def getStudent(_idE):
    if _idE == 'all':
        response = DBHandler().obtenerEstudiantes()
    else:
        pass

    return response

def addStudent(estudiante):
    response = DBHandler().insertarEstudiante(estudiante)
    return response





if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')