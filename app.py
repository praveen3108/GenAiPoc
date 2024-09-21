from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

genai.configure(api_key='AIzaSyD4kPx-7Ggj8Z1uqedLDNjEit_7gVloR9E')
model = genai.GenerativeModel('gemini-pro')    

# Define a POST route
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()  # Get JSON data from the POST request
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # You can process the received data here
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    response = model.generate_content(prompt)
    print(response.text)
    # Example response
    return  jsonify({"generated_text": response.text}), 200


if __name__ == '__main__':
    app.run(debug=True)
