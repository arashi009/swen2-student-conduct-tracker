# Student Conduct Tracker Flask Application

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

A command-line interface for staff to provide reports on students, including a score out of 10 and detailed comments.

## Table of Contents
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Database Migrations](#database-migrations)
- [Initializing the Database](#initializing-the-database)
- [User Commands](#user-commands)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Features
- Add students to the database
- Find students by name
- Find staff by name
- List all students
- List all staff
- Add reviews for students
- Retrieve reviews for a specific student
- Retrieve reviews written by a specific staff member

## Dependencies
- Python 3.x
- pip3
- Packages listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-conduct-tracker.git
   cd student-conduct-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

For development:
```bash
flask run
```

For production (using gunicorn):
```bash
gunicorn wsgi:app
```

## Database Migrations

If you make changes to the models, sync the database using these commands:

```bash
flask db init
flask db migrate
flask db upgrade
```

For more options:
```bash
flask db --help
```

## Initializing the Database

When connecting to a fresh database or deploying on Heroku:

```bash
flask init
```

## User Commands

### Creating a student
```bash
flask reviewer add_student 
```

### Finding student(s) by full name
```bash
flask reviewer find_students
```

### Finding staff by full name
```bash
flask reviewer find_staff
```

### Listing all students
```bash
flask reviewer list_students
```

### Listing all staff
```bash
flask reviewer list_staff
```

### Get review(s) for a student by ID
```bash
flask reviewer get_student_reviews
```

### Get review(s) written by a staff member by username
```bash
flask reviewer get_staff_reviews
```

### Review a student
```bash
flask reviewer review_student
```

## Troubleshooting

Ensure you run `flask init` before running any of the listed commands.

## Credits

The template for the CLI was provided by Nicholas Mendez and Tristan Leid. The original template repository can be found [here](https://github.com/uwidcit/flaskmvc).

---