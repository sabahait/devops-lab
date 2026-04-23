from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version final - Déployée automatiquement-day2-version 5"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)