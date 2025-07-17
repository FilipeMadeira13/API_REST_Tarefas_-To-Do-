import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel, StaticPool, create_engine

from app.infra import database as db_module
from app.main import app

from app.domain.models import Task


@pytest.fixture()
def client(session: Session):
    def get_session_override():
        yield session

    app.dependency_overrides[db_module.get_session] = get_session_override
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


@pytest.fixture(scope="session")
def test_engine():
    engine = create_engine(
        "sqlite:///:memory:",
        echo=False,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False},
    )
    return engine


@pytest.fixture(scope="session")
def test_session_factory(test_engine):
    return sessionmaker(bind=test_engine, class_=Session)


@pytest.fixture(scope="function")
def session(test_engine, test_session_factory):
    SQLModel.metadata.create_all(test_engine)
    session = test_session_factory()
    try:
        yield session
    finally:
        session.close()
        SQLModel.metadata.drop_all(test_engine)
