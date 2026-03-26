# Declaração de variáveis
x = int
y = int

def main():
    global x, y
    # Início
    x = int(input("Digite um valor inteiro: "))
    y = int(input("Digite outro valor inteiro: "))

    if x > y:
        if x % y == 0:
            print(x, "é múltiplo de", y)
        else:
            print(x, "não é múltiplo de", y)
    elif y % x == 0:
            print(y, "é múltiplo de", x)
    else:
         print(y, "não é múltiplo de", x)

if __name__ == "__main__":
    main()

#Fim