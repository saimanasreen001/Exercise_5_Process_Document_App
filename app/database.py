from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config

# Create engine --> Connection to the DB.
engine = create_engine(config.DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get database session
# Creates a new Database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
