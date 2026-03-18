import time
from sqlalchemy import create_engine

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@mysql:3306/url_shortener"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def connect_with_retry():
    for i in range(30):
        try:
            engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
            connection = engine.connect()
            print("✅ Connected to MySQL")
            return engine
        except Exception as e:
            print(f"⏳ Waiting for MySQL... Attempt {i+1}", e)
            time.sleep(2)

    raise Exception("❌ Could not connect to MySQL")

engine = connect_with_retry()