from flask import Flask, render_template, jsonify
from landmarks import get_sf_landmarks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/landmarks')
def landmarks():
    landmarks = get_sf_landmarks()
    return jsonify(landmarks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
