from app import db
from app.models.url_model import URL
from app.utils.base62 import encode_base62
from app.utils.redis_client import redis_client
from datetime import datetime, timedelta


def create_short_url(original_url, expires_in=None):

    new_url = URL(original_url=original_url)
    db.session.add(new_url)
    db.session.commit()

    short_code = encode_base62(new_url.id)
    new_url.short_code = short_code

    if expires_in:
        new_url.expires_at = datetime.utcnow() + timedelta(seconds=expires_in)

    db.session.commit()

    if expires_in:
        redis_client.setex(short_code, expires_in, original_url)
    else:
        redis_client.set(short_code, original_url)

    return short_code


def get_original_url(short_code):

    cached_url = redis_client.get(short_code)

    if cached_url:
        url = URL.query.filter_by(short_code=short_code).first()
        if url:
            url.clicks += 1
            db.session.commit()
        return cached_url

    url = URL.query.filter_by(short_code=short_code).first()

    if not url:
        return None

    if url.expires_at and url.expires_at < datetime.utcnow():
        return None

    url.clicks += 1

    redis_client.incr(f"clicks:{short_code}")

    db.session.commit()

    redis_client.setex(short_code,3600, url.original_url)

    return url.original_url


#For Performance testing
# USE_CACHE = False # change this to False to disable Redis

# def get_original_url(short_code):
#     # Try cache
#     if USE_CACHE:
#         cached = redis_client.get(short_code)
#         if cached:
#             return cached.decode('utf-8')

#     # DB fetch
#     url = URL.query.filter_by(short_code=short_code).first()

#     if url:
#         if USE_CACHE:
#             redis_client.set(short_code, url.original_url, ex=3600)
#         return url.original_url

#     return None