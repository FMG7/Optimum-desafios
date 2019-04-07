## Constante inicial de altura
HEIGHT = 1

## Quantidade de casos ##
t = int(input())

for i in range(t):
    ## Numero de ciclos ##
    n = int(input())

    ## inicializacao da altura
    height = HEIGHT

    for j in range(n):
        if(j%2==0):
            ## se SUMMER ##
            height *= 2
        else:
            ## se SPRING ##
            height += 1
    ## Altura FINAL ##
    print(height)