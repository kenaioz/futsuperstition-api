from flask import abort

from database.connection import db
from src.database.models.competitions import Competitions


class CompetitionsService:
    def listAll(self):
        competitions = Competitions.query.all()
        competitions_dict = [
            competition.as_dict() for competition in competitions
        ]

        return competitions_dict

    def indexById(self, id):
        competition = Competitions.query.get(id)

        if competition is None:
            abort(404, description="Competition not found")

        competition_dict = competition.as_dict()

        return competition_dict

    def createCompetition(self, data):
        new_competition = Competitions(
            name=data.get("name"),
            category=data.get("category"),
            rounds=data.get("rounds"),
        )

        db.session.add(new_competition)
        db.session.commit()

        return new_competition.as_dict()

    def updateCompetition(self, id, data):
        competition = Competitions.query.get(id)

        if competition is None:
            abort(404, description="Jersey not found")

        competition.name = data.get("name", competition.name)
        competition.year = data.get("category", competition.year)
        db.session.commit()

        return competition.as_dict()
