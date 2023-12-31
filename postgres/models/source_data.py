# memory.py
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
import os
import sys
from ..database  import Base
class BaseModel(Base):
    __tablename__ = 'base'

    unique_id = Column(String, primary_key=True, comment='Unique identifier for each record.')
    name = Column(String, nullable=True, comment='Name of the user.')
    email = Column(String, nullable=True, comment='Email address of the user.')
    city = Column(String, nullable=True, comment='City where the user resides.')
    personality_description = Column(String, nullable=True, comment='Description of the user\'s personality.')
    hobbies = Column(String, nullable=True, comment='List of hobbies enjoyed by the user.')
    in_game_behavior = Column(String, nullable=True, comment='Description of the user\'s behavior in games.')
    backstory = Column(String, nullable=True, comment='Backstory associated with the user.')
    favorite_gaming_moment = Column(String, nullable=True, comment='Description of the user\'s favorite gaming moment.')
