from flask import jsonify
from app import app
from app.database import db
from app.models import User, Skill


@app.route('/skills/<int:min_frequency>/<int:max_frequency>', methods=['GET'])
def get_skills(min_frequency, max_frequency):
    """
    Get a list of all skills with a frequency between min_frequency and max_frequency
    """
    skills = Skill.query.join(Skill.users).group_by(Skill.id).having(
        db.func.count(User.id) >= min_frequency,
        db.func.count(User.id) <= max_frequency
    ).all()
    return jsonify([skill.serialize() for skill in skills])
