# Declaração de variáveis
horaI = int
horaF = int
minI = int
minF = int
horaD = int
minD = int

def main():
    global horaI, horaF, minI, minF, horaD, minD
    # Início
    horaI = int(input("Digite a hora inicial do jogo: "))
    horaF = int(input("Digite a hora final do jogo: "))
    minI = int(input("Digite o minuto inicial do jogo: "))
    minF = int(input("Digite o minuto final do jogo: "))

    if horaI < horaF:
       horaD = horaF - horaI
    elif horaI > horaF:
       horaD = (24 - horaI) + horaF
    else:
       horaD = 0

    if minI < minF:
          minD = minF - minI
    elif minI > minF:
          minD = (60 - minI) + minF
          horaD = horaD - 1
    else:
          minD = 0

    print("Hora:", horaD, "minutos: ", minD)

if __name__ == "__main__":
    main()

#Fim