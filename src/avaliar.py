import tensorflow as tf
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd

model = tf.keras.models.load_model("modelo_aprovacao.h5")

novo_aluno = np.array([[20, 2.0, 2, 3]])

df = pd.read_csv("data/alunos.csv")
scaler = StandardScaler().fit(df[["idade", "horas_estudo", "freq_leitura", "uso_ia"]])
novo_aluno_scaled = scaler.transform(novo_aluno)

prob = model.predict(novo_aluno_scaled)[0][0]
print(f"Probabilidade de aprovação: {prob:.2f}")
print("✅ Aprovado" if prob >= 0.5 else "❌ Reprovado")
