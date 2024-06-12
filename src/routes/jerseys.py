from flask import Blueprint
from controllers.jerseys import JerseysController

jerseys = Blueprint("jerseys", __name__, url_prefix="/jerseys")
jerseysController = JerseysController()


jerseys.add_url_rule("/", view_func=jerseysController.list, methods=["GET"])
jerseys.add_url_rule(
    "/<int:id>", view_func=jerseysController.index, methods=["GET"]
)
jerseys.add_url_rule(
    "/<int:id>", view_func=jerseysController.update, methods=["PUT"]
)
jerseys.add_url_rule("/", view_func=jerseysController.create, methods=["POST"])
