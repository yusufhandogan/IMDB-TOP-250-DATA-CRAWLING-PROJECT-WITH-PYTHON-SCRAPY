from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary,VARCHAR,NVARCHAR)

from scrapy.utils.project import get_project_settings


Declarativebase = declarative_base()




def db_connect():



      return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):

      Declarativebase.metadata.create_all(engine)


class IMDB_DATABASE(Declarativebase):

      __tablename__ = "TOP_250_MOVIES"


      MOVIE_CODE = Column("MOVIE_CODE",NVARCHAR(300),primary_key=True)

      MOVIE_NAME = Column("MOVIE_NAME",NVARCHAR(300))

      YEAR = Column("YEAR",Integer())

      RANK = Column("RANK",Integer())
      
      IMDB_RATING = Column("IMDB_RATING",Float())