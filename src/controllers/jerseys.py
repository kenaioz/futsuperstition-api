from flask import jsonify, request
from services.jerseys import JerseysService

jerseysServices = JerseysService()


class JerseysController:
    def list(self):
        jerseys = jerseysServices.listAll()
        return jsonify(jerseys), 200

    def index(self, id):
        jersey = jerseysServices.indexById(id)
        return jsonify(jersey), 200

    def create(self):
        data = request.get_json()
        new_jersey = jerseysServices.createJersey(data)
        return jsonify(new_jersey), 201

    def update(self, id):
        data = request.get_json()
        updated_jersey = jerseysServices.updateJersey(id, data)
        return jsonify(updated_jersey), 200
