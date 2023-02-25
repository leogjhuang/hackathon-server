from app.database import db


class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Skill %r>' % self.skill

    def serialize(self):
        return {
            'id': self.id,
            'skill': self.skill,
            'rating': self.rating,
            'user_id': self.user_id
        }
