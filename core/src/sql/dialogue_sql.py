from sqlalchemy import create_engine, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Dialogue(Base):
    __tablename__ = "dialogue_sql"

    user_id = Column('user_id', String, primary_key=True)
    conversation_id = Column('conversation_id', String, nullable=False)
    dialogue_state = Column('dialogue_state', String)
    system_action = Column('system_action', String)
    response = Column('response', String)
    event_ts = Column('event_ts', String, nullable=False)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)