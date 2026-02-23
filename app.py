from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown

app = Flask(__name__)

FILE_ID = "16Dl3JGKWk_o8uUhA_R61zvLosYaZNak3"
MODEL_PATH = "housing_model.pkl"


def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)


download_model()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Load model ONLY when needed
        data = joblib.load(MODEL_PATH)
        reg_model = data["reg_model"]
        rf_model = data["rf_model"]

        MedInc = float(request.form["MedInc"])
        HouseAge = float(request.form["HouseAge"])
        AveRooms = float(request.form["AveRooms"])
        AveBedrms = float(request.form["AveBedrms"])
        Population = float(request.form["Population"])
        AveOccup = float(request.form["AveOccup"])
        Latitude = float(request.form["Latitude"])
        Longitude = float(request.form["Longitude"])

        features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                              Population, AveOccup, Latitude, Longitude]])

        market_value = reg_model.predict(features)[0]
        estimated_price = round(market_value * 100000, 2)

        tier_pred = rf_model.predict(features)[0]

        if tier_pred == 0:
            tier_label = "Low Value Housing"
        elif tier_pred == 1:
            tier_label = "Medium Value Housing"
        else:
            tier_label = "High Value Housing"

        return render_template(
            "index.html",
            market_value=estimated_price,
            tier=tier_label
        )

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
