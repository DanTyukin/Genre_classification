import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
from utils.feature_extraction import extract_features

app = Flask(__name__)

with open('model/xgb_mgen.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('model/min_max_scaler.pkl', 'rb') as scaler_file:
    min_max_scaler = pickle.load(scaler_file)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

style = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        features = extract_features(file_path, min_max_scaler)
        prediction = model.predict(features)
        genre = style[prediction[0]]

        return redirect(url_for('result', genre=genre))
    else:
        return jsonify({'error': 'File not processed'}), 400

@app.route('/result')
def result():
    genre = request.args.get('genre', 'Unknown')
    return render_template('result.html', genre=genre)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)