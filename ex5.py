def elemntos_impares(v):
    temp = []
    for x in v:
        if(x % 2) != 0:
            temp.append(x)
    return x

v1 = [45, 89, 32, 12, 13]
print(f"Os elementos ímpares da lista são {elemntos_impares(v1)}")

