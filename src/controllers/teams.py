from flask import jsonify, request
from services.teams import TeamsService

teamsService = TeamsService()


class TeamsController:
    def list(self):
        teams = teamsService.listAll()
        return jsonify(teams), 200

    def index(self, id):
        team = teamsService.indexById(id)
        return jsonify(team), 200

    def create(self):
        data = request.get_json()
        new_team = teamsService.createTeam(data)
        return jsonify(new_team), 201

    def update(self, id):
        data = request.get_json()
        updated_team = teamsService.updateTeam(id, data)
        return jsonify(updated_team), 200

    def delete(self, id):
        message = teamsService.deleteTeam(id)
        return jsonify(message), 200
