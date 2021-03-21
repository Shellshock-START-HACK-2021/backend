from flask import Blueprint, request, jsonify
import requests
from decouple import config

bp = Blueprint("misc", __name__)

@bp.route("/definition")
def word_definition():
    word = request.args.get("word")
    headers = {
        "app_id": config("OXFORD_ID"),
        "app_key": config("OXFORD_KEY")
    }
    resp = requests.get(f"https://od-api.oxforddictionaries.com/api/v2/words/en-gb?q={word}", headers=headers)
    if resp.status_code >= 400:
        return jsonify(success=False, error="word not found")
    result = resp.json()["results"][0]
    senses = result["lexicalEntries"][0]["entries"][0]["senses"]
    definitions = []
    for i in senses:
        definitions.append(i["definitions"][0])
    return jsonify(success=True, definitions=definitions)