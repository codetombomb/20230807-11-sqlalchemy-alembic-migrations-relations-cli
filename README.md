# 20230807-11-sqlalchemy-alembic-migrations-relations-cli

## Review

- Questions
  - What is an ORM?
    - [ORM Visualization](https://www.figma.com/file/Udbuyi0ezpGhxNPL6qmWrK/ORM-Visual?type=whiteboard&node-id=0%3A1&t=n1rntyz68uDGdvge-1)
  - What is a Python module?
  - What is a Python package?
  - What is `PyPi`?
    - [The Python Package Index (PyPI) is a repository of software for the Python programming language.](<https://pypi.org/#:~:text=The%20Python%20Package%20Index%20(PyPI)%20is%20a%20repository%20of%20software%20for%20the%20Python%20programming%20language>)
  - What is `pipenv`
    - Pipenv docs: [What is pipenv?](<https://pipenv.pypa.io/en/latest/#:~:text=Pipenv%20is%20a%20Python%20virtualenv%20management%20tool%20that%20supports%20a%20multitude%20of%20systems%20and%20nicely%20bridges%20the%20gaps%20between%20pip%2C%20python%20(using%20system%20python%2C%20pyenv%20or%20asdf)%20and%20virtualenv.>)
  - What is a virtual environment?
    - [Virtual Environment Visualization](https://www.figma.com/file/ej3qo3FLhS78eipGApigmH/Virtual-Environments-Visualization?type=whiteboard&node-id=0%3A1&t=n1rntyz68uDGdvge-1)

## Where are we going?

- CLI todo list - [Demo CLI Repo](https://github.com/codetombomb/taskmaster-5000)

## SWBATs

- [x] Create a Virtual Env with `pipenv` and install dependencies
- [x] Initialize migrations with `alembic`
- [x] Configure `alembic` to work with our DB
- [x] Create a schema and migrate the DB
- [ ] Use migrations to:
  - create/drop tables
  - rename tables
  - add/remove columns
  - rename columns
  - modify constraints

## Evolving The DB Through Migrations

Create the following migrations:
```python
# Migration 1: Change user table to users

# Migration 2: Add email column
# Add a new column called "email" to the "user" table.

# Migration 3: Add unique constraint on username
# Add a unique constraint on the "username" column in the "user" table.

# - error
# - solution - https://stackoverflow.com/questions/30378233/sqlite-lack-of-alter-support-alembic-migration-failing-because-of-this-solutio
    # - add render_as_batch=True to the env.py file 
    # downgrade the DB to base
    # redo all migrations
    # test with seeds

# Migration 4: Add created_at and updated_at timestamps
# Add "created_at" and "updated_at" timestamp columns to the "user" table to track creation and update times.

# func - https://docs.sqlalchemy.org/en/14/core/functions.html#selected-known-functions
# server_default - https://docs.sqlalchemy.org/en/14/orm/persistence_techniques.html#fetching-server-generated-defaults
# onupdate - https://docs.sqlalchemy.org/en/14/core/constraints.html#on-update-and-on-delete

# Test updated_at in seeds file
# __repr__ method:
    # def __repr__(self):
    #     return f"\n<User "\
    #         + f"id={self.id}," \
    #         + f"username={self.username}," \
    #         + f"email={self.email}," \
    #         + f"created_at={self.create_at}," \
    #         + f"updated_at={self.updated_at}," \


# Migration 5: Add phone number column
# Add a new column called "phone_number" to the "user" table to store user contact phone numbers.
```
