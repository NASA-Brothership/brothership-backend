from flask import Flask, request, jsonify
from cultura.enum import AltaSusceptibilidade, MediaSusceptibilidade, BaixaSusceptibilidade

app = Flask(__name__)

@app.route("/dry-analysis", methods=["POST"])
def dry_analysis():
    data_input = {
        "culture": request.json.get('culture'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radio": request.json.get('radio'),                         # raio em kilometros do circulo
        "irrigation": request.json.get('irrigation'),               # "Tem irrigação ou capacidade de investir em uma?"
        "planting_period": request.json.get('planting_period'),     # "Estamos antes, durante ou depois o período ideal de plantio?"
        "existing_culture": request.json.get('existing_culture')    # "Já tem cultura plantada no momento?"
    }
    # Prepare a resposta
    output = {
        "susceptibility": 0,    # Nota da Suscetibilidade => 1 ALTA | 0.66 MEDIA | 0.33 BAIXA
        "wbi_medium": 0,        # Balanço Hídrico
        "ndmi_medium": 0,       # UMIDADE
        "sb": 0,                # SB [ALTO; MEDIO E BAIXO ]

    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
