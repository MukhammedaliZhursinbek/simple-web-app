from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Privet, Mir!"

if __name__ == "__main__":
    app.run(debug=Ture)
