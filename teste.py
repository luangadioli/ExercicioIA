import math

matriz = [[2,0,0,0,0],
          [0,0,1,1,0],
          [0,0,0,1,0],
          [1,0,1,0,3],
          [1,0,0,0,0]
          ]

posicaoFinal = [4, 3]

matriz2 = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]
          ]

def calculaDistancia(x , y , posicaoFinal):
    distancia = math.sqrt(pow(posicaoFinal[0] - x , 2) + pow(posicaoFinal[1] - y , 2)) 
    return float("{:.1f}".format(distancia))

for y in range(len(matriz)):
    for x in range(len(matriz[0])):
        if matriz[y][x] == 1:
            matriz2[y][x] = 10.0 
        else: 
            matriz2[y][x] = calculaDistancia(x, y, posicaoFinal)



print(matriz2)


[
    [5.0,  4.2, 3.6,  3.2,  3.0], 
    [4.5,  3.6, 10.0, 10.0, 2.0], 
    [4.1,  3.2, 2.2,  10.0, 1.0], 
    [10.0, 3.0, 10.0, 1.0,  0.0], 
    [10.0, 3.2, 2.2,  1.4,  1.0]
]