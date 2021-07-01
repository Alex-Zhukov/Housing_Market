# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import pandas as pd
import dill

app = Flask(__name__)


def load_model(model_path):
    # load the pre-trained model
    global model
    with open(model_path, 'rb') as f:
        model = dill.load(f)


modelpath = "./models/lightgbm.dill"
load_model(modelpath)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    data = {"success": False}
    if request.method == "POST":
        request_json = request.get_json()
        try:
            prediction = model.predict(pd.DataFrame(request_json, index=[request_json['id']]))
        except Exception as e:
            data['predictions'] = str(e)
            data['success'] = False
            return jsonify(data)

    data["success"] = True
    data['predictions'] = float(prediction[0])
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
