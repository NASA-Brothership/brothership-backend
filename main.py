from flask import Flask, request, jsonify
from cultura.enum import MuitoAltaSusceptibilidade, AltaSusceptibilidade, MediaSusceptibilidade, BaixaSusceptibilidade, MuitoBaixaSusceptibilidade
from google_earth_engine.init_engine import GoogleEartnInterface


app = Flask(__name__)
google = GoogleEartnInterface()


def get_susceptibility(culture):
    if culture in MuitoAltaSusceptibilidade.__members__.keys():
        return VERY_HIGH
    if culture in AltaSusceptibilidade.__members__.keys():
        return HIGH
    if culture in MediaSusceptibilidade.__members__.keys():
        return MEDIUM
    if culture in BaixaSusceptibilidade.__members__.keys():
        return LOW
    if culture in MuitoBaixaSusceptibilidade.__members__.keys():
        return VERY_LOW

@app.route("/dry-analysis", methods=["POST"])
def dry_analysis():
    data_input = {
        "culture": request.json.get('culture'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radio_km": request.json.get('radio_km'),                   # raio em kilometros do circulo
        "irrigation": request.json.get('irrigation'),               # "Tem irrigação ou capacidade de investir em uma?"
        "planting_period": request.json.get('planting_period'),     # "Estamos antes, durante ou depois o período ideal de plantio?"
        "existing_culture": request.json.get('existing_culture')    # "Já tem cultura plantada no momento?"
    }
    susceptibility = get_susceptibility(data_input['culture'])
    output = {
        "susceptibility": susceptibility,   # Nota da Suscetibilidade da cultura => 1 ALTA | 0.66 MEDIA | 0.33 BAIXA
        "wbi_medium": 0,                    # Balanço Hídrico
        "sb": 0,                            # SB Balanço Hídrico
        "ndmi_medium": 0,                   # UMIDADE
        "su": 0                             # SU Umidade
    }
    return jsonify(output)

if __name__ == "__main__":
    VERY_HIGH = 0.9
    HIGH = 0.7
    MEDIUM = 0.5
    LOW = 0.3
    VERY_LOW = 0.1

    
    
    app.run(host="0.0.0.0", port=8000, debug=True)
