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
        new_local = localsService.createLocal(data)
        return jsonify(new_local), 201

    def update(self, id):
        data = request.get_json()
        updated_local = localsService.updateLocal(id, data)
        return jsonify(updated_local), 200

    def delete(self, id):
        message = localsService.deleteLocal(id)
        return jsonify(message), 200
