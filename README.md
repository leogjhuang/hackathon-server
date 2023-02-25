# Hackathon Server

This backend server is intended to be used for hackathon management. It is a simple REST API that allows you to create and manage hackathon attendees and their skills. Built with [Flask](https://flask.palletsprojects.com) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com), it uses [SQLite](https://www.sqlite.org) as a database and [Docker](https://www.docker.com) for containerization.

## Project Structure

The project is structured as follows:

- `app/` - Contains the Flask application and all of its components
  - `__init__.py` - Initializes the Flask application
  - `database.py` - Initializes the database
  - `models/` - Contains the database models
    - `__init__.py` - Initializes the database models
    - `user.py` - Defines the `User` model
    - `skill.py` - Defines the `Skill` model
  - `routes/` - Contains the API routes
    - `__init__.py` - Initializes the API routes
    - `user.py` - Defines the `/user` API routes
    - `skill.py` - Defines the `/skill` API routes
  - `users.json` - Contains the initial users to be added to the database

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose)
- [Python 3](https://www.python.org)

### Installation

1. Clone the repository

```bash
git clone https://github.com/leogjhuang/hackathon-server.git
```

2. Build and run the Docker container

```bash
docker-compose up --build
```

3. Navigate to `http://localhost:5000`

## Usage

### API Routes

#### Users

- `GET /users` - Returns a list of all users
- `GET /users/<id>` - Returns the user with the specified ID
- `PUT /users/<id>` - Updates the user with the specified ID

#### Skills

- `GET /skills/<min_frequency>/<max_frequency>` - Returns a list of all skills with a frequency between the specified minimum and maximum values

## License

Distributed under the MIT License. See `LICENSE` for more information.
