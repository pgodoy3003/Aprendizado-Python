nDigitado = int(input("Qual número deseja ver a tabuada? \n"))

print(f"---Tabuada do {nDigitado}---")

for i in range(1, 11):
    resultado = nDigitado * i
    print(f"{nDigitado} x {i} = {resultado}")