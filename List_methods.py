cesta_letra = ["a","b","c","d","e","a","b"]
cesta = [1,2,3,4,5]
#len retorna o numero de itens numa lista
#print(len(cesta))
#----------------------------------------------------------------------


#adição
#nova_lista = cesta.append(100)
#print(cesta)
#----------------------------------------------------------------------


#o append modifica a lista cesta, não cria uma nova, por isso nesse caso ele consta none, a menos que façamos a atribuição das listas através do operador =
#nova_lista = cesta 
#print(nova_lista)
#----------------------------------------------------------------------


#insert adiciona um objeto em qualquer lugar da lista - insert(index, object)
#cesta.insert(1,100)
#print(cesta)
#----------------------------------------------------------------------


#extend permite uma iteração (++) bem como permite extender a lista esse módulo também não gera uma nova lista, ele apenas modifica a existente
#nova_lista = cesta.extend([100])
#print(cesta)
#print(nova_lista)
#----------------------------------------------------------------------



#METODOS DE REMOÇÃO
#pop remove um objeto do array através do índice, se estiver vazio remove o ultimo
#cesta.pop()
#cesta.pop(2)
#print(cesta)
#----------------------------------------------------------------------
#remove deleta o objeto definido entre os parenteses.
#cesta.remove(5)
#print(cesta)
#----------------------------------------------------------------------

#clear limpa totalmente o array selecionado.
#nova_lista = cesta.clear()
#print(cesta)
#----------------------------------------------------------------------


#POSIÇÃO
#index entrega o índice do objeto procurado, o primeiro parâmetro é o objeto-alvo, o segundo é em que índice a pesquisa vai começar, e o terceiro é em que indice a pesquisa para.
#print(cesta_letra.index("b"))
#----------------------------------------------------------------------

#in é uma keyword que pode ser usada para pesquisar dentro de uma lista por algo. No caso abaixo o código procura se há D dentro de cesta_letra e informa se é true ou false
#print("d" in cesta_letra)
#print("eu" in "eu disse olá mundo")
#----------------------------------------------------------------------

#count conta quantas vezes o objeto ocorreu numa lista
#print(cesta_letra.count("d"))
#print("eu não sei se eu o fiz".count("eu"))
#----------------------------------------------------------------------

#Sort ordena a lista sem criar uma nova, diferente da função sorted que ordena e cria um novo array
# cesta_letra.sort() 
#Reverse o nome já entrega, ele inverte os índices. no final usando um corte de array [::] e adicionando -1 ele inverteu novamente, no final teremos um resultado normal.
# cesta_letra.reverse()
# print(cesta_letra[::-1])
#----------------------------------------------------------------------

#range cria uma lista com o tamanho indicado.
#print(list(range(1, 100)))
#----------------------------------------------------------------------

#join junta string com array etc.
# nova_frase = " ".join(["oi", "meu", "nome", "é", "dudu"])
# print(nova_frase)
#----------------------------------------------------------------------

#desempacotamento de lista serve para atribuirmos uma variável ao objeto dentro da lista rapidamente, permitindo que a gente separe os objetos que queremos e deixemos o restante da lista como está.
# a,b,c, * outros, d = [1,2,3,4,5,6,7,8,9]

# print(a)
# print(outros)
#----------------------------------------------------------------------


