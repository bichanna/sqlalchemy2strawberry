from sqlalchemy2strawberry import __version__, sqlalchemy2strawberry
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


def test_version():
    assert __version__ == '0.0.1'

