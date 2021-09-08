from flask import Flask, jsonify
import os

from utils import get_jokes


app = Flask(__name__)

@app.route('/health-check', methods=['GET'])
def api_health_check():
    return jsonify({"status": "Server is running..!!!"}) 

@app.route('/api/v1/fetch_jokes', methods=['GET'])
def fetch_jokes():
    page, jokes = 1, []
    while len(jokes) < 100:
        jokes.extend(get_jokes(page))
        page += 1
    return jsonify({"success": True, "jokes": jokes})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
