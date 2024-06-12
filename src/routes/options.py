from flask import Blueprint
from controllers.options import OptionsController

options = Blueprint("options", __name__, url_prefix="/options")
optionsController = OptionsController()


options.add_url_rule(
    "/jerseys", view_func=optionsController.listJerseys, methods=["GET"]
)
options.add_url_rule(
    "/teams", view_func=optionsController.listTeams, methods=["GET"]
)
options.add_url_rule(
    "/locals", view_func=optionsController.listLocals, methods=["GET"]
)
options.add_url_rule(
    "/stadiums", view_func=optionsController.listStadiums, methods=["GET"]
)
options.add_url_rule(
    "/competitions",
    view_func=optionsController.listCompetitions,
    methods=["GET"],
)
