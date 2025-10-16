import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def carregar_dados():
    df = pd.read_csv("data/alunos.csv")
    X = df[["idade", "horas_estudo", "freq_leitura", "uso_ia"]]
    y = df["aprovado"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
