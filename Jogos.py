import forca
import adivinha

def escolhe_jogo():
    print("*********************************")
    print("    Escolha o jogo desejado!")
    print("*********************************")

    print("(1)Forca (2)Adivinhação")

    choice = int(input("Digite o número do jogo desejado: "))


    if (choice == 1):
        print("Jogo da forca")
        forca.jogo()
    elif (choice == 2):
        print("Jogo da Adivinhação")
        adivinha.jogo()

if(__name__ == "__main__"):
    escolhe_jogo()    