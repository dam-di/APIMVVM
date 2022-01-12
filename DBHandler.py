
from pymongo import MongoClient

from ResponseModel import ResponseModel


class DBHandler(object):
    def __init__(self):
        self.db = self.conectar()
        self.collection = self.db.get_collection('estudiantes')


    def conectar(self):
        client = MongoClient(
            host = 'infsalinas.sytes.net:10450',
            serverSelectionTimeoutMS = 3000,
            username = 'profe2',
            password = 'abcd1234',
            authSource = 'profe2'
        )
        db = client.get_database('profe2')
        return db

    def obtenerEstudiantes(self):
        response = ResponseModel()
        try:
            listaEstudiantes = []
            coleccion = self.collection.find({})
            for estudiante in coleccion:
                listaEstudiantes.append(estudiante)

            response.resultOk = True
            response.data = str(listaEstudiantes)

        except Exception as e:
            print(e)

        return response

    def insertarEstudiante(self, estudiante):
        response = ResponseModel()
        try:
            self.collection.insert_one(estudiante)
            response.resultOk = True
            response.data = 'Estudiante insertado con exito'
        except Exception as e:
            print(e)

        return response