# 🛡️ TruthGuard AI

Sistema de detecção de Fake News utilizando Machine Learning com Python e Flask.

O projeto utiliza processamento de linguagem natural (NLP) e o algoritmo **Naive Bayes** para classificar notícias como:

* ✅ Verdadeiras
* ❌ Falsas

A aplicação possui interface web simples desenvolvida com Flask.

---

# 🚀 Demonstração

O usuário insere uma notícia no sistema e o modelo de IA analisa o texto retornando:

* Classificação da notícia
* Nível de confiança da previsão

---

# 📌 Funcionalidades

✅ Classificação automática de notícias
✅ Interface web com Flask
✅ Processamento de texto com TF-IDF
✅ Modelo de Machine Learning treinável
✅ Exibição da probabilidade/confiança
✅ Estrutura simples para estudos em IA/NLP

---

# 🧠 Tecnologias Utilizadas

* Python
* Flask
* Scikit-Learn
* Pandas
* HTML5
* CSS3
* Pickle

---

# 📂 Estrutura do Projeto

```bash id="q7l3ae"
TRUTHGUARD_AI/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── fake_news_model.pkl
├── vectorizer.pkl
├── noticias.csv
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Como Funciona

O sistema segue as seguintes etapas:

1. Carrega a base de notícias
2. Vetoriza os textos usando TF-IDF
3. Treina o modelo Naive Bayes
4. Salva o modelo treinado
5. Executa a aplicação Flask
6. Recebe uma notícia do usuário
7. Realiza a previsão da classificação

---

# 📦 Instalação

Clone o repositório:

```bash id="yht6sk"
git clone https://github.com/seu-usuario/truthguard-ai.git
```

Entre na pasta:

```bash id="s7ph1m"
cd truthguard-ai
```

Instale as dependências:

```bash id="0nsp42"
pip install -r requirements.txt
```

---

# ▶️ Executando o Projeto

## 1. Treinar o modelo

```bash id="t0h97a"
python train_model.py
```

O treinamento irá:

* Processar a base de notícias
* Treinar o modelo
* Gerar:

  * `fake_news_model.pkl`
  * `vectorizer.pkl`

---

## 2. Executar a aplicação Flask

```bash id="dwyzt3"
python app.py
```

Acesse no navegador:

```bash id="m6vg4r"
http://127.0.0.1:5000
```

---

# 🧪 Modelo de Machine Learning

O projeto utiliza:

## Vetorização

* TF-IDF Vectorizer

## Algoritmo

* Multinomial Naive Bayes

---

# 📊 Exemplo de Uso

### Entrada

```text id="9b6g1r"
"Nova vacina cura todas as doenças em apenas 24 horas."
```

### Resultado

```text id="q39l2m"
❌ Possível Fake News
Confiança: 97.8%
```

---

# 📈 Melhorias Futuras

* [ ] Suporte a múltiplos idiomas
* [ ] Upload de arquivos
* [ ] Integração com APIs de fact-check
* [ ] Dashboard analítico
* [ ] Histórico de análises
* [ ] Deploy em nuvem
* [ ] Deep Learning com TensorFlow/PyTorch
* [ ] Análise de sentimento
* [ ] Sistema de usuários

---

# 🎯 Objetivo Educacional

Este projeto foi desenvolvido com foco em estudos de:

* Machine Learning
* NLP (Natural Language Processing)
* Flask
* Classificação de textos
* Inteligência Artificial

---

# ⚠️ Aviso

O modelo possui finalidade educacional e pode apresentar erros de classificação.

Não utilize como única fonte de verificação de informações.

---

# 👨‍💻 Autor

Desenvolvido por Guilherme Silva 🚀
