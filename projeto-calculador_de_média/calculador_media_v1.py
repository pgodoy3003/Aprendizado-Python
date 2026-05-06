x=0
while(x == 0):
    print("--Calculador de Média--")
    
    nota1 = float(input("Digite sua primeira nota:"))
    nota2 = float(input("Digite sua segunda nota:"))
    nota3 = float(input("Digite sua terceira nota:"))
    nota4 = float(input("Digite sua quarta nota:"))
    nota5 = float(input("Digite sua quinta nota:"))
    
    media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5 
    
    if(media <= 10 and media >= 7):
        print(f"Sua média é: {round(media,2)}\nParabens você foi aprovado!")
    
    elif(media <= 6 and media >= 5):
        print(f"Sua média é: {round(media,2)}\nParabens você foi aprovado, por pouco!")
    
    elif(media <= 4 and media >= 0):
        print(f"Sua média é: {round(media,2)}\n Infelizmente você foi reprovado ;-;")
    
    elif(media > 10 and media < 0):
        print(f"Os Valores que você inseriu, tente novamente.")
    x = int(input("Para calcular novamente digite 0 e para sair digite 1:"))
