def soma_valores(v):
    soma = 0
    for x in v:
        soma += x
    return soma

v1 = [45, 89, 32, 12, 13]
print(f"A soma dos valores é de {soma_valores(v1)}")