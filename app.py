from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load saved models (Regression + Random Forest)
data = joblib.load("housing_model.pkl")
reg_model = data["reg_model"]   # Multiple Linear Regression
rf_model = data["rf_model"]     # Random Forest Classifier


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        MedInc = float(request.form["MedInc"])
        HouseAge = float(request.form["HouseAge"])
        AveRooms = float(request.form["AveRooms"])
        AveBedrms = float(request.form["AveBedrms"])
        Population = float(request.form["Population"])
        AveOccup = float(request.form["AveOccup"])
        Latitude = float(request.form["Latitude"])
        Longitude = float(request.form["Longitude"])

        # Arrange input in correct feature order (VERY IMPORTANT ORDER)
        features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                              Population, AveOccup, Latitude, Longitude]])

        # 1️⃣ Regression Prediction (Estimated Market Value)
        market_value = reg_model.predict(features)[0]

        # Convert to readable price (dataset scale is in 100,000s)
        estimated_price = round(market_value * 100000, 2)

        # 2️⃣ Classification Prediction (Price Tier using Random Forest)
        tier_pred = rf_model.predict(features)[0]

        # Convert numeric class to label
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
    app.run(host="0.0.0.0", port=10000)