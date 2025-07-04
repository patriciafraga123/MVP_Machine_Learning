"""
Projeto Machine Learning Avaliação de Personalidade
Autor: Patricia Fraga Ferreira
Data: Julho/2025

Backend Flask para classificar personalidade como Extrovertido(a) ou Introvertido(a)
a partir das respostas do questionário. Usa modelo Naive Bayes treinado.

Rotas:
- '/'           : página principal (front-end)
- '/prever'     : endpoint para receber dados e retornar predição
"""


from flask import Flask, request, jsonify, render_template, send_from_directory
import pickle
import numpy as np

app = Flask(
    __name__,
    static_folder='../front/static',      # pasta CSS, JS, imagens
    template_folder='../front/templates'  # pasta HTML, se usar templates
)

# Carrega modelo
with open('api/model/modelo_nb.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Mapeamento do output do modelo para texto em portugues
labels = {
    'Introvert': 'Introvertido(a)',
    'Extrovert': 'Extrovertido(a)'
}

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/prever', methods=['POST'])
def prever():
    dados = request.get_json()

    
    entrada = dados.get('entrada', None)

    if entrada is None:
        return jsonify({'erro': 'Nenhuma entrada fornecida'}), 400

    
    entrada_array = np.array(entrada).reshape(1, -1)

    # Faz a predição
    predicao = modelo.predict(entrada_array)

    # Busca o resultado no dicionário usando a string retornada pelo modelo
    resultado = labels.get(predicao[0], 'Indefinido')

    return jsonify({'predicao': resultado})

if __name__ == '__main__':
    app.run(debug=True)
