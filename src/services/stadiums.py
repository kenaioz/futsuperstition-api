from flask import abort

from database.connection import db
from src.database.models.stadiums import Stadiums


class StadiumsService:
    def listAll(self):
        stadiums = Stadiums.query.all()
        stadiums_dict = [stadium.as_dict() for stadium in stadiums]

        return stadiums_dict

    def indexById(self, id):
        stadium = Stadiums.query.get(id)

        if stadium is None:
            abort(404, description="Stadium not found")

        stadium_dict = stadium.as_dict()

        return stadium_dict

    def createStadium(self, data):

        return data

    def updateStadium(self, id, data):

        return data
