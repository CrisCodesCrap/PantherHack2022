from sqlalchemy import ARRAY, Boolean, Column, DateTime, Float, ForeignKey,String ,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from settings import settings

def engine_init(settings):
    url = f'{settings["host"]}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url,pool_size=50,echo=False)
    return engine

engine = engine_init(settings)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

Base = declarative_base()

class User(Base):
    __tablename__ = 'userlist'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    store = Column(String)
    name = Column(String(30),unique=True)
    position = Column(String())
    password = Column(String(64))
    timestamp = Column(DateTime)
    typeOfEstablishment = Column(Integer)
    messagesSent = Column(Integer(),default=0)
    lastSeen = Column(DateTime)
    location = Column(ARRAY(Float))
    online = Column(Boolean)

class MessageList(Base):
    __tablename__ = 'messages'
    id = Column(Integer(),primary_key=True)
    content = Column(String(512))
    timestamp = Column(DateTime)
    sender = Column(ForeignKey('userlist.id'))
    room = Column(ForeignKey('rooms.id'))

class RoomList(Base):
    __tablename__ = 'rooms'
    id = Column(Integer(), primary_key=True)
    user1 = Column(ForeignKey('userlist.id'))
    user2 = Column(ForeignKey('userlist.id'))
    timestamp = Column(DateTime)

class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    heading = Column(String(50))
    body = Column(String(1000))
    creator = Column(ForeignKey('userlist.id'))
    timestamp = Column(DateTime)
    price = Column(Float)
    amount = Column(Integer)
    location = Column(ARRAY(Float))

Base.metadata.create_all(bind=engine)