import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from constants import ROOT_DIR

engine = create_engine('sqlite:///' + os.path.join(ROOT_DIR, 'aplicacion.sqlite'))
Session = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()
