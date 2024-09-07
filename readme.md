# README: CV Roaster Project

## Overview

The **CV Roaster** is a Flask-based web application that allows users to upload their CVs for analysis using Google Generative AI (Gemini 1.5). The application humorously critiques overused clichés, buzzwords, and unnecessary jargon, providing playful feedback and friendly advice on how to improve the CV.

## Features

- **CV Upload**: Users can upload their CVs (PDF format).
- **AI-Powered Analysis**: The application utilizes Google Generative AI to critique the CV.
- **Humorous Feedback**: The CV is analyzed with a humorous and constructive tone.
- **Friendly Advice**: Users receive advice on how to improve their CVs.

## Prerequisites

- Python 3.7+
- Flask
- Flask-CORS
- Google Generative AI (Gemini 1.5)
- dotenv (for managing environment variables)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root and add your Google Generative AI API key:
   ```
   API_KEY=your_google_api_key
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

   The app will be running locally at `http://127.0.0.1:5000`.

## Usage

- Access the `/roast_cv` endpoint via a POST request to upload a CV for analysis.
- You can upload a CV as part of the form data using the key `cv`.
  
Example request:
```bash
curl -X POST -F "cv=@path_to_cv.pdf" http://127.0.0.1:5000/roast_cv
```

## File Structure

- `app.py`: The main Flask application file.
- `uploads/`: A folder where uploaded CVs are stored.
- `.env`: File for storing environment variables, such as the API key.
- `requirements.txt`: A list of all the Python dependencies.

## Endpoints

### POST /roast_cv

- **Description**: Upload a CV and receive humorous feedback.
- **Parameters**: 
  - `cv`: A PDF file containing the CV to be roasted.
- **Response**:
  - `message`: Confirmation of successful upload.
  - `filepath`: The path of the uploaded file.
  - `roaster_response`: The humorous and constructive feedback from the AI.

## Example Response

```json
{
  "message": "File uploaded successfully",
  "filepath": "./uploads/my_cv.pdf",
  "roaster_response": "Your CV says 'team player'—that's like saying 'I show up to work!'..."
}
```



