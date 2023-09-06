
#def define que os códigos dentro do seu bloco só serão chamados quando a função for lida, no caso jogo();
def jogo():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************")

    print("Fim do jogo")

#esse if foi criado pensando na flexibilidade do arquivo, sem o IF e a função sendo chamada esse arquivo só pode ser aberto se for importado para outro, tendo a função é possível chamar ela diretamente pelo cmd ou interpretador py, o IF ajuda o arquivo a não ser chamado por completo quando importado, a palavra __main__ se estiver preenchida indica que o arquivo foi aberto diretamente como o arquivo principal(main)
if(__name__ == "__main__"):
    jogo()