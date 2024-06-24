def elementos_negativos(v):
    temp = []
    for x in v:
        if x < 0:
            temp.append(x)
    return temp

v1 = [-45, 89, 32, -12, 13]
print(f"O primeiro elemento do vetor é {elementos_negativos(v1)}")