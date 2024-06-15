from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:root@localhost:5432/quiz'

engine = create_engine(URL_DATABASE)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
