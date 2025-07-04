# Projeto Machine Learning Avaliação de Personalidade - MVP
PuC - Pos Gradução em Engenharia de Software
Disciplina Qualidade de Software, Segurança e Sistemas Inteligentes
Autor: Patricia Fraga Ferreira
Data: Julho/2025

## Introdução 

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de classificar a personalidade do usuário como **Extrovertido(a)** ou **Introvertido(a)** a partir das respostas a um questionário simples.

A aplicabilidade prática inclui áreas como psicologia, recursos humanos, coaching e desenvolvimento pessoal, onde identificar traços de personalidade pode ajudar em processos de seleção, autoconhecimento, melhoria de equipes e personalização de serviços.

---

## Como Executar

⚠️ Execute todos os comandos a partir da pasta raiz do projeto.

1) Clone o repositório e acesse a pasta raiz:

git clone <link-do-repositório>
cd nome-da-pasta

2) Crie e ative um ambiente virtual:

python3 -m venv env
source env/bin/activate

3) Instale as dependências:

pip install -r requirements.txt

4) Rode os testes automatizados para validar a acurácia do modelo:

pytest -s api/tests/test_modelo.py

(Os resultados aparecerão no terminal e devem indicar uma acurácia acima de 90%.)

5) Execute o backend Flask:

FLASK_APP=api/app.py flask run --host 0.0.0.0 --port 5000

6) Abra o navegador e acesse:

http://localhost:5000/

    Responda ao questionário e veja a predição da sua personalidade!

---

##  Arquitetura da Solução

A aplicação é composta por três principais camadas e seus respectivos arquivos:

- **Notebook (Google Colab)**  
  - `modelo_personalidade.ipynb`: Responsável por todo o pipeline de machine learning — desde o carregamento dos dados até a exportação do modelo final (`modelo_nb.pkl`). Inclui análises detalhadas, gráficos, tuning e conclusão.

- **Back-end (Flask)**  
  - `api/app.py`: Carrega o modelo treinado e expõe uma rota `/prever` que recebe dados via POST (JSON) e retorna a predição da personalidade.
  - `modelo_nb.pkl`: Arquivo serializado do modelo Naive Bayes exportado do notebook.

- **Front-end (HTML + CSS + JavaScript)**  
  - `templates/index.html`: Página com o formulário do questionário para o usuário responder.
  - `static/style.css`: Define a estilização da página HTML.
  - `static/script.js`: Realiza o envio dos dados preenchidos no formulário para o back-end e exibe o resultado da predição ao usuário.

A comunicação entre front-end e back-end ocorre de forma assíncrona usando `fetch`, permitindo resposta em tempo real sem recarregar a página.


## Estrutura do Projeto

```
/api
    app.py
    modelo_nb.pkl
    data/
         personality_datasert.csv
    tests/
        test_modelo.py
    model/
        modelo_nb.pkl
/front
    /templates
        index.html
    /static
        estilo.css
        script.js
README.md
requirements.txt
```

---

## Sobre o Dataset

O conjunto de dados foi obtido no [Kaggle](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data/data) e contém respostas a um questionário sobre traços de personalidade.

- O dataset reúne dados comportamentais e sociais relacionados a traços de personalidade, especialmente voltados à distinção entre introversão e extroversão. Composto por 2.900 registros e 8 variáveis, o conjunto foi projetado para análise e modelagem de padrões de comportamento.
- Os dados foram coletados via **Google Forms** como parte de um projeto universitário.
- A variável alvo ("Introvertido(a)" ou "Extrovertido(a)") foi **autodeclarada** pelos próprios participantes.
- Embora as respostas apresentem padrão estruturado, o autor confirmou que os dados são reais, e não gerados sinteticamente.

---

## Descrição do Projeto

- Um modelo Naive Bayes foi treinado usando o dataset para classificar personalidades.
- Foram aplicadas boas práticas de pré-processamento, validação cruzada, otimização de hiperparâmetros e comparação com outros algoritmos clássicos.
- O modelo final apresenta acurácia média de aproximadamente 93,4%.
- A aplicação full stack permite ao usuário responder ao questionário no front-end e receber a classificação em tempo real via backend Flask.
- Um teste automatizado em PyTest garante que o modelo mantém o desempenho esperado e evita implantação de modelos inferiores.

---

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- Numpy
- PyTest
- HTML/CSS/JavaScript (Frontend)

---


## Notebook de Machine Learning

O notebook no Google Colab inclui:

- Carregamento e pré-processamento dos dados.
- Separacão treino/teste com holdout e validação cruzada.
- Treinamento e comparação dos modelos KNN, Decision Tree, Naive Bayes e SVM.
- Otimização de hiperparâmetros do Naive Bayes.
- Exportação do modelo final para uso no backend.
- Avaliação detalhada dos resultados
- Conclusão

# Link do notebook no Colab
https://colab.research.google.com/drive/1ijHSwRPTzj-gEeFcWqNS_eS6zK_4FFF_?usp=sharing

## Considerações sobre Segurança e Privacidade
Embora o foco deste trabalho seja acadêmico, reforça-se a relevância prática da solução desenvolvida. Modelos preditivos aplicados à análise de perfis de personalidade devem sempre considerar princípios éticos, privacidade dos dados e transparência nas decisões automatizadas.

Este projeto utiliza um dataset público do Kaggle, que não contém informações sensíveis nem dados que identifiquem os indivíduos. O processamento dos dados ocorre em tempo real no backend, sem armazenamento de informações pessoais, o que contribui para a anonimização e redução dos riscos de exposição.

Foram adotadas práticas básicas, como a coleta mínima necessária de dados e o uso restrito das informações apenas para predição. Entretanto, por se tratar de um MVP, algumas práticas essenciais para ambientes de produção — como autenticação de usuários, controle de acesso e proteção contra acessos não autorizados — ainda precisariam ser implementadas para garantir maior segurança e conformidade.

Essas medidas asseguram que a aplicação seja ética, segura e respeitosa com a privacidade, alinhando-se aos conceitos de desenvolvimento de software seguro aprendidos na disciplina. Mesmo utilizando dados públicos e anonimizados, é fundamental aplicar técnicas e práticas que garantam a segurança e a confidencialidade, reforçando o compromisso com a responsabilidade social no uso da inteligência artificial.

## Conclusão

Este projeto aplicou os conceitos de Machine Learning estudados na disciplina para desenvolver uma aplicação capaz de classificar perfis de personalidade com alto desempenho.

Seguindo as etapas essenciais de um pipeline de ML — da preparação dos dados à validação e avaliação final — foi possível identificar que o modelo Naive Bayes, mesmo com dados originais, oferece resultados consistentes e com baixa complexidade.

Com acurácia de 93% no conjunto de teste e F1-score equilibrado para ambas as classes, a solução mostra-se confiável para uso em contextos educacionais, laboratoriais ou experimentais em áreas como psicologia, coaching e recursos humanos.

A solução reforça a importância da ética, da transparência e do cuidado com dados sensíveis em projetos de inteligência artificial voltados ao comportamento humano.