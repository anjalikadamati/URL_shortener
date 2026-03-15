from app import db
from app.models.url_model import URL
from app.utils.base62 import encode_base62


def create_short_url(original_url):

    new_url = URL(original_url=original_url)

    db.session.add(new_url)
    db.session.commit()

    short_code = encode_base62(new_url.id)

    new_url.short_code = short_code
    db.session.commit()

    return short_code

def get_original_url(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        url.clicks += 1
        db.session.commit()
        return url.original_url

    return None