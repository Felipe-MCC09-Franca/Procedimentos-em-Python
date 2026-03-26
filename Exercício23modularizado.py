# Declaração de variáveis
a = int
b = int
c = int
d = int

def main():
    global a, b, c, d
    # Início
    a = int(input("Digite o maior valor inteiro: "))
    b = int(input("Digite o segundo maior valor inteiro: "))
    c = int(input("Digite o terceiro maior valor inteiro: "))
    d = int(input("Digite outro valor inteiro: "))

    if d > a:
        print(d, a, b, c)
    elif d < a and d > b:
        print(a, d, b, c)
    elif d < b and d > c:
        print(a, b, d, c)
    else:
        print(a, b, c, d)

if __name__ == "__main__":
    main()

#Fim