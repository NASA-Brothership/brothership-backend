import datetime
import crops.plants as plants
from crops.code_enums import DroughtRiskValues
from flask import (
    Flask,
    request,
    jsonify
)
from flask_cors import CORS
from meteomatics_interface.meteomatics_interface import MeteomaticsInterface
from utils.risk import get_drought_risk, get_mean_risk, get_recomendation

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

username = "sonoda_gustavoshoiti"
password = "5P6Kmg1ktI"

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
        precipitation_sum = api.get_precipitation_sum(weather_data)
    except Exception as e:
        print(str(e))
    
    sc = DroughtRiskValues.VERY_LOW.value     # sucetibilidade da cultura (quanto maior, maior probabilidade de perdas na procução)
    su = DroughtRiskValues.VERY_LOW.value     # sucetibilidade da umidade (quanto maior, maior probabilidade de perdas na procução)
    sb = DroughtRiskValues.VERY_LOW.value     # sucetibilidade do balanço hidrigo (quanto maior, maior probabilidade de perdas na procução)
    spt = DroughtRiskValues.VERY_LOW.value    # sucetibilidade do previsão de chuvas (quanto maior, maior probabilidade de perdas na procução)

    mean_risk = get_mean_risk(sc, su, sb, spt)
    recomandation = get_recomendation(
                                mean_risk, 
                                data_input['is_irrigated'], 
                                data_input['planting_period'],
                                data_input['existing_crops']
                                )

    output = {
        "drought_risk": drought_risk.value, # drought_risk rating of the crop
        "precipitation_mean": precipitation_sum,
        "sc": sc,
        "su": su,
        "sb": sb,
        "spt": spt,
        "recomentation": recomandation
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
