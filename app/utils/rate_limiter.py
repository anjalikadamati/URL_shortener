from flask import request, jsonify
from app.utils.redis_client import redis_client

RATE_LIMIT = 100
WINDOW = 60

def check_rate_limit():

    ip = request.remote_addr

    key = f"rate_limit:{ip}"

    requests = redis_client.incr(key)

    if requests == 1:
        redis_client.expire(key, WINDOW)

    if requests > RATE_LIMIT:
        return False

    return True