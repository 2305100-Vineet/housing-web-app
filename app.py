from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown

app = Flask(__name__)

# -----------------------------
# Google Drive Model Settings
# -----------------------------
FILE_ID = "16Dl3JGKWk_o8uUhA_R61zvLosYaZNak3"
MODEL_PATH = "housing_model.pkl"

# Download model only if not already present
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    gdown.download(id=FILE_ID, output=MODEL_PATH, quiet=False)

# Load saved models safely
try:
    data = joblib.load(MODEL_PATH)
    reg_model = data["reg_model"]   # Regression Model
    rf_model = data["rf_model"]     # Random Forest Classifier
except Exception as e:
    print("Error loading model:", e)
    raise e


# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        MedInc = float(request.form["MedInc"])
        HouseAge = float(request.form["HouseAge"])
        AveRooms = float(request.form["AveRooms"])
        AveBedrms = float(request.form["AveBedrms"])
        Population = float(request.form["Population"])
        AveOccup = float(request.form["AveOccup"])
        Latitude = float(request.form["Latitude"])
        Longitude = float(request.form["Longitude"])

        # Arrange features in correct dataset order
        features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                              Population, AveOccup, Latitude, Longitude]])

        # 1️⃣ Regression Prediction (Estimated Market Value)
        market_value = reg_model.predict(features)[0]
        estimated_price = round(market_value * 100000, 2)

        # 2️⃣ Classification Prediction (Price Tier)
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
