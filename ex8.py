def valor_existe(vetor, valor):
    return valor in vetor

v1 = [45, 89, 32, 12, 33]
print(valor_existe(v1, 45))
print(valor_existe(v1,9))