from flask import jsonify
from app import app
from app.models import User


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
