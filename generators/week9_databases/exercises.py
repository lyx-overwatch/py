from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


def get_engine(url: str = "sqlite:///:memory:"):
    return create_engine(url, echo=False)


def create_tables(engine):
    Base.metadata.create_all(engine)


def get_session(engine):
    return sessionmaker(bind=engine)()


def add_user(session, name: str):
    u = User(name=name)
    session.add(u)
    session.commit()
    return u


def get_user(session, user_id: int):
    return session.query(User).filter_by(id=user_id).first()
