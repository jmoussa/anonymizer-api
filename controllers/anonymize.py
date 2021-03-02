from mongodb import get_nosql_db
from config import MONGODB_DB_NAME, SECRET_KEY_1, SECRET_KEY_2, SECRET_KEY_3, SALT
import logging

logger = logging.getLogger(__name__)


async def anonymize_data(username, password, _data):
    client = await get_nosql_db()
    # TODO: HASH THIS SUCKER
    hashed_password = password
    db = client[MONGODB_DB_NAME]
    _collection = db.users
    # CHANGE TO A CREATE ONE
    _collection.find_one({"username": username, "password": hashed_password})
    return _data
