from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return "Bienvenue sur mon projet Flask !"

if __name__ == '__main__':
    app.run(debug=True)
