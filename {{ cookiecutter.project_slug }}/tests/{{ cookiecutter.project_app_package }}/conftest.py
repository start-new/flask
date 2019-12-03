from {{ cookiecutter.project_app_package }} import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def db(app):
    from {{ cookiecutter.project_app_package }} import db

    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()
