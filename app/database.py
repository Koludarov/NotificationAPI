from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Создание объекта для подключения к базе данных
engine = create_engine("postgresql://postgres:postgres@localhost:5432/db_name")

# Создание объекта сессии для работы с базой данных
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Базовый класс для объявления моделей
Base = declarative_base()
Base.query = db_session.query_property()

# Импорт моделей
from app.api.models import Client, Mailing, Message

# Создание таблиц в базе данных (если необходимо)
def create_tables():
    Base.metadata.create_all(bind=engine)
