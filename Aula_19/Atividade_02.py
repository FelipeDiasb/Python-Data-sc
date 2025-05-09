import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Gerar dados sintéticos
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # variável independente
y = 4 + 3 * X + np.random.randn(100, 1)  # variável dependente com ruído

# 2. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Criar e treinar o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Fazer previsões
y_pred = model.predict(X_test)

# 5. Avaliar o modelo
print("Coeficiente angular (inclinação):", model.coef_[0])
print("Coeficiente linear (intercepto):", model.intercept_)
print("Erro quadrático médio (MSE):", mean_squared_error(y_test, y_pred))
print("Coeficiente de determinação (R²):", r2_score(y_test, y_pred))

# 6. Visualizar os resultados
plt.scatter(X_test, y_test, color='blue', label='Dados reais')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Previsão')
plt.title('Regressão Linear com scikit-learn')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
