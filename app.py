from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

reg_model = None
rf_model = None
models_loaded = False


def load_models():
    global reg_model, rf_model, models_loaded
    if not models_loaded:
        reg_model = joblib.load("reg_model.pkl")
        rf_model = joblib.load("rf_model.pkl")
        models_loaded = True


@app.route("/", methods=["GET", "POST"])
def home():
    global models_loaded

    # 🔥 Load models during first GET request (after server is healthy)
    if request.method == "GET" and not models_loaded:
        load_models()

    if request.method == "POST":
        try:
            # Ensure models are loaded
            load_models()

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

            market_value = reg_model.predict(features_array)[0]
            estimated_price = round(market_value * 100000, 2)

            category_pred = rf_model.predict(features_array)[0]

            category_map = {
                0: "Low Value Housing",
                1: "Medium Value Housing",
                2: "High Value Housing"
            }

            category = category_map.get(category_pred, "Unknown")

            return render_template(
                "index.html",
                market_value=f"{estimated_price:,.2f}",
                tier=category,
                inputs=features
            )

        except Exception as e:
            return render_template("index.html", error=str(e), inputs=None)

    return render_template("index.html", inputs=None)


if __name__ == "__main__":
    app.run(debug=True)
