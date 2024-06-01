from flask import jsonify, request
from services.jerseys import JerseysService

jerseysServices = JerseysService()


class JerseysController:
    def list(self):
        jerseys = jerseysServices.listAll()
        return jerseys

    def get(self, id):
        return jsonify({"id": id})

    def create(self):
        data = request.get_json()
        return jsonify(data), 201
