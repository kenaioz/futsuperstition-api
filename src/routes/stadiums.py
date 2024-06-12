from flask import Blueprint
from controllers.stadiums import StadiumsController

stadiums = Blueprint("stadiums", __name__, url_prefix="/stadiums")
stadiumsController = StadiumsController()


stadiums.add_url_rule("/", view_func=stadiumsController.list, methods=["GET"])
stadiums.add_url_rule(
    "/<int:id>", view_func=stadiumsController.index, methods=["GET"]
)
stadiums.add_url_rule(
    "/<int:id>", view_func=stadiumsController.update, methods=["PUT"]
)
stadiums.add_url_rule(
    "/", view_func=stadiumsController.create, methods=["POST"]
)
