from flask import jsonify
from app import app
from app.models import User


@app.route('/skills/<int:min_frequency>/<int:max_frequency>', methods=['GET'])
def get_skills(min_frequency, max_frequency):
    """
    Get a list of all skills with a frequency between min_frequency and max_frequency
    """
    users = User.query.all()
    skills = {}
    for user in users:
        for skill in user.skills:
            if skill.skill not in skills:
                skills[skill.skill] = 0
            skills[skill.skill] += 1
    return jsonify([skill for skill in skills if skills[skill] >= min_frequency and skills[skill] <= max_frequency])
