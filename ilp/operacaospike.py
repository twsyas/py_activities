## Dicionario das variaveis
# B = numero de kills, C = credito recebido por kill, D = creditos gastos, A = creditos iniciais
## Creditos finais: CF = A+B*C-D

# Entrada composta por uma única linha, contendo quatro numeros interios separados por espaço. Nesse caso, usaremos o "split()" no final.
A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

# Calculando os creditos finais, temos:

CF = A+B*C-D

# Para a saida, precisamos so printar o CF:

print(CF)


## ou, para nao fazer quatro linhas para mudar a tipagem das variaveis, voce pode utilizar a funcao map()

A,B,C,D = map(int,input().split())
CF = A+B*C-D
print(CF)

## Ja otimiza e diminui bastante o seu codigo. Dê uma lida sobre como o map() funciona. Links: para o map : https://www.w3schools.com/PYTHON/ref_func_map.asp, para o split(): https://www.w3schools.com/python/ref_string_split.asp
