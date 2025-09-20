from flask import Flask, jsonify, request
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

# load the virtual environement variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app) 
# file  for  storing uploaded files
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# verifie if the upload folder exists, if not create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuration of the Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

    
def roaster(cv_file_path):
    prompt = """Tu es un expert en ressources humaines et en recrutement.
Analyse le CV suivant en tenant compte des standards du marché actuel.

Analyse ciblée : Identifie les points forts et les points faibles du CV.

Conseils personnalisés : Fournis des recommandations précises adaptées au secteur d’activité et au niveau d’expérience du candidat.

Optimisation ATS : Vérifie si le CV est compatible avec les systèmes de suivi des candidatures (ATS) et propose des améliorations pour passer ces filtres.

Suggestions pratiques : Propose des conseils concrets (formulation, mise en valeur des compétences, choix des mots-clés, structure)."""
    #prompt = """Plonge en profondeur dans ce CV et critique-le sévèrement ! Critique-moi à fond."""


    cv_file = genai.upload_file(path=cv_file_path,
                                display_name="Gemini 1.5 PDF")
    response = model.generate_content([cv_file, prompt])
    return response


@app.route('/roast_cv', methods=['POST'])
def upload_cv():
    # verifie if a file was uploaded
    if 'cv' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['cv']

    # verifie if a file was selected
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    # save the uploaded file to the upload folder
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
