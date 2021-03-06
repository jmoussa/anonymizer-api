import pytest
import nest_asyncio

from anonymizer.mongodb import get_nosql_db, connect_to_mongo
from fastapi.testclient import TestClient
from anonymizer.app import app

# handles event loop
nest_asyncio.apply()


# override mongodb (currently just using normal db, will transition to mock db later)
async def override_get_nosql_db():
    await connect_to_mongo()
    client = await get_nosql_db()
    return client


app.dependency_overrides[get_nosql_db] = override_get_nosql_db

# instantiate test client app that we will use for these test modules
client = TestClient(app)


@pytest.mark.asyncio
async def test_anon():
    json_body = {"username": "test_user", "password": "password", "data": {"test_key": "test_value"}}
    response = client.post("/api/anonymize", json=json_body)
    assert response.status_code == 200
