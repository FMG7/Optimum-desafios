## n tamanho da escada ##
n = int(input())

for i in range(n):
    ## imprime espacos livres ##
    for k in range(n-(i+1)):
        print(' ', end ='')
        
    ## imprime o degrau ##
    for j in range(i+1):
        print('#', end='')
    print()