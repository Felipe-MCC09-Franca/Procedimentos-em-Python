# Declaração de variáveis
z = float
y = float

def main():
    global z, y
    # Início
    z = float(input("Digite um valor real: "))
    y = float(input("Digite outro valor real: "))
    if z > y:
        print("O maior valor e:", z)
    else:
        print("O maior valor é:", y)

if __name__ == "__main__":
    main()
# Fim