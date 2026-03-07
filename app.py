from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("model/IDS_Intrusiondet_model.h5")

# Create scaler from dataset
df = pd.read_csv("sample_dataset.csv")
X = df.drop("Label", axis=1)

scaler = StandardScaler()
scaler.fit(X)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json["features"]

    data = np.array(data).reshape(1,-1)

    data = scaler.transform(data)

    data = np.expand_dims(data,axis=2)

    prediction = model.predict(data)

    label = int(np.argmax(prediction))

    if label == 0:
        result = "Normal Traffic"
    else:
        result = "Intrusion Detected"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)