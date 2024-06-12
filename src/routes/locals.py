from flask import Blueprint
from controllers.locals import LocalsController

locals = Blueprint("locals", __name__, url_prefix="/locals")
localsController = LocalsController()


locals.add_url_rule("/", view_func=localsController.list, methods=["GET"])
locals.add_url_rule(
    "/<int:id>", view_func=localsController.index, methods=["GET"]
)
locals.add_url_rule(
    "/<int:id>", view_func=localsController.update, methods=["PUT"]
)
locals.add_url_rule(
    "/<int:id>", view_func=localsController.delete, methods=["DELETE"]
)
locals.add_url_rule("/", view_func=localsController.create, methods=["POST"])
