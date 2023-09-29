lista = []

def Media():
    quant = int(input("Quantos números você quer adicionar na lista? "))
    for q in range(quant):
        num = int(input("Adicione um número: "))
        lista.append(num)
    media = sum(lista)/quant

    return media

print(Media())


