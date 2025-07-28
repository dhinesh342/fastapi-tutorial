from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_url = f"sqlite:///./blog.db"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()


