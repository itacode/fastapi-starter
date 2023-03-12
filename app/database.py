from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.get_db_url())

# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#using-a-sessionmaker
db_session = sessionmaker(bind=engine, expire_on_commit=False)
