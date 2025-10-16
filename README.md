
---
Uma Rede Neural Artificial (RNA) é um modelo computacional inspirado no funcionamento do cérebro humano, criado para reconhecer padrões, aprender com dados e tomar decisões automaticamente.

Ela é composta por camadas de neurônios artificiais (nós matemáticos) conectados entre si, que processam informações e “aprendem” com exemplos.

Entrada (Input) 🧾

A rede recebe dados brutos (por exemplo: horas de estudo, idade, uso de IA).

Cada característica vira um número que entra na rede.

Camadas Ocultas (Hidden Layers) 🧮

Os neurônios nessas camadas combinam e transformam as informações.

É aqui que a rede “aprende” padrões — por exemplo: alunos que estudam mais têm mais chance de aprovação.

Saída (Output) ✅❌

A rede gera uma previsão final (exemplo: 1 = aprovado, 0 = reprovado).

Pode ser também uma probabilidade (ex: 0.85 = 85% de chance de aprovação).

Treinamento

A rede compara sua previsão com o resultado real e calcula o erro.

Ajusta os “pesos” das conexões para melhorar as próximas previsões.

Esse processo é repetido muitas vezes até a rede ficar precisa.
# 🧠 Projeto — Rede Neural para Predição de Aprovação de Estudantes

## 📌 Descrição

## 🧠 Visão Geral

Este projeto utiliza Machine Learning com Redes Neurais (TensorFlow/Keras) para prever a probabilidade de aprovação de um aluno com base em seus hábitos de estudo, uso de inteligência artificial e frequência de leitura.

A ideia é demonstrar como uma rede neural pode identificar padrões em dados educacionais e fornecer insights sobre comportamento de estudo.

## 🧾 Problema a Resolver

Muitos estudantes têm diferentes formas de estudar — alguns leem livros, outros utilizam IA para obter respostas rápidas.
A pergunta que queremos responder é:

📌 “Como os hábitos de estudo (leitura, tempo de estudo e uso de IA) influenciam no resultado final dos alunos?”

Com base nisso, criamos um modelo preditivo que classifica os alunos em:

✅ Aprovado

❌ Reprovado

---

## 🧮 Como a Rede Neural Funciona

1. **Entrada (Features)**

   * `idade` → idade do aluno
   * `horas_estudo` → média de horas de estudo por dia
   * `freq_leitura` → frequência de leitura de livros por semana
   * `uso_ia` → frequência de uso de IA para estudar

2. **Camadas da Rede Neural** (modelo sequencial Keras)

   * Camada de entrada com 4 neurônios
   * Camada oculta (Dense) com ativação ReLU
   * Camada de saída com ativação Sigmoid (retorna valor entre 0 e 1)

3. **Saída (Label)**

   * `aprovado` → 1 (aprovado) ou 0 (reprovado)

4. **Função de perda:** Binary Crossentropy

5. **Otimizador:** Adam

6. **Métrica:** Acurácia

---
## 📊 Exemplo de Dados Gerados

| idade | horas_estudo | freq_leitura | uso_ia | aprovado |
| ----- | ------------ | ------------ | ------ | -------- |
| 18    | 2.5          | 4            | 2      | 1        |
| 23    | 1.0          | 1            | 6      | 0        |
| 20    | 3.0          | 3            | 2      | 1        |

---

## 📈 Resultados

* A rede neural aprende a identificar o padrão entre **bons hábitos de estudo** e **resultados positivos**.
* Alunos com mais tempo de estudo e leitura apresentam maior chance de aprovação.
* Uso excessivo de IA sem leitura correlaciona-se a reprovação.

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
git clone Rede-Neural-para-Predi-o-de-Aprova-o-de-Estudantes.git
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

