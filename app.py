from flask import Flask, render_template, request
import numpy as np
import joblib
import os
import gdown

app = Flask(__name__)

# === Google Drive File IDs ===
REG_FILE_ID = "PASTE_REG_FILE_ID_HERE"
RF_FILE_ID = "PASTE_RF_FILE_ID_HERE"

REG_MODEL_PATH = "reg_model.pkl"
RF_MODEL_PATH = "rf_model.pkl"


def download_model(file_id, output_path):
    if not os.path.exists(output_path):
        print(f"Downloading {output_path}...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)


# Download models once at startup
download_model(REG_FILE_ID, REG_MODEL_PATH)
download_model(RF_FILE_ID, RF_MODEL_PATH)

# Load models once at startup
reg_model = joblib.load(REG_MODEL_PATH)
rf_model = joblib.load(RF_MODEL_PATH)


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

            # Regression Prediction
            market_value = reg_model.predict(features_array)[0]

            # Classification Prediction
            category_pred = rf_model.predict(features_array)[0]

            category_map = {
                0: "Low Value Housing",
                1: "Medium Value Housing",
                2: "High Value Housing"
            }

            category = category_map.get(category_pred, "Unknown")

            return render_template(
                "index.html",
                prediction_text=f"Estimated Market Value: ${market_value:.2f}",
                category_text=f"Predicted Category: {category}"
            )

        except Exception as e:
            return render_template("index.html", prediction_text="Error occurred.")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
