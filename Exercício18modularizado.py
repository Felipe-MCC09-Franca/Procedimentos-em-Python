# Declaração de variáveis
z = int
y = int
dif = int

def main():
    global z, y, dif
    # Início
    z = int(input("Digite um valor inteiro: "))
    y = int(input("Digite outro valor inteiro: "))
    if z > y: 
        dif = z - y
        print("A diferença é:", dif)
    else:
        dif = y - z
        print("A diferença é:", dif)

if __name__ == "__main__":
    main()

# Fim