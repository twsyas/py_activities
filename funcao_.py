
def maior_numero():
    num1 = int(input("Adicione o primeiro número: "))
    num2 = int(input("Adicione o segundo número: "))
    

    if num1 <0 or num2 <0:
        print("Adicione um número inteiro.")
    elif num1 == num2:
        print("Os dois números são iguais!")
    elif num1 != num2:
        maior = max(num1, num2)
        print(f'O número máximo entre os dois números adicionados é: {maior}')

    return 

    

print(maior_numero())

    


        





