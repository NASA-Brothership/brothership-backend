from flask import Flask, request, jsonify
from cultura.enum import VeryHighSusceptibility, HighSusceptibility, MediumSusceptibility, LowSusceptibility, VeryLowSusceptibility
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

def get_susceptibility(culture):
    if culture in VeryHighSusceptibility.__members__.keys():
        return VERY_HIGH
    if culture in HighSusceptibility.__members__.keys():
        return HIGH
    if culture in MediumSusceptibility.__members__.keys():
        return MEDIUM
    if culture in LowSusceptibility.__members__.keys():
        return LOW
    if culture in VeryLowSusceptibility.__members__.keys():
        return VERY_LOW

@app.route("/dry-analysis", methods=["POST"])
def dry_analysis():
    data_input = {
        "culture": request.json.get('culture'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radius_km": request.json.get('radius_km'),               # radius in kilometers of the circle
        "irrigation": request.json.get('irrigation'),             # "Does it have irrigation or the capacity to invest in one?"
        "planting_period": request.json.get('planting_period'),   # "Are we before, during, or after the ideal planting period?"
        "existing_culture": request.json.get('existing_culture')  # "Is there already a culture planted at the moment?"
    }
    susceptibility = get_susceptibility(data_input['culture'])
    output = {
        "susceptibility": susceptibility,   # Susceptibility rating of the culture => 1 HIGH | 0.66 MEDIUM | 0.33 LOW
        "wbi_medium": 0,                    # Water Balance Index
        "sb": 0,                            # SB Water Balance
        "ndmi_medium": 0,                   # MOISTURE
        "su": 0                             # SU Moisture
    }
    return jsonify(output)

if __name__ == "__main__":
    VERY_HIGH = 0.9
    HIGH = 0.7
    MEDIUM = 0.5
    LOW = 0.3
    VERY_LOW = 0.1

    app.run(host="0.0.0.0", port=8000, debug=True)