<<<<<<< HEAD
models/base_model.py!/usr/bin/python3
"""
0x00. AirBnB clone - The console
City module
"""
from models.base_model import BaseModel
=======
#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
>>>>>>> 09fbc4501e62544f8fa5efde4b7a0da1805751fd


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
                      ForeignKey("states.id", ondelete="CASCADE"),
                      nullable=False)
    places = relationship(
        "Place",
        cascade="all",
        backref=backref("cities", cascade="all"),
        passive_deletes=True)
    # TODO: we need single_parent=True here?
