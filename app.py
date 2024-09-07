from flask import Flask, jsonify, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
CORS(app) 
# Dossier pour stocker les CV téléchargés
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Assure-toi que le dossier existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuration de l'API clé
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

    
def roaster(cv_file_path):
    prompt = "Analyze this CV with a humorous and constructive tone. Highlight any overused clichés, buzzwords, or unnecessary jargon. Feel free to give playful critiques on the job experiences, skills, or education, and make fun of overly generic statements like 'team player' or 'hard-working.' End with a piece of friendly advice on how to improve the CV."

    cv_file = genai.upload_file(path=cv_file_path,
                                display_name="Gemini 1.5 PDF")
    response = model.generate_content([cv_file, prompt])
    return response


@app.route('/roast_cv', methods=['POST'])
def upload_cv():
    # Vérifie si un fichier est bien dans la requête
    if 'cv' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['cv']

    # Vérifie si un fichier a bien été sélectionné
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # Sauvegarde le fichier dans le répertoire UPLOAD_FOLDER
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        response = roaster(filepath)
        return jsonify({'message': 'File uploaded successfully', 
                        'filepath': filepath,
                        'roaster_response':response.text})

    return jsonify({'error': 'File upload failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
