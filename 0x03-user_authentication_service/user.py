#!/usr/bin/env python3
"""
This module defines the User model for the SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Define the base class for all models
Base = declarative_base()

# Define the User model
class User(Base):
    """ Represents user object/table
    """    
    __tablename__ = 'users'  # Name of the table

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
