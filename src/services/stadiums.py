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
        new_stadium = Stadiums(
            name=data.get("name"),
            country=data.get("country"),
            city=data.get("city"),
        )

        db.session.add(new_stadium)
        db.session.commit()

        return new_stadium.as_dict()

    def updateStadium(self, id, data):
        stadium = Stadiums.query.get(id)

        if stadium is None:
            abort(404, description="Jersey not found")

        stadium.name = data.get("name", stadium.name)
        stadium.year = data.get("year", stadium.year)
        stadium.category = data.get("category", stadium.category)
        stadium.manufacturer = data.get("manufacturer", stadium.manufacturer)
        db.session.commit()

        return stadium.as_dict()

    def deleteStadium(self, id):
        stadium = Stadiums.query.get(id)
        if stadium is None:
            abort(404, description="Stadium not found")
        db.session.delete(stadium)
        db.session.commit()
        return {"message": "Stadium deleted"}
