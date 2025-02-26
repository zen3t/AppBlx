from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///app_blx.db"
# Criar conexão com o banco de dados SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args = {"check_same_thread":False}
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
# Base para as tabelas
Base = declarative_base()


def criar_db():
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
