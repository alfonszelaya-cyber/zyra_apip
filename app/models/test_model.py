from sqlalchemy import Column, Integer, String
from app.db.base import Base

class TestModel(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
