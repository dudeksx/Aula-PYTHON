import random


#def define que os códigos dentro do seu bloco só serão chamados quando a função for lida, no caso jogo();
def jogo():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    #Define qual régua de números será usada, no caso de 1 até 100
    numero_secreto = random.randrange(1,101)
    #------------------------------------------------------------
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    #Recebe o número digitado pelo player e então converte em inteiro.
    nivel = int(input("Defina o nível: "))
    #------------------------------------------------------------

    #O bloco abaixo analisa o inteiro digitado e define o número de tentativas baseado num sistema de dificuldade
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    #------------------------------------------------------------

    #Define o total de rodadas baseado na dificuldade, mostra o número do chute e analisa se o player chutou fora da régua de números
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
    #-------------------------------------------------------------

    #Define se a pessoa acertou, se chutou muito alto ou muito baixo. E define a quantidade de pontos do Player
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    #----------------------------------------------------------------


    print("Fim do jogo")

#esse if foi criado pensando na flexibilidade do arquivo, sem o IF e a função sendo chamada esse arquivo só pode ser #aberto se for importado para outro, tendo a função é possível chamar ela diretamente pelo cmd ou interpretador py, o IF #ajuda o arquivo a não ser chamado por completo quando importado, a palavra __main__ se estiver preenchida indica que o #arquivo foi aberto diretamente como o arquivo principal(main)

if(__name__ == "__main__"):
    jogo()