import math

# Declaração de variáveis
a = float
b = float
c = float
raiz1 = float
raiz2 = float
delta = float

def main():
    global a, b, c, raiz1, raiz2, delta
    # Início
    a = float(input("Digite o valor de A: "))
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = ((b**2) - (4 * a * c))

    if delta < 0:
        print("Não existem raízes reais")
    elif delta == 0:
        raiz1 = ((-b + math.sqrt(delta)) / (2 * a))
        print("O valor das raízes são: ", raiz1)
    else:
        raiz1 = ((-b + math.sqrt(delta)) / (2 * a))
        raiz2 = ((-b - math.sqrt(delta)) / (2 * a))
        print("O valor da primeira raiz é:", raiz1, "e o da segunda raiz é:", raiz2)

if __name__ == "__main__":
    main()

#Fim