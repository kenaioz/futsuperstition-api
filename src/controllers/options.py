from flask import jsonify, request
from services.options import OptionsService

optionsServices = OptionsService()


class OptionsController:
    def listJerseys(self):
        jerseys = optionsServices.listAllJerseysOptions()
        return jsonify(jerseys), 200

    def listTeams(self):
        teams = optionsServices.listAllTeamsOptions()
        return jsonify(teams), 200

    def listLocals(self):
        locals = optionsServices.listAllLocalsOptions()
        return jsonify(locals), 200

    def listStadiums(self):
        stadiums = optionsServices.listAllStadiumsOptions()
        return jsonify(stadiums), 200

    def listCompetitions(self):
        competitions = optionsServices.listAllCompetitionsOptions()
        return jsonify(competitions), 200
