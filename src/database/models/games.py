from database.connection import db


class Games(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    home_team_goals = db.Column(db.Integer)
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    away_team_goals = db.Column(db.Integer)
    result = db.Column(db.Enum("win", "draw", "loss", name="result_enum"))
    stadium_id = db.Column(db.Integer, db.ForeignKey("stadiums.id"))
    date = db.Column(db.Date)
    jersey_id = db.Column(db.Integer, db.ForeignKey("jerseys.id"))
    competition_id = db.Column(db.Integer, db.ForeignKey("competitions.id"))
    competition_round = db.Column(db.String(255))
    local_id = db.Column(db.Integer, db.ForeignKey("locals.id"))
    local_type = db.Column(db.Enum("stadium", "other", name="local_type_enum"))
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now()
    )

    home_team = db.relationship("Teams", foreign_keys=[home_team_id])
    away_team = db.relationship("Teams", foreign_keys=[away_team_id])
    stadium = db.relationship("Stadiums")
    jersey = db.relationship("Jerseys")
    competition = db.relationship("Competitions")
    local = db.relationship("Locals")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
