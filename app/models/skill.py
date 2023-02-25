from app.database import db


class Skill(db.Model):
    # Define the table name
    __tablename__ = 'skills'

    # Define the columns
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    # Define the many-to-many relationship with the User model
    users = db.relationship('User', secondary='user_skills', back_populates='skills')

    # Define the string representation of the model
    def __repr__(self):
        return '<Skill %r>' % self.skill

    # Define the serialization method
    def serialize(self):
        return {
            'skill': self.skill,
            'rating': self.rating
        }


class UserSkill(db.Model):
    # Define the table name
    __tablename__ = 'user_skills'

    # Define the columns
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)

    # Define the string representation of the model
    def __repr__(self):
        return '<UserSkill %r>' % self.id

    # Define the serialization method
    def serialize(self):
        return {
            'user_id': self.user_id,
            'skill_id': self.skill_id
        }
