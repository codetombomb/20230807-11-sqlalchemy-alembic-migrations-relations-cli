from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    

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