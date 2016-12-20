import random, sys, math
from time import time

#Las dos matrices necesarias


def matrizPesos(n):

#Primero cogemos los pesos de la matriz creada al leer el txt, añadiendo un cero al inicio

    matrizdePesos=[0]
    for i in range(len(n)):
        matrizdePesos.append(n[i][1])

#Ahora nos creamos una matriz con n+1 filas y columnas

    
    matriz = [[0 for i in range(len(n)+1)] for j in range (len(n)+1)]

#Aqui metemos en cada fila los valores de los pesos.  
    for i in range(len(n)+1):
        for j in range(len(matriz)):
            matriz[i][j]=matrizdePesos[j]
            
#Aqui en cada valor donde j=i, ejemplo 3-3, ponemos un cero.       
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(j==i):
                
                matriz[i][j] = 0
        
    return matriz

def matrizValores(n):

#Cargamos en nuestra matriz preparada todos los datos de valores


    matrizdeValores=[0]
    for i in range(len(n)):
        matrizdeValores.append((n[i][2]))
    
    matriz = [[0 for i in range(len(n)+1)] for j in range (len(n)+1)]

    for i in range(len(n)+1):
        for j in range(len(matriz)):
            matriz[i][j]=matrizdeValores[j]
            
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if(j==i):
                
                matriz[i][j] = 0
             
 

    return matriz
 
 
# Elige un paso para una hormiga, teniendo en cuenta los valores
# las feromonas y descartando los nodos ya visitados.
def eligeNodo(valors, ferom, visitados, soluciones):
    #Se calcula la tabla de pesos de cada ciudad
    listaValores  = []
    disponibles = []
    actual      = soluciones[-1]
 
    # Influencia de cada valor (alfa: feromonas; beta: valor)
    alfa = 1.0
    beta = 0.5
   

    # El parámetro beta (peso de los valores) es 0.5 y alfa=1.0
    for i in range(len(valors)):
        if i not in visitados: 
            fer  = math.pow((1.0 + ferom[actual][i]), alfa)
            peso = math.pow(1.0/valors[actual][i], beta) * fer
            disponibles.append(i)
            listaValores.append(peso)

    
    # Se elige aleatoriamente una de los nodos disponibles,
    # teniendo en cuenta su peso relativo.
    valor     = random.random() * sum(listaValores)
    acumulado = 0.0
    i         = -1
    while valor > acumulado:
        i         += 1
        acumulado += listaValores[i]
 
 
    return disponibles[i]
  
 
# Genera una " hormiga " , que eligirá un camino (nodos que visita) teniendo en cuenta
# los valores y los rastros de feromonas. Devuelve una tupla
# con el camino (nodos visitados) y su longCamino (Suma de valores).
def eligeCamino(matriz, matrizPesos, feromonas, pesoMochila):
    # El nodo inicial siempre es el 0
    camino     = [0]
    visitados  = [0]
    longCamino = 0
 
    # Elegir cada paso según los valores y las feromonas
    while len(visitados) < len(matriz):
        nodo      = eligeNodo(matriz, feromonas, visitados, camino)
               
        camino.append(nodo)
        
        valorActual = 0
        for x in range(len(camino)):
        
                if x != 0:
                    valorActual = valorActual + matrizSinTransformar[camino[x]-1][2]
       
        pesoActual = 0
        for x in range(len(camino)):
                pesoActual = pesoActual + matrizPesos[0][camino[x]]
                
       
        if (pesoActual > pesoMochila):
            camino.remove(nodo)
         
        else:
            longCamino = pesoActual / valorActual
          
        visitados.append(nodo)
   
 
    return (camino, longCamino)
 
# Actualiza la matriz de feromonas siguiendo el camino recibido
def rastroFeromonas(feromonas, camino, dosis):
   for i in range (len(camino) - 1):
       feromonas[camino[i]][camino[i+1]] += dosis
 
# Evapora todas las feromonas multiplicándolas por una constante
# = 0.9 ( en otras palabras, el coefienciente de evaporación es 0.1)
def evaporaFeromonas(feromonas):    
   for lista in feromonas:
        for i in range(len(lista)):
            lista[i] *= 0.9
 
 
# Resuelve el problema del viajante de comercio mediante el
# alforitmo de la colonia de hormigas. Recibe una matriz de
# distancias y devuelve una tupla con el mejor camino que ha
# obtenido (lista de índices) y su longitud
def hormigas(matriz, matrizPesos, iteraciones, pesoMochila):
    # Primero se crea una matriz de feromonas vacía
    n = len(matriz)
    feromonas = [[0 for i in range(n)] for j in range(n)]
   
    # El mejor camino y su longitud (inicialmente "infinita")
    mejorCamino     = []
    longMejorCamino = sys.maxsize
   
    # En cada iteración se genera una hormiga, que elige una camino,
    # y si es mejor que el mejor que teníamos, deja su rastro de
    # feromonas (mayor cuanto más corto sea el camino)
    hormiga = 1
    for iter in range(iteraciones):
        controlHormiga = hormiga % 100
        if controlHormiga == 000:
            print ("Hormigas: ", hormiga)
            
        hormiga = hormiga + 1
        (camino,longCamino) = eligeCamino(matriz, matrizPesos, feromonas, pesoMochila)
     #   print(longCamino)      
        if longCamino <= longMejorCamino:
            mejorCamino     = camino
            longMejorCamino = longCamino
        #print("longCamino: ",longCamino)
        dosis = (pesoMochila/longCamino)
        rastroFeromonas(feromonas, camino, dosis)
        # En cualquier caso, las feromonas se van evaporando
        evaporaFeromonas(feromonas)
         
    # Se devuelve el mejor camino que se haya encontrado
    peso = 0
    for x in range(len(mejorCamino)):
            peso = peso + matrizPesos[0][mejorCamino[x]]
    return (mejorCamino, longMejorCamino, peso)
 
 
                                 
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Cargamos las matriz del txt')
f = open('03-exemplo7b.txt')
# Primera lectura para obviar la cabecera
f.readline()
# Cargamos los datos
data = f.read().strip()
# Se cierra el fichero
f.close()
#Separamos los datos en un array
matrizSinTransformar = [[int(num) for num in line.strip().split()] for line in data.split('\n')]


#consiguiendo las matrices que necesitamos para resolver el problema
matrizDePesos = matrizPesos(matrizSinTransformar)
matrizDeValores = matrizValores(matrizSinTransformar)

 
# Obtención del mejor camino, las iteraciones son la cantidad de hormigas que empleamos para resolverlo
#Iteraciones
numHormigas = 10000

pesoMochila = 14
print("Llamamos a las hormigas para que resuelvan el problema")
start_time = time()
(camino, longCamino, peso) = hormigas(matrizDeValores,matrizDePesos, numHormigas, pesoMochila)
elapsed_time = time() - start_time
camino.remove(0)
print("Numero de hormigas usadas: ", numHormigas)
print("Tiempo de ejecución: %.10f seconds." % elapsed_time)
print("Nuestra mochila puede cargar con ", pesoMochila, "kilos")
print("Longitud del camino basado en la suma de pesos entre valores: ", longCamino)
print("SOLUCIÓN AL POBLEMA: ", camino)
print("PESO DE LA MOCHILA SOLUCIÓN: ", peso)
valorTotal = 0
for x in range(len(camino)):
            valorTotal = valorTotal + matrizSinTransformar[camino[x]-1][2]
print("VALOR DE LA MOCHILA SOLUCIÓN:", valorTotal)

#print("real long", longCamino)
