from flask import jsonify, request
from services.competitions import CompetitionsService

competitionsService = CompetitionsService()


class CompetitionsController:
    def list(self):
        competitions = competitionsService.listAll()
        return jsonify(competitions), 200

    def index(self, id):
        competition = competitionsService.indexById(id)
        return jsonify(competition), 200

    def create(self):
        data = request.get_json()
        new_competition = competitionsService.createCompetition(data)
        return jsonify(new_competition), 201

    def update(self, id):
        data = request.get_json()
        updated_competition = competitionsService.updateCompetition(id, data)
        return jsonify(updated_competition), 200
