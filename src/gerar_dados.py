import pandas as pd
import random

def gerar_dados(n=200):
    dados = []
    for _ in range(n):
        idade = random.randint(16, 30)
        horas_estudo = round(random.uniform(0, 5), 1)
        freq_leitura = random.randint(0, 7)
        uso_ia = random.randint(0, 7)
        aprovado = 1 if (horas_estudo >= 2 or freq_leitura >= 3) and uso_ia <= 5 else 0
        dados.append([idade, horas_estudo, freq_leitura, uso_ia, aprovado])

    df = pd.DataFrame(dados, columns=["idade", "horas_estudo", "freq_leitura", "uso_ia", "aprovado"])
    df.to_csv("data/alunos.csv", index=False)
    print("✅ Dataset gerado com sucesso!")

if __name__ == "__main__":
    gerar_dados()
