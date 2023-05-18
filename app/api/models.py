from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.database import database

class Client(database.Model):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(12), unique=True, index=True)
    operator_code = Column(String(3), index=True)
    tag = Column(String(255), index=True)
    timezone = Column(String(255))

class Mailing(database.Model):
    __tablename__ = "mailings"

    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    message = Column(String(255))
    operator_code = Column(String(3), index=True)
    tag = Column(String(255))

class Message(database.Model):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String(20))
    mailing_id = Column(Integer, index=True)
    client_id = Column(Integer, index=True)
