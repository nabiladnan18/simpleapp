from flask import Flask, render_template, session, request
from dotenv import load_dotenv
import os

app = Flask(__name__, template_folder="./templates", static_folder="./static")

load_dotenv(".env")


@app.route("/", methods=["GET", "POST"])
def home():
    counter = session.get("counter", 0)
    environment = os.getenv("FLASK_ENVIRONMENT")
    if request.method == "POST":
        counter += 1
        session.update(
            {
                "counter": counter
            }
        )
    
    return render_template('base.html', counter=counter, environment=environment)

if __name__ == '__main__':
    app.run()
