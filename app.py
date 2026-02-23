from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown

app = Flask(__name__)

# Google Drive File ID of your model (DO NOT CHANGE)
FILE_ID = "16Dl3JGKWk_o8uUhA_R61zvLosYaZNak3"
MODEL_PATH = "housing_model.pkl"

# Auto-download model if not present (needed for Render because PKL > 25MB)
if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    print("Downloading model from Google Drive...")
    gdown.download(url, MODEL_PATH, quiet=False)

# Load saved models (Regression + Random Forest)
data = joblib.load(MODEL_PATH)
reg_model = data["reg_model"]   # Multiple Linear Regression (Market Value)
rf_model = data["rf_model"]     # Random Forest Classifier (Price Tier)


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

        # Correct feature order (MANDATORY as per California Housing dataset)
        features = np.array([[
            MedInc,
            HouseAge,
            AveRooms,
            AveBedrms,
            Population,
            AveOccup,
            Latitude,
            Longitude
        ]])

        # 🔹 1. Regression Prediction (Estimated Market Value)
        market_value = reg_model.predict(features)[0]

        # Dataset target is in 100,000s → convert to actual price
        estimated_price = round(market_value * 100000, 2)

        # 🔹 2. Classification Prediction (Price Tier using Random Forest)
        tier_pred = rf_model.predict(features)[0]

        # Convert class number to readable label (as per assignment 3 classes)
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


# IMPORTANT: Dynamic port for Render deployment (DO NOT REMOVE)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
