# Declaração de variáveis
nota1 = int
nota2 = int
nota3 = int
nota4 = int
media = float

def main():
    global nota1, nota2, nota3, nota4, media
    # Início
    nota1 = int(input("Digite a nota do primeiro bimestre: "))
    nota2 = int(input("Digite a nota do segundo bimestre: "))
    nota3 = int(input("Digite a nota do terceiro bimestre: "))
    nota4 = int(input("Digite a nota do quarto bimestre: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 6:
        print("APROVADO")
    elif media >= 3 and media < 6:
        print("EXAME")
    else:
        print("RETIDO")

if __name__ == "__main__":
    main()

#Fim