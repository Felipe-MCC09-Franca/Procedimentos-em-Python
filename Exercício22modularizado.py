# Declaração de variáveis
x = int
y = int

def main():
    global x, y
    # Início
    x = int(input("Digite um valor inteiro: "))
    y = int(input("Digite OUTRO valor inteiro: "))

    if x > y:
        print(y, ",", x)
    else:
        print(x, ",", y)

if __name__ == "__main__":
    main()

#Fim