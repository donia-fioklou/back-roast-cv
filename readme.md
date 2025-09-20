# Transformez votre CV avec l'intelligence artificielle

Obtenez des conseils personnalisés, optimisez vos compétences et augmentez vos chances d'être recruté grâce à notre IA spécialisée.

## Vue d'ensemble

**CV Roaster** est une application web basée sur Flask qui utilise l'intelligence artificielle (Google Generative AI - Gemini 1.5) pour analyser et améliorer votre CV. Notre IA vous fournit des conseils personnalisés pour optimiser votre présentation professionnelle et maximiser vos chances de décrocher l'emploi de vos rêves.

## Fonctionnalités

- **Upload de CV** : Téléchargez votre CV au format PDF pour analyse
- **Analyse IA avancée** : Utilisation de Google Generative AI pour une évaluation approfondie
- **Conseils personnalisés** : Recevez des recommandations adaptées à votre profil
- **Optimisation des compétences** : Mise en valeur de vos atouts et amélioration des points faibles
- **Augmentation des chances de recrutement** : Stratégies pour vous démarquer des autres candidats

## Prérequis

- Python 3.7+
- Flask
- Flask-CORS
- Google Generative AI (Gemini 1.5)
- dotenv (pour la gestion des variables d'environnement)

## Instructions d'installation

1. **Cloner le repository** :
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Créer un environnement virtuel** (optionnel mais recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances requises** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Créer un fichier `.env`** à la racine du projet et ajouter votre clé API Google Generative AI :
   ```
   API_KEY=votre_cle_api_google
   ```

5. **Lancer l'application** :
   ```bash
   python app.py
   ```

   L'application sera accessible localement à l'adresse `http://127.0.0.1:5000`.

## Utilisation

- Accédez au point de terminaison `/roast_cv` via une requête POST pour télécharger un CV à analyser.
- Vous pouvez télécharger un CV en tant que partie des données de formulaire en utilisant la clé `cv`.
  
Exemple de requête :
```bash
curl -X POST -F "cv=@chemin_vers_cv.pdf" http://127.0.0.1:5000/roast_cv
```

## Structure des fichiers

- `app.py` : Le fichier principal de l'application Flask.
- `uploads/` : Un dossier où les CV téléchargés sont stockés.
- `.env` : Fichier pour stocker les variables d'environnement, comme la clé API.
- `requirements.txt` : Liste de toutes les dépendances Python.

## Points de terminaison

### POST /roast_cv

- **Description** : Téléchargez un CV et recevez des conseils personnalisés d'amélioration.
- **Paramètres** : 
  - `cv` : Un fichier PDF contenant le CV à analyser.
- **Réponse** :
  - `message` : Confirmation du téléchargement réussi.
  - `filepath` : Le chemin du fichier téléchargé.
  - `roaster_response` : Les conseils personnalisés et constructifs de l'IA.

## Exemple de réponse

```json
{
  "message": "File uploaded successfully",
  "filepath": "./uploads/mon_cv.pdf",
  "roaster_response": "Votre CV présente de bons points, mais voici comment l'optimiser pour maximiser vos chances de recrutement..."
}
```

## Avantages de notre solution IA

- **Analyse approfondie** : Notre IA examine chaque aspect de votre CV
- **Conseils personnalisés** : Recommandations adaptées à votre secteur d'activité
- **Optimisation ATS** : Amélioration de la compatibilité avec les systèmes de recrutement automatisés
- **Mise en valeur des compétences** : Identification et valorisation de vos atouts uniques
- **Stratégies de différenciation** : Techniques pour vous démarquer de la concurrence



