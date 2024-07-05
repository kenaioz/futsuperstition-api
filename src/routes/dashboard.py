from flask import Blueprint
from controllers.dashboard import DashboardController

dashboard = Blueprint("dashboard", __name__, url_prefix="/dashboard")
dashboardController = DashboardController()


dashboard.add_url_rule(
    "/jerseys", view_func=dashboardController.JerseysDashboard, methods=["GET"]
)
# dashboard.add_url_rule(
#     "/teams", view_func=dashboardController.listTeams, methods=["GET"]
# )
# dashboard.add_url_rule(
#     "/locals", view_func=dashboardController.listLocals, methods=["GET"]
# )
# dashboard.add_url_rule(
#     "/stadiums", view_func=dashboardController.listStadiums, methods=["GET"]
# )
# dashboard.add_url_rule(
#     "/competitions",
#     view_func=dashboardController.listCompetitions,
#     methods=["GET"],
# )
