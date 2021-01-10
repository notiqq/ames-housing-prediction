
from flask import Flask, session, redirect
from flask import request
from flask import jsonify
from model import Model
import json



app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_data():
    model = Model()
    results = model.predict()
    items = []
    for item in results:
        dct = {"id":int(item[0]), "price":int(item[1])}
        items.append(dct)
        
    result = json.dumps(items)
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=False)
    