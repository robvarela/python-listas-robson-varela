# Exercicio 2: leia 10 números reais e mostre na ordem inversa
reais = []

for i in range(10):
  num = float(input(f"Digite o {i+1}º número real: "))
  reais.append(num)

reais.reverse()  # Inverte a ordem dos elementos guardados na lista
print("\nNúmeros na ordem inversa:", reais)
