import tensorflow as tf
from src.preprocessamento import carregar_dados

def treinar_modelo():
    X_train, X_test, y_train, y_test = carregar_dados()

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)

    loss, acc = model.evaluate(X_test, y_test)
    print(f"✅ Acurácia no teste: {acc:.2f}")

    model.save("modelo_aprovacao.h5")
    print("📁 Modelo salvo com sucesso!")

if __name__ == "__main__":
    treinar_modelo()
