# Declaração de variáveis
x = int

def main():
    global x
    # Início
    x = int(input("Digite um valor inteiro: "))

    if x % 2 == 0 and x % 3 == 0:
        print(x, "é divisível por 2 e por 3")
    else:
        print(x, "não é divisível por 2 e por 3")

if __name__ == "__main__":
    main()

#Fim