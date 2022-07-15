import  pygame
import estados from estado_inicial , estado1 , estado2 , estado3 , estado4 , estado5 , estado6 , estado7 , estado8 , estado9 , estado10 , estado_final

# definição do estado inicial 

# posição 0 = 3 m na e

# posição 1 = 3 c na e 

# posição 2 = 0 m na d

# posição 3 = 0 c na d 

# posição 4 = l do b 0 = e e 1 = d 

estadoinicial = [3, 3, 0, 0, 0]

# definição dos operadores 

# (1, 0) = atravessar 1 m 

# (1, 1) = atravessar 1 m e 1 c

# (2, 0) = atravessar 2 m 

# (0, 2) = atravessar 2 c

operadores = [(1,0), (1,1), (2,0), (0,2)]
        
# definição da borda ou fronterira da busca e a lista de estados visitados

borda = []
visitados = []

# função para mudar o barco de uma margem a outra, nst = estado atual, nm = numero de missionarios, nc = número de canibais

def andarbarco(nst,nm=0,nc=0): # limita o número de canibais e missionários a serem transportados.

  if nm + nc > 2:
    return

  # verifica o posicionamento do barco 

  if nst[-1] == 0: # barco na esqueda 

    mo = 0 # mo = posição dos missionarios na origem no vetor estadoinicial

    co = 1 # co = posição dos canibais na origem no vetor estadoinicial

    md = 2 # md = posição dos missionarios no destino no vetor estadoinicial

    cd = 3 # cd = posição dos canibais no destino no vetor estadoinicial

  else: #barco na direita

    mo = 2

    co = 3

    md = 0

    cd = 1
    
  if nst[mo] == 0 and nst[co] == 0: # caso não tenha o que transportar
    return
  
  nst[-1] = 1-nst[-1] # atulizando a posição do barco

  # transportar o missionarios 

  for i in range (min(nm,nst[mo])): # recebe o numero de missionários (nm), o estado atual dos missionários na origem (nst[mo])

    nst[mo] -= 1 # retira um missionario da origem 
    nst[md] += 1 # adciona um missinario no destino
    # limitando esta ação ao número de missionarios disponíveis na origem e ao limite de transporte do barco

    # transportar os canibais

  for i in range (min(nc,nst[co])): # recebe o numero de canibais (nc), o estado atual dos canibais na origem (nst[co])

    nst[co]-=1 # retira um canibal da origem 
    nst[cd]+=1 # adciona um canibal no destino 
    # limitando esta ação ao número de canibais disponíveis na origem e ao limite de transporte do barco

  return nst

# definimos a função sucessores para gerar os estados validos 

def sucessores(estado):

  sucessores = []

  for (i,j) in operadores: # para cada par ordenado definido anteriormente nos operadores possíveis deslocamos o barco

    s = andarbarco(estado[:], i,j) # puxamos também a quantidade de missinários e canibais que serão transportados

    if s == None: continue # se for vazio continua testando 

    if (s[0] < s[1] and s[0] > 0) or (s[2] < s[3] and s[2] > 0): continue # testa se tem mais canibal que missionário quando o n° de missionários 

    # for diferente de 0 para ambos os lados do rio eliminando os estados invalidos

    if s in visitados: continue # verifica se o sucessor já estava na lista de visitados para não registra-lo novamente

    sucessores.append(s) # se o estado passou por todas as condições ele é adcionado a lista

  return sucessores

sucessores(estadoinicial)

# definindo o nó adjacente
def adjacente(elementoanalisado):
  l = sucessores(elementoanalisado)
  if len(l) > 0:
    return l[0]
  else:
    return -1

# teste para saber se objetivo foi atingido
def testeobjetivo(estado):
  if estado[2] == 3 and estado[3] == 3:
    return True
  else:
    return False

 # Inicialindo o Pygame e criando.
    pygame . init ()
    display  =  pygame . exibir . set_mode ([ 1350 , 400 ])
    pygame . exibir . set_caption ( 'Missionários e Canibais' )
    objectGroup  =  pygame . sprite . Grupo ()
    estados  =  estado_inicial ( objectGroup )

# definindo a função de busca em profundidade 
def dfs(estadoinicial): # recebe o estado inicial 
  borda.append(estadoinicial) # adciona-o na borda
  while len(borda) != 0: # quando a borda estiver vazia ela procura o próximo elemento a analizar 
    elementoanalisado = borda[len(borda)-1] # retira da borda o elemento analizado
    if testeobjetivo(elementoanalisado): break # se ele for o estado objetivo ela para 
    v = adjacente(elementoanalisado) # se não for identifica-o como adjacente não visitado 
    if v == -1: # se v = -1 é porque não exite então ele é removido definitivamente
      borda.pop()
    else: # se não ele é adcionado aos visitados e a borda 
      visitados.append(v)
      borda.append(v)
  else: 
    print("caminho não encontrado, busca sem sucesso")
  return borda

    estados  =  estado1 ( objectGroup )
    estados  =  estado2 ( objectGroup )
    estados  =  estado3 ( objectGroup )
    estados  =  estado4 ( objectGroup )
    estados  =  estado5 ( objectGroup )
    estados  =  estado6 ( objectGroup )
    estados  =  estado7 ( objectGroup )
    estados  =  estado8 ( objectGroup )
    estados  =  estado9 ( objectGroup )
    estados  =  estado10 ( objectGroup )
    estados  =  estado_final ( objectGroup )
    gameLoop  =  Verdadeiro
    relógio  =  pygame . tempo . Relógio ()
    if  __name__  ==  '__main__' :
            while  gameLoop :
                relógio . marca ( 60 )
                para  evento  em  pygame . evento . obter ():
                    se  evento . tipo  ==  pygame . SAIR :
                        gameLoop  =  False

                #atualizar e desenhar
                exibir . preencher ([ 30 , 20 , 20 ])
                objectGrupo . atualização ()
                objectGrupo . desenhar ( exibir )
                pygame . exibir . atualização ()

sol = dfs(estadoinicial)

sol
