from app import create_app, db
import time

app = create_app()

def wait_for_db():
    with app.app_context():  
        while True:
            try:
                db.create_all()
                print("✅ Database connected!")
                break
            except Exception as e:
                print("⏳ Waiting for DB...", e)
                time.sleep(3)

wait_for_db()

@app.route("/")
def home():
    return "URL Shortener is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)