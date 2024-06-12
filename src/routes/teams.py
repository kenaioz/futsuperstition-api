from flask import Blueprint
from controllers.teams import TeamsController

teams = Blueprint("teams", __name__, url_prefix="/teams")
teamsController = TeamsController()


teams.add_url_rule("/", view_func=teamsController.list, methods=["GET"])
teams.add_url_rule(
    "/<int:id>", view_func=teamsController.index, methods=["GET"]
)
teams.add_url_rule(
    "/<int:id>", view_func=teamsController.update, methods=["PUT"]
)
teams.add_url_rule("/", view_func=teamsController.create, methods=["POST"])
