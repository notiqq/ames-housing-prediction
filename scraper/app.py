
from flask import Flask, session, redirect
from flask import request
from flask import jsonify
from spider import Spider


app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_data():
    data = Spider().scrape_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001, use_reloader=False)
    