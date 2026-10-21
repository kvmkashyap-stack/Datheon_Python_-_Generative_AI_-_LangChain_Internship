
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Store the database in the VortexAI project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "vortex.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy database models."""
    pass


def init_db():
    """Create all database tables registered with Base."""
    from database import chat_repository  # Register models

    Base.metadata.create_all(bind=engine)


def get_db():
    """Provide a database session and always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
