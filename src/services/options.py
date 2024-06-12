from flask import abort
from sqlalchemy import func, asc

from database.connection import db
from src.database.models.jerseys import Jerseys
from src.database.models.teams import Teams
from src.database.models.locals import Locals
from src.database.models.stadiums import Stadiums
from src.database.models.competitions import Competitions


class OptionsService:
    def listAllJerseysOptions(self):
        jerseys = Jerseys.query.with_entities(
            Jerseys.id,
            func.concat(Jerseys.name, " ", Jerseys.year).label("name"),
        ).all()

        return [{"id": jersey.id, "name": jersey.name} for jersey in jerseys]

    def listAllTeamsOptions(self):
        teams = Teams.query.with_entities(Teams.id, Teams.name).all()

        return [{"id": team.id, "name": team.name} for team in teams]

    def listAllLocalsOptions(self):
        locals = (
            Locals.query.with_entities(Locals.id, Locals.name)
            .order_by(asc(Locals.id))
            .all()
        )

        return [{"id": local.id, "name": local.name} for local in locals]

    def listAllStadiumsOptions(self):
        stadiums = Stadiums.query.with_entities(
            Stadiums.id, Stadiums.name
        ).all()

        return [
            {"id": stadium.id, "name": stadium.name} for stadium in stadiums
        ]

    def listAllCompetitionsOptions(self):
        competitions = Competitions.query.with_entities(
            Competitions.id, Competitions.name, Competitions.rounds
        ).all()

        return [
            {
                "id": competition.id,
                "name": competition.name,
                "rounds": competition.rounds,
            }
            for competition in competitions
        ]
