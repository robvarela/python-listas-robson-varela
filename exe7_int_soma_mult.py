# exercício 7: Ler cinco números inteiros, mostrar a soma, a multiplicação e os numeros
numeros = []
soma = 0
multiplicacao = 1

for i in range(5):
  num = int(input(f"Digite o {i+1} número inteiro: "))
  numeros.append(num)
  soma += num
  multiplicacao *= num

print("\n--- Resultados ---")
print("Números introduzidos:", numeros)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
