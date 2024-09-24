# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Running the Project
_For development run the serve command (what you execute):_
```bash
$ flask run
```

_For production using gunicorn (what heroku executes):_
```bash
$ gunicorn wsgi:app
```

# Database Migrations
If changes to the models are made, the database must be'migrated' so that it can be synced with the new models.

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask db --help
```
# A Student Conduct Tracker for Flask Application 
This flask app provides a command line interface for staff to anonymously provide reports on a particular student, providing the student with a score out of 10 and a provide extra details in the comment.

# Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```

# User Commands
_Creating a student:_
```bash
$ flask reviewer add_student <firstname> <lastname>
```

_Finding student(s) by full name:_
```bash
$ flask reviewer find_student <firstname> <lastname>
```

_List all students:_
```bash
$ flask reviewer list_students
```

_Get review(s) for a student by ID:
```bash
$ flask reviewer get_reviews <student_id>
```

# Troubleshooting
Ensure you run `flask init` before running any of the listed commands

# Credits
 The template for the CLI was provided by Nicholas Mendez and Tristan Leid, the repository for the original template can be found [here](https://github.com/uwidcit/flaskmvc)