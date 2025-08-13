from packaging import Package

from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager

_base_dir = Path(__file__).parent
DATABASE = Package(
    _base_dir,
    lambda *a: lambda cls: cls
)
ENGINE = create_engine(f"sqlite:///{_base_dir / 'panel.db'}")
SessionLocal = sessionmaker(bind=ENGINE, autoflush=False, autocommit=False)
BASE = declarative_base()


@contextmanager
def db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init_database():
    BASE.metadata.create_all(ENGINE)


def add_model(model):
    with db_session() as session:
        session.add(model)


def delete_model(model):
    with db_session() as session:
        session.delete(model)


def update_model(model):
    with db_session() as session:
        session.merge(model)


def query(model, primary_key = None, unfiltered: bool = False, just_one: bool = False, **kwargs):
    with SessionLocal() as session:
        if primary_key is not None:
            return session.query(model).get(primary_key)

        result = session.query(model) if unfiltered else session.query(model).filter_by(**kwargs)
        return result.first() if just_one else result.all()


def queue_action(name: str, data: dict = None):
    action = DATABASE.resolve('critical_action')
    new_action = action(name, data)
    add_model(new_action)


def get_actions():
    actions = DATABASE.resolve('critical_action')
    return query(actions, unfiltered=True)
