import json

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# Import the models here to avoid circular imports
from app.models import User, Skill


# Initialize the database
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


# Retrieve the data from the URL
def load_data(app):
    with open('app/users.json') as f:
        users_data = json.load(f)

    # Create the database
    with app.app_context():
        for user_data in users_data:
            kwargs = {key: user_data[key] for key in user_data if key != 'skills'}
            user = User(**kwargs)
            db.session.add(user)

            # Add the skills
            for skill_data in user_data['skills']:
                skill = Skill.query.filter_by(skill=skill_data['skill']).first()
                if skill is None:
                    skill = Skill(**skill_data)
                    db.session.add(skill)
                user.skills.append(skill)

        # Commit the changes
        db.session.commit()
