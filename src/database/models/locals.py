from database.connection import db


class Locals(db.Model):
    __tablename__ = "locals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(
        db.Enum("stadium", "bar", "home", "others", name="local_type_enum")
    )
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
