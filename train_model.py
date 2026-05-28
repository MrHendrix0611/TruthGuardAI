import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle


# ==========================================
# CARREGAR DADOS
# ==========================================

dados = pd.read_csv("noticias.csv")

X = dados["texto"]
y = dados["label"]

# ==========================================
# DIVIDIR DADOS
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# VETORIZAÇÃO + MODELO
# ==========================================

vectorizer = TfidfVectorizer(stop_words=None)

X_train_vectorized = vectorizer.fit_transform(X_train)

modelo = MultinomialNB()

modelo.fit(X_train_vectorized, y_train)

# ==========================================
# TESTE
# ==========================================

X_test_vectorized = vectorizer.transform(X_test)

predicoes = modelo.predict(X_test_vectorized)

acuracia = accuracy_score(y_test, predicoes)

print(f"Acurácia do modelo: {acuracia * 100:2f}%")

# ===========================================
# SALVAR MODELO
# ===========================================

pickle.dump(modelo, open("fake_news_model.pkl", "wb"))

pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Modelo treinado com sucesso!")