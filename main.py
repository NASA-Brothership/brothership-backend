import datetime
import crops.plants as plants
from crops.code_enums import (
    DroughtRisk
)
from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS
from meteomatics_interface.meteomatics_interface import MeteomaticsInterface

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

username = "sonoda_gustavoshoiti"
password = "5P6Kmg1ktI"

# Function to get drought risk category for a crop
def get_drought_risk(crop: str) -> DroughtRisk:
    # Check for crop in each drought risk category
    print(crop)
    if crop in plants.very_low_drought_risk:
        return DroughtRisk.VERY_LOW
    elif crop in plants.low_drought_risk:
        return DroughtRisk.LOW
    elif crop in plants.medium_drought_risk:
        return DroughtRisk.MEDIUM
    elif crop in plants.high_drought_risk:
        return DroughtRisk.HIGH
    elif crop in plants.very_high_drought_risk:
        return DroughtRisk.VERY_HIGH

@app.route('/plants', methods=['GET'])
def get_plants():
    return jsonify(list(plants.all_plants))

@app.route("/drought-analysis", methods=["POST"])
def drought_analysis():
    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=14)
    data_input = {
        "crop_type": request.json.get('crop_type'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radius_km": request.json.get('radius_km'),                 # radius in kilometers of the circle
        "is_irrigated": request.json.get('is_irrigated'),           # "Does it have irrigation or the capacity to invest in one?"
        "planting_period": request.json.get('planting_period'),     # "Are we before, during, or after the ideal planting period?"
        "existing_crops": request.json.get('existing_crops')        # "Is there already a crop planted at the moment?"
    }
    app.logger.debug(data_input['crop_type'])
    drought_risk = get_drought_risk(data_input['crop_type'])

    api = MeteomaticsInterface(username, password)

    try:
        weather_data = api.get_precipitation_days(data_input['latitude'], data_input['longitude'], start, end)
        precipitation_mean = api.get_precipitation_mean(weather_data)
    except Exception as e:
        print(str(e))
        
    output = {
        "drought_risk": drought_risk.value, # drought_risk rating of the crop
        "precipitation_mean": precipitation_mean
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
