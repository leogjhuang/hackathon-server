from flask import jsonify
from app import app
from app.database import db
from app.models import User, Skill


@app.route('/users', methods=['GET'])
def get_users():
    """
    Get a list of all users
    """
    users = User.query.all()
    return jsonify([user.serialize() for user in users])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get information about a specific user
    """
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.serialize())


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id, name, company, email, phone, skills):
    """
    Update information about a specific user
    """
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    # Update properties if they are not None
    if name is not None:
        user.name = name
    if company is not None:
        user.company = company
    if email is not None:
        user.email = email
    if phone is not None:
        user.phone = phone
    if skills is not None:
        # Add new skills to the database and update rating
        for skill in skills:
            skill = Skill.query.filter_by(skill=skill['skill']).first()
            if skill is None:
                skill = Skill(**skill)
                db.session.add(skill)
            user.skills.append(skill)
    # Commit the changes
    db.session.commit()
    return jsonify(user.serialize())
