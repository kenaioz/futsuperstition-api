from flask import jsonify, request
from services.locals import LocalsService

localsService = LocalsService()


class LocalsController:
    def list(self):
        locals = localsService.listAll()
        return jsonify(locals), 200

    def index(self, id):
        local = localsService.indexById(id)
        return jsonify(local), 200

    def create(self):
        data = request.get_json()
        new_local = localsService.createJersey(data)
        return jsonify(new_local), 201

    def update(self, id):
        data = request.get_json()
        updated_local = localsService.updateJersey(id, data)
        return jsonify(updated_local), 200
