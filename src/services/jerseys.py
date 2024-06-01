from src.database.models.jerseys import Jersey


class JerseysService:
    def listAll(self):
        jerseys = Jersey.query.all()
        jerseys_dict = [jersey.as_dict() for jersey in jerseys]
        return jerseys_dict
