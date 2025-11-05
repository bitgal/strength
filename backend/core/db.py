#db connection and session creation
# defined as a class
# TODO uses DI for env-specific database usage

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
from typing import Generator


class Database:

    def __init__(self, DATABASE_URL:str = "sqlite:///strength.db", ECHO:bool = True):
        # self.env = os.getenv("ENV", "development")
        self.echo = ECHO
        self.database_url = DATABASE_URL

        self.engine = create_engine(self.database_url, echo=self.echo)
        self.sessionLocal = sessionmaker(bind=self.engine)
        self.Base = declarative_base()

    # yields a db session object (used per route), doesnt accept or return anything else:
    def get_db(self) -> Generator[Session, None, None]: 
        db = self.sessionLocal()
        try:
            yield db
        finally:
            db.close()

# instantiate a single database manager
db_url_prod = "mysql+pymysql://root:root@localhost:8889/db_strength"
db_url_test = "sqlite:///strength.db"

db_manager = Database(DATABASE_URL = db_url_prod)

# expose the Base and dependency for FastAPI
Base = db_manager.Base
get_db = db_manager.get_db # not calling it here - just refers to the method itself!
        
        



