from app import db
from app.models.url_model import URL
from app.utils.base62 import encode_base62
from app.utils.redis_client import redis_client


def create_short_url(original_url):

    new_url = URL(original_url=original_url)

    db.session.add(new_url)
    db.session.commit()

    short_code = encode_base62(new_url.id)

    new_url.short_code = short_code
    db.session.commit()

    return short_code

def get_original_url(short_code):

    cached_url = redis_client.get(short_code)

    if cached_url:
        return cached_url

    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        url.clicks += 1
        db.session.commit()

        redis_client.set(short_code, url.original_url)

        return url.original_url

    return None