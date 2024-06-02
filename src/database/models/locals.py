from database.connection import db


class Locals(db.Model):
    __tablename__ = "locals"

    category = db.Column(db.Enum("stadium", "other", name="local_type_enum"))

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
