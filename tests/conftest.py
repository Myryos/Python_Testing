import pytest
from server import app as flask_app
import threading
import time


@pytest.fixture(scope="module")
def app():
    flask_app.config["TESTING"] = True
    return flask_app


@pytest.fixture(scope="module")
def client(app):
    return app.test_client()


@pytest.fixture(scope="module")
def live_server(app):
    server = threading.Thread(target=app.run, kwargs={"port": 5000})
    server.start()
    time.sleep(1)  # Donne le temps au serveur de démarrer
    yield
    server.join(1)
