from flask import Flask, render_template, request

import pickle

# =========================================
# CARREGAR MODELO
# =========================================

modelo = pickle.load(open("fake_news_model.pkl", "rb"))

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# =========================================
# APP
# =========================================

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():

    resultado = None
    probabilidade = None

    if request.method == "POST":

        noticia = request.form["noticia"]

        noticia_transformada = vectorizer.transform([noticia])

        previsao = modelo.predict(noticia_transformada)[0]

        probabilidades = modelo.predict_proba(
            noticia_transformada
        )

        confianca = round(
            max(probabilidades[0]) * 100, 2
        )

        resultado = previsao
        probabilidade = confianca

    return render_template(
        "index.html",
        resultado=resultado,
        probabilidade=probabilidade
    )

if __name__ == "__main__":
    app.run(debug=True)