x = 0

while(x == 0):

    print("\n-- Calculador de Média --")

    quantidade = int(input("Quantas notas você deseja calcular? (1 até 10): "))

    if quantidade < 1 or quantidade > 10:
        print("Quantidade inválida! Digite um número entre 1 e 10.")
        continue

    soma = 0

    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i + 1}: "))

        if nota < 0 or nota > 10:
            print("Nota inválida! As notas devem estar entre 0 e 10.")
            break

        soma += nota

    else:
        media = soma / quantidade

        print(f"\nSua média foi: {round(media, 2)}")

        if media >= 7:
            print("Parabéns, Aprovado!")

        elif media >= 5:
            print("Aprovado por pouco!")

        else:
            print("Infelizmente Reprovado.")

    x = int(input("\nDigite 0 para calcular novamente ou 1 para sair: "))

print("\nPrograma encerrado.")