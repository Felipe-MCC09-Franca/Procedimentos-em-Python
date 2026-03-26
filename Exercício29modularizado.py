# Declaração de variáveise
tipoi = int
valori = float
valorc = float

def calcular_investimento(tipoi, valori):
    # Início
    if tipoi == 1:
        valorc = valori + (valori * 0.03)
        print("O valor corrigido em 30 dias é de:",valorc)
    elif tipoi == 2:
        valorc = valori + (valori * 0.05)
        print("O valor corrigido em 30 dias é de:",valorc)

def main():
    tipoi = int(input("Digite o tipo de investimento: "))
    valori = float(input("Digite o valor do investimento: "))
    calcular_investimento(tipoi, valori)

if __name__ == "__main__":
    main()

#Fim