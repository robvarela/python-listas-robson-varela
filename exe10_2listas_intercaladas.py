# Exercício 10: Ler duas listas de dez elementos e gerar uma terceira intercalada
lista1 = []
lista2 = []
lista3 = []

print("--- Preenchimento da Lista 1 (10 elementos) ---")
for i in range(10):
  num = int(input(f"Digite o {i+1} número da Lista 1: "))
  lista1.append(num)

print("\n--- Preenchimento da Lista 2 (10 elementos) ---")
for i in range(10):
  num = int(input(f"Digite o {i+1} número da Lista 2: "))
  lista2.append(num)

# Intercalação dos elementos das duas listas
for i in range(10):
  lista3.append(lista1[i])
  lista3.append(lista2[i])

print("\n--- Resultados ---")
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (Intercalada):", lista3)
