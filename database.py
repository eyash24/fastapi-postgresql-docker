import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
from config import settings as _settings


engine = _sql.create_engine(_settings.database_url)

SessionLocal = _orm.sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = _declarative.declarative_base()
