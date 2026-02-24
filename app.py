from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# ==============================
# Load Models (Direct from Repo)
# ==============================

reg_model = joblib.load("reg_model.pkl")
rf_model = joblib.load("rf_model.pkl")

print("Models loaded successfully.")

# ==============================
# Routes
# ==============================

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            features = [
                float(request.form["MedInc"]),
                float(request.form["HouseAge"]),
                float(request.form["AveRooms"]),
                float(request.form["AveBedrms"]),
                float(request.form["Population"]),
                float(request.form["AveOccup"]),
                float(request.form["Latitude"]),
                float(request.form["Longitude"]),
            ]

            features_array = np.array([features])

            # Regression prediction
            market_value = reg_model.predict(features_array)[0]
            estimated_price = round(market_value * 100000, 2)

            # Classification prediction
            category_pred = rf_model.predict(features_array)[0]

            category_map = {
                0: "Low Value Housing",
                1: "Medium Value Housing",
                2: "High Value Housing"
            }

            category = category_map.get(category_pred, "Unknown")

            return render_template(
                "index.html",
                market_value=estimated_price,
                tier=category
            )

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")


# ==============================
# Render Production Setup
# ==============================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
