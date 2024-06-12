from flask import Blueprint
from controllers.competitions import CompetitionsController

competitions = Blueprint("competitions", __name__, url_prefix="/competitions")
competitionsController = CompetitionsController()


competitions.add_url_rule(
    "/", view_func=competitionsController.list, methods=["GET"]
)
competitions.add_url_rule(
    "/<int:id>", view_func=competitionsController.index, methods=["GET"]
)
competitions.add_url_rule(
    "/<int:id>", view_func=competitionsController.update, methods=["PUT"]
)
competitions.add_url_rule(
    "/<int:id>", view_func=competitionsController.delete, methods=["DELETE"]
)
competitions.add_url_rule(
    "/", view_func=competitionsController.create, methods=["POST"]
)
