from crops.code_enums import (
    VeryLowDroughtRisk,
    LowDroughtRisk,
    MediumDroughtRisk,
    HighDroughtRisk,
    VeryHighDroughtRisk,
    DroughtRisk
)

from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to get drought risk category for a crop
def get_drought_risk(crop: str):
    # Check for crop in each drought risk category
    if crop in VeryHighDroughtRisk.__members__.keys():
        return DroughtRisk.VERY_HIGH
    elif crop in HighDroughtRisk.__members__.keys():
        return DroughtRisk.HIGH
    elif crop in MediumDroughtRisk.__members__.keys():
        return DroughtRisk.MEDIUM
    elif crop in LowDroughtRisk.__members__.keys():
        return DroughtRisk.LOW
    elif crop in VeryLowDroughtRisk.__members__.keys():
        return DroughtRisk.VERY_LOW
    else:
        return None  # Return None if crop is not found in any category

@app.route("/drought-analysis", methods=["POST"])
def drought_analysis():
    data_input = {
        "crop_type": request.json.get('crop_type'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radius_km": request.json.get('radius_km'),               # radius in kilometers of the circle
        "is_irrigated": request.json.get('is_irrigated'),             # "Does it have irrigation or the capacity to invest in one?"
        "planting_period": request.json.get('planting_period'),   # "Are we before, during, or after the ideal planting period?"
        "existing_crops": request.json.get('existing_crops')  # "Is there already a crop planted at the moment?"
    }
    drought_risk = get_drought_risk(data_input['crop_type'])
    output = {
        "drought_risk": drought_risk.value # drought_risk rating of the crop
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
