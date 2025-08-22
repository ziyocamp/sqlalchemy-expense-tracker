from datetime import datetime
import enum
from sqlalchemy import (
    Table, Column,
    Integer, String, DateTime, Enum as SqlEnum, Float, CheckConstraint, ForeignKey
)
from app.database import metadata_obj


class Category(enum.Enum):
    food = "Ovqatlanish"
    transport = "Transport"
    clothes = "Kiyim"
    rent = "Ijara"
    communal = "Kamunal"
    other = "Boshqa"


users = Table(
    'users',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String(length=64), nullable=False, unique=True),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now)
)

expenses = Table(
    'expenses',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('category', SqlEnum(Category), default=Category.other, nullable=False),
    Column('amount', Float, CheckConstraint("amount >= 0"), nullable=False),
    Column('user_id', Integer, ForeignKey("users.id"), nullable=False),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now)
)
