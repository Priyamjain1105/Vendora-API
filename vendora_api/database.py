import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()
# Reuse the same DATABASE URI as Flask app
DB_PASSWORD = os.getenv("DB_PASSWORD")
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://avnadmin:{DB_PASSWORD}"
    "@mysql-3b0838a6-priyamjainsocial-b642.i.aivencloud.com:27509/defaultdb"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
