from flask import jsonify, request
from services.stadiums import StadiumsService

stadiumsService = StadiumsService()


class StadiumsController:
    def list(self):
        stadiums = stadiumsService.listAll()
        return jsonify(stadiums), 200

    def index(self, id):
        stadium = stadiumsService.indexById(id)
        return jsonify(stadium), 200

    def create(self):
        data = request.get_json()
        new_stadium = stadiumsService.createStadium(data)
        return jsonify(new_stadium), 201

    def update(self, id):
        data = request.get_json()
        updated_stadium = stadiumsService.updateStadium(id, data)
        return jsonify(updated_stadium), 200

    def delete(self, id):
        message = stadiumsService.deleteStadium(id)
        return jsonify(message), 200
