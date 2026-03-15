from datetime import datetime
from app import db


class URL(db.Model):
    __tablename__ = "urls"

    id = db.Column(db.Integer, primary_key=True)

    original_url = db.Column(db.Text, nullable=False)

    short_code = db.Column(db.String(10), unique=True, index=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    expires_at = db.Column(db.DateTime, nullable=True)

    clicks = db.Column(db.Integer, default=0)