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
- [ ] Initialize migrations with `alembic`
- [ ] Configure `alembic` to work with our DB
- [ ] Create a schema and migrate the DB
- [ ] Use migrations to:

  - create/drop tables
  - rename tables
  - add/remove columns
  - rename columns
  - modify constraints

---  

## Initializing Migrations

- In the top-level directory, run: `alembic init migrations`
    - This will generate a folder named `migrations`. You can change `migrations` to something else if you would like. In the Alembic documentation, they use `alembic init alembic`. [Link](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)
- This command will generate the following file structure:

```bash
yourproject/
    migrations/
        env.py
        README
        script.py.mako
        versions/
```

### [Taking a look at the file structure](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment:~:text=The%20directory%20includes%20these%20directories/files%3A)

- **`alembic`** - This directory lives within your application’s source tree and is the home of the migration environment.
- **`env.py`** - This is a Python script that is run whenever the alembic migration tool is invoked. It contains instructions to configure and generate a SQLAlchemy engine, procure a connection from that engine, and then invoke the migration engine using the connection for database connectivity.
- **`README`** - Included with the various environment templates, should have something informative.
- **`script.py.mako`** - This is a Mako template file which is used to generate new migration scripts. It helps generate new files within the **`versions/`** directory.
- **`versions/`** - This directory holds the individual version scripts. The files here represent the changes to your app's database over time.

## Configuration

Before we can use `SQLAlchemy` or `alembic` to create a database, we need to configure a couple of things first:

- In the `alembic.ini` configuration file, we need to define the connection string for the SQLAlchemy engine.
    - Find the line (around 58) that says `sqlalchemy.url`
    - Set the value to `sqlite:///name_of_your_db.db`
        - Change `name_of_your_db` to a name that best suits the kind of date that you will be storing.
        - This also defines the path to the directory in which we want our db to be created.
- In the `migrations/env.py` file, we need to define the `target_metadata` variable. Find the following lines of code in the `migrations/env.py` file:

```python
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
```

And change it to this:

```python
from models import Base
target_metadata = Base.metadata
```

- Explanation
    - `from models import Base`
        
        We have not defined `models` or `Base` yet but, we will add the following code to the `models.py` file next:
        
        ```python
        from sqlalchemy.ext.declarative import declarative_base
        
        Base = declarative_base()
        ```
        
        - This code defined the Base class that all of our models will inherit from. This gives alembic a way to know about the state of our schemas (models) and compare it to the DB. If there is a difference, alembic will detect those differences and generate the necessary script in the migration files to bring the DB in sync with the schema.
    - `target_metadata = Base.metadata`
        - The line **`target_metadata = Base.metadata`** sets the variable  **`target_metadata`** to hold information about the database tables and structure defined in the SQLAlchemy models.
        - The **`metadata`** attribute of the **`Base`** class is like a record keeper that stores all the information about the model classes (tables) and their columns. It keeps track of what tables exist in the application and how they are structured.
        - So, when you write **`Base.metadata`**, you are referring to this record-keeping tool, and by setting **`target_metadata`** to it, you can use this information to manage and compare the database structure during migrations with Alembic.
