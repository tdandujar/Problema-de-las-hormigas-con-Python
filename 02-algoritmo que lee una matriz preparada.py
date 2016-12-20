import random, sys, math
 
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
# con el camino (nodos solucion) y su longCamino (Suma de valores).
def eligeCamino(matriz, feromonas):
    # El nodo inicial siempre es el 0
    camino     = [0]
    visitados  = [0]
    longCamino = 0
 
    # Elegir cada paso según los valores y las feromonas
    while len(visitados) < len(matriz):
        nodo      = eligeNodo(matriz, feromonas, visitados, camino)
        
      #  print("camino: ", longCamino)
      
        camino.append(nodo)
        longCamino += matriz[visitados[-1]][nodo]
        if (longCamino > 20):
            camino.remove(nodo)
            longCamino -= matriz[visitados[-1]][nodo]
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
def hormigas(matriz, iteraciones, distMedia):
    # Primero se crea una matriz de feromonas vacía
    n = len(matriz)
    feromonas = [[0 for i in range(n)] for j in range(n)]
   
    # El mejor camino y su longitud (inicialmente "infinita")
    mejorCamino     = []
    longMejorCamino = sys.maxsize
   
    # En cada iteración se genera una hormiga, que elige una camino,
    # y si es mejor que el mejor que teníamos, deja su rastro de
    # feromonas (mayor cuanto más corto sea el camino)
    for iter in range(iteraciones):
        (camino,longCamino) = eligeCamino(matriz, feromonas)
       
        if longCamino <= longMejorCamino:
            mejorCamino     = camino
            longMejorCamino = longCamino
           
        rastroFeromonas(feromonas, camino, distMedia/longCamino)
        # En cualquier caso, las feromonas se van evaporando
        evaporaFeromonas(feromonas)
         
    # Se devuelve el mejor camino que se haya encontrado

    return (mejorCamino, longMejorCamino)
 
 
                                 
# Mostramos por pantalla lo que leemos desde el fichero
print('>>> Cargamos la matriz de los txts')
f = open('01-exemplo3.txt')
# Primera lectura para obviar la cabecera
print(f.readline())
# Cargamos los datos
data = f.read().strip()
# Se cierra el fichero
f.close()
#Separamos los datos en un arrya
M = [[int(num) for num in line.strip().split()] for line in data.split('\n')]
print (M)
 
 
 
 
# Ejemplo de uso    
# Generación de una matriz de prueba
numCiudades      = 4
distanciaMaxima  = 10
 
# Obtención del mejor camino, las iteraciones son la cantidad de hormigas que empleamos para resolverlo
iteraciones = 5
distMedia   = numCiudades*distanciaMaxima/2
(camino, longCamino) = hormigas(M, iteraciones, distMedia)
print("Camino: ", camino)
print("Longitud del camino: ", longCamino)
