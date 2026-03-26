# Declaração de variáveis
precoA = float
mediaM = int
precoN = float

def calcular_reajuste(precoA, mediaM):
    # Início
    if mediaM < 500 and precoA < 30.00:
        precoN = precoA + (precoA * 0.10)
    elif (mediaM >= 500 and mediaM < 1000) and (precoA >= 30.00 and precoA < 80.00):
        precoN = precoA + (precoA * 0.15)
    elif mediaM >= 1000 and precoA >= 80.00:
        precoN = precoA - (precoA * 0.05)
    else:
        precoN = precoA

    print ("O novo preço será de:", precoN)

def main():
    precoA = float(input("Digite o preço atual do produto: "))
    mediaM = int(input("Digite a média mensal do produto: "))
    calcular_reajuste(precoA, mediaM)

if __name__ == "__main__":
    main()

#Fim