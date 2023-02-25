from app.database import db


class User(db.Model):
    # Define the table name
    __tablename__ = 'users'

    # Define the columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)

    # Define the many-to-many relationship with the Skill model
    skills = db.relationship('Skill', secondary='user_skills', back_populates='users')

    # Define the string representation of the model
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'phone': self.phone,
            'skills': [skill.serialize() for skill in self.skills]
        }
