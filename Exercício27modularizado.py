# Declaração de variáveis
nvoltas = int
ecircuitos = int
t = int
vmedia = float

def calcular_vmedia(nvoltas, ecircuitos, t):
    # Início
    vmedia = ((ecircuitos * nvoltas) / t) * 0.06
    print (("A velocidade média é de:"),vmedia, ("km/h"))

def main():
    nvoltas = int(input("Digite o número de voltas: "))
    ecircuitos = int(input("Digite a extensão do circuito em metros: "))
    t = int(input("Digite o tempo de duração em minutos: "))
    calcular_vmedia(nvoltas, ecircuitos, t)

if __name__ == "__main__":
    main()

#Fim