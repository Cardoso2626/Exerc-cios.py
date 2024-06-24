def indice_par(v):
    temp = []
    for x in v:
        if (x%2) == 0:
            temp.append(x)
    return temp


v1 = [45, 89, 32, 12, 13]
print(indice_par(v1))