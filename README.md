# sqlalchemy2strawberry
A simple tool to convert SQLAlchemy models to Strawberry types

## Installation
```
pip install sqlalchemy2strawberry
```
In case you use poetry:
```
poetry add sqlalchemy2strawberry
```

## Usage
```python
from sqlalchemy2strawberry import sqlalchemy2strawberry
# other imports

# code for other sqlalchemy stuff

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


UserType = sqlalchemy2strawberry(User)

@strawberry.type
class Query:
    users: List[UserType]
```
