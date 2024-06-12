from flask import abort

from database.connection import db
from src.database.models.locals import Locals


class LocalsService:
    def listAll(self):
        locals = Locals.query.all()
        locals_dict = [local.as_dict() for local in locals]

        return locals_dict

    def indexById(self, id):
        local = Locals.query.get(id)

        if local is None:
            abort(404, description="Local not found")

        local_dict = local.as_dict()

        return local_dict

    def createLocal(self, data):
        new_local = Locals(
            name=data.get("name"),
            category=data.get("category"),
        )

        db.session.add(new_local)
        db.session.commit()

        return new_local.as_dict()

    def updateLocal(self, id, data):
        local = Locals.query.get(id)

        if local is None:
            abort(404, description="Local not found")

        local.name = data.get("name", local.name)
        local.category = data.get("category", local.category)
        db.session.commit()

        return local.as_dict()

    def deleteLocal(self, id):
        local = Locals.query.get(id)
        if local is None:
            abort(404, description="Local not found")
        db.session.delete(local)
        db.session.commit()
        return {"message": "Local deleted"}
