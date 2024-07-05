from sqlalchemy.orm import aliased
from sqlalchemy import func, case

from database.connection import db
from src.database.models.jerseys import Jerseys
from src.database.models.teams import Teams
from src.database.models.locals import Locals
from src.database.models.stadiums import Stadiums
from src.database.models.competitions import Competitions
from src.database.models.games import Games


class DahboardService:
    def JerseysDashboardData(self):

        # Query
        query = (
            db.session.query(
                Jerseys.id,
                Jerseys.name,
                Jerseys.year,
                func.count(Games.id).label("frequency"),
                func.sum(case((Games.result == "win", 1), else_=0)).label(
                    "wins"
                ),
                (
                    func.sum(case((Games.result == "win", 1), else_=0))
                    * 100
                    / func.count(Games.id)
                ).label("percentage"),
            )
            .join(Games, Jerseys.id == Games.jersey_id)
            .group_by(Jerseys.id, Jerseys.name, Jerseys.year)
            .order_by(
                (
                    (func.sum(case((Games.result == "win", 1), else_=0)) * 100)
                    / func.count(Games.id)
                ).desc()
            )
        )

        result = query.all()

        jersey_stats = [
            {
                "id": row.id,
                "name": row.name,
                "year": row.year,
                "frequency": row.frequency,
                "wins": row.wins,
                "percentage": int(row.percentage),
            }
            for row in result
        ]

        return jersey_stats

    def TeamsDashboardData(self):

        return

    def LocalsDashboardData(self):

        return

    def StadiumsDashboardData(self):

        return

    def CompetitionsDashboardData(self):

        return
