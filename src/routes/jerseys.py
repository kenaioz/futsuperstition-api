from flask import Blueprint
from controllers.jerseys import JerseysController

jerseys = Blueprint("jerseys", __name__, url_prefix="/jerseys")
jerseysController = JerseysController()


# Definindo as rotas de forma semelhante ao Node.js
jerseys.add_url_rule("/", view_func=jerseysController.list, methods=["GET"])
jerseys.add_url_rule(
    "/<int:id>", view_func=jerseysController.get, methods=["GET"]
)
jerseys.add_url_rule(
    "/new", view_func=jerseysController.create, methods=["POST"]
)
