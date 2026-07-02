import numpy as np

print("="*60)
print("MODELAGEM DE REDE DE DISTRIBUIÇÃO DE ÁGUA")
print("Aplicação de Álgebra Linear")
print("="*60)

# Entrada de dados
print("\nDigite a demanda de água em cada nó (L/s):")

d1 = float(input("Nó 1: "))
d2 = float(input("Nó 2: "))
d3 = float(input("Nó 3: "))

# Matriz dos coeficientes
A = np.array([
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 1]
], dtype=float)

b = np.array([d1, d2, d3])

# Exibe a matriz
print("\nMATRIZ DOS COEFICIENTES")
print(A)

# Determinante
det = np.linalg.det(A)

print("\nDETERMINANTE")
print(f"Det(A) = {det:.2f}")

if det == 0:
    print("O sistema não possui solução única.")
else:

    # Resolve o sistema
    x = np.linalg.solve(A, b)

    print("\nVAZÕES ENCONTRADAS")
    print(f"Q1 = {x[0]:.2f} L/s")
    print(f"Q2 = {x[1]:.2f} L/s")
    print(f"Q3 = {x[2]:.2f} L/s")

    # Espaço vetorial
    print("\nESPAÇO VETORIAL")

    v1 = np.array([1,0,1])
    v2 = np.array([1,1,0])
    v3 = np.array([0,1,1])

    print("v1 =", v1)
    print("v2 =", v2)
    print("v3 =", v3)

    # Subespaço
    print("\nSUBESPAÇO VETORIAL")
    print("Gerado pelos vetores v1 e v2.")

    # Base
    print("\nBASE DO SUBESPAÇO")
    print("{v1, v2}")

    # Combinação Linear
    print("\nCOMBINAÇÃO LINEAR")

    a = float(input("Digite o coeficiente de v1: "))
    c = float(input("Digite o coeficiente de v2: "))

    resultado = a*v1 + c*v2

    print("\nResultado da combinação linear:")
    print(resultado)

    # Verificação
    print("\nVERIFICAÇÃO")
    print("A*x =")
    print(A @ x)

print("\nPrograma encerrado.")
