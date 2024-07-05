from flask import jsonify
from services.dashboard import DahboardService

dahboardService = DahboardService()


class DashboardController:
    def JerseysDashboard(self):
        jerseys = dahboardService.JerseysDashboardData()
        return jsonify(jerseys), 200

    def TeamsDashboard(self):
        return

    def LocalsDashboard(self):
        return

    def StadiumsDashboard(self):
        return

    def CompetitionsDashboard(self):
        return
