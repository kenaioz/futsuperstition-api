from flask import abort

from database.connection import db
from src.database.models.teams import Teams


class TeamsService:
    def listAll(self):
        teams = Teams.query.all()
        teams_dict = [team.as_dict() for team in teams]

        return teams_dict

    def indexById(self, id):
        team = Teams.query.get(id)

        if team is None:
            abort(404, description="Team not found")

        team_dict = team.as_dict()

        return team_dict

    def createTeam(self, data):
        new_team = Teams(
            name=data.get("name"),
            country=data.get("country"),
            city=data.get("city"),
        )

        db.session.add(new_team)
        db.session.commit()

        return new_team.as_dict()

    def updateTeam(self, id, data):
        team = Teams.query.get(id)

        if team is None:
            abort(404, description="Team not found")

        team.name = data.get("name", team.name)
        team.country = data.get("country", team.country)
        team.city = data.get("city", team.city)
        db.session.commit()

        return team.as_dict()
