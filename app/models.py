from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(String)

    role = Column(String)


class UpgradeHistory(Base):

    __tablename__ = "upgrade_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_version = Column(String)

    target_version = Column(String)

    status = Column(String)