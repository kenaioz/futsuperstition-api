from flask import abort

from database.connection import db
from src.database.models.jerseys import Jersey


class JerseysService:
    def listAll(self):
        jerseys = Jersey.query.all()
        jerseys_dict = [jersey.as_dict() for jersey in jerseys]

        return jerseys_dict

    def indexById(self, id):
        jersey = Jersey.query.get(id)

        if jersey is None:
            abort(404, description="Jersey not found")

        jersey_dict = jersey.as_dict()

        return jersey_dict

    def createJersey(self, data):
        new_jersey = Jersey(name=data.get("name"), year=data.get("year"))

        db.session.add(new_jersey)
        db.session.commit()

        return new_jersey.as_dict()

    def updateJersey(self, id, data):
        jersey = Jersey.query.get(id)

        if jersey is None:
            abort(404, description="Jersey not found")

        jersey.name = data.get("name", jersey.name)
        jersey.year = data.get("year", jersey.year)
        db.session.commit()

        return jersey.as_dict()
