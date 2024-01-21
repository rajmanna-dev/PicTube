from flask import Flask, render_template
import config

app = Flask(__name__)

app.secret_key = config.SECRET_KEY


# Home page
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)
