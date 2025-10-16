
---

# 🧠 Projeto — Rede Neural para Predição de Aprovação de Estudantes

## 📌 Descrição

Este projeto utiliza **Redes Neurais Artificiais (RNA)** para prever se um estudante tem **alta ou baixa probabilidade de aprovação**, com base em **dados acadêmicos simulados**.
Ele foi desenvolvido em **Python** com foco educacional, apresentando uma **arquitetura limpa e modular**, permitindo fácil manutenção e expansão futura.

---

## 🧰 Tecnologias Utilizadas

* 🐍 **Python 3.12+**
* 📊 **Pandas** — manipulação de dados
* 🤖 **TensorFlow / Keras** — criação e treinamento da rede neural
* 📈 **Matplotlib / Seaborn** — visualização de dados e desempenho do modelo
* 🧪 **Scikit-learn** — divisão de dados e métricas de avaliação

---

## 🧭 Estrutura do Projeto

```
projeto-aprovacao/
│
├── data/
│   └── notas.csv                # Base de dados com informações de desempenho dos alunos
│
├── models/
│   └── neural_network.py        # Arquitetura da rede neural e função de treino
│
├── utils/
│   ├── preprocess.py            # Funções de pré-processamento de dados
│   └── evaluate.py              # Funções para avaliação do modelo
│
├── main.py                      # Arquivo principal que orquestra toda a execução
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação do projeto
```

---

## 🧱 Explicação dos Componentes

### 📂 `data/notas.csv`

* Contém os dados simulados de estudantes, incluindo:

  * Horas de estudo diárias
  * Frequência às aulas
  * Notas anteriores
  * Status final (Aprovado ou Reprovado)

---

### 🧠 `models/neural_network.py`

* Define a **arquitetura da rede neural** com:

  * Camada de entrada proporcional ao número de features
  * Duas camadas densas intermediárias
  * Camada de saída binária (aprovado / reprovado)
* Contém funções para:

  * Criar o modelo
  * Compilar com otimizador Adam e função de perda binária
  * Treinar com os dados pré-processados
  * Salvar e carregar pesos treinados

---

### 🧪 `utils/preprocess.py`

* Responsável por preparar os dados para a rede neural:

  * Leitura do CSV
  * Normalização e padronização de valores numéricos
  * Conversão de valores categóricos em numéricos (One-Hot Encoding / Label Encoding)
  * Divisão em **dados de treino e teste**

---

### 📊 `utils/evaluate.py`

* Faz a **avaliação do modelo**:

  * Calcula métricas de acurácia, precisão, recall e f1-score
  * Exibe matriz de confusão
  * Gera gráficos de desempenho para melhor interpretação dos resultados

---

### 🚀 `main.py`

* É o **ponto de entrada** da aplicação.
* Faz a chamada dos outros módulos para:

  1. Carregar e pré-processar os dados
  2. Treinar a rede neural
  3. Avaliar os resultados
  4. Exibir métricas e gráficos no terminal

---

## 🧪 Como Executar

### 1. Clonar ou descompactar o projeto

```bash
cd projeto-aprovacao
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o projeto

```bash
python main.py
```

---

## 📈 Resultados Esperados

* Exibição de métricas de desempenho da rede neural no terminal.
* Gráficos com histórico de **acurácia** e **perda (loss)** durante o treinamento.
* Matriz de confusão mostrando o desempenho da classificação.
* Modelo treinado capaz de prever aprovação com base nos dados de entrada.

---


## ✨ Autor

**Edwin Machaieie**
💻 Projeto educacional para aplicação prática de Redes Neurais Artificiais.

