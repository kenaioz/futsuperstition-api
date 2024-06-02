from database.connection import db


class Jerseys(db.Model):
    __tablename__ = "jerseys"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    year = db.Column(db.String(4))
    category = db.Column(
        db.Enum(
            "oficial", "torcida", "retro", "other", name="jersey_type_enum"
        )
    )
    manufacturer = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
