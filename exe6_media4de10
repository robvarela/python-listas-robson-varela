# 6xercício 6: Média de dez alunos e contagem de notas maioe e igual a sete
medias = []
aprovados = 0

for i in range(10):
  print(f"\n--- Aluno {i+1} ---")
  soma = 0
  for j in range(4):
    nota = float(input(f"Digite a {j+1}ª nota: "))
    soma += nota

  # Calcula a média do aluno atual
  media = soma / 4
  medias.append(media)  # Armazena a média no vetor

  # Verifica se a média é maior ou igual a 7.0
  if media >= 7.0:
    aprovados += 1

print(f"\n--- Resultados Finais ---")
print(f"Vetor com as médias de todos os alunos: {medias}")
print(f"Número de alunos com média maior ou igual a 7.0: {aprovados}")
