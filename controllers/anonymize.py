from mongodb import get_nosql_db
from config import MONGODB_DB_NAME, SECRET_KEY_1, SECRET_KEY_2, SALT, HASHED_FIELDS
from controllers.users import get_password_hash
import logging
import hmac
import hashlib
import base64

logger = logging.getLogger(__name__)


async def anonymize_data(username, password, _data):
    client = await get_nosql_db()
    db = client[MONGODB_DB_NAME]
    _collection = db.users
    hashed_password = get_password_hash(password + SALT)
    data = {}
    data["password"] = hashed_password
    for k, v in _data:
        if type(v) == str and k in HASHED_FIELDS:
            digest = hmac.new(SECRET_KEY_1, msg=SALT + v, digestmod=hashlib.sha256).digest()
            signature = base64.b64encode(digest).decode()
            data[k] = signature
        else:
            data[k] = v

    # CHANGE TO A CREATE ONE
    inserted_id = _collection.insert_one(data).inserted_id
    connector_id = _collection.find_one({"_id": inserted_id})._id.toString()

    digest = hmac.new(SECRET_KEY_2, msg=SALT + connector_id, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest).decode()

    _sensitive = db.usersen
    _sensitive.insert_one({"root_id": signature, "content": {**_data}})

    row = _collection.find_one({"_id": inserted_id})
    return row
