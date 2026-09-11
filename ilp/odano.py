# Objetivo do codigo: calcular o dano total causado apos uma sequencia de ataques
# Formula do dano: DA = (F*2)+(N*3)-(P//4), sendo F a força, N o nivel e P o peso da arma
# Como a questao fala que Lae'zel faz X ataques e a formula do DA continua o mesmo entao vamos fazer algo do tipo: X*DA
F, N, P, X =  map(int,input().split())
DA = ((F*2)+(N*3)-(P//4))

print(DA*X)

## A primeira saida do PDF ta dando um valor diferente daqui. Mesmo calculando tudo na calculadora, o valor é diferente. Nao sei se voce ja viu if e else nesta lista.
