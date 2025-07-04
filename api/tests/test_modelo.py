"""
Projeto Machine Learning Avaliação de Personalidade
Autor: Patricia Fraga Ferreira
Data: Julho/2025

Teste unitário automatizado para verificar se o modelo Naive Bayes
atinge acurácia mínima de 90% no conjunto de teste.

Carrega o modelo e dados, realiza predição e valida desempenho.
"""

import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def test_model_accuracy():
    # Carrega o modelo
    with open('api/model/modelo_nb.pkl', 'rb') as f:
        modelo = pickle.load(f)

    # Carrega os dados
    dataset = pd.read_csv('api/data/personality_datasert.csv')

    #Ajusta os tipos de dados
    dataset['Stage_fear'] = dataset['Stage_fear'].map({'Yes': 1, 'No': 0})
    dataset['Drained_after_socializing'] = dataset['Drained_after_socializing'].map({'Yes': 1, 'No': 0})

    # Define X e y
    X = dataset.iloc[:, 0:7].values
    y = dataset.iloc[:, 7].values

    # Parâmetros idênticos ao treino
    test_size = 0.20
    seed = 7

    # Faz o split exatamente igual
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, shuffle=True, random_state=seed, stratify=y
    )

    # Faz a predição
    y_pred = modelo.predict(X_test)

    # Calcula acurácia
    acc = accuracy_score(y_test, y_pred)
    print(f"Total de exemplos testados: {len(X_test)}")
    print(f"Acurácia: {acc:.3f}")

    # Verifica se passou no critério
    if acc >= 0.90:
        print("✅ Teste aprovado: acurácia está acima de 90%")
    else:
        print("❌ Teste falhou: acurácia abaixo de 90%")
    
    assert acc >= 0.90, f"Acurácia abaixo do esperado: {acc:.3f}"
