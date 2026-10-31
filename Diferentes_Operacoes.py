n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

def media (a, b):
    return (a + b)/2

def diferenca(a, b):
    return a - b

def produto (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        print("Escreva um numero maior que 0")
    else:
        return a/b 
    
operacoes = {
    
    1: media,
    2: diferenca,
    3: produto,
    4: divisao,

}

print("\nOperadores\n1: Média\n2: Diferença\n3: Produto\n4: Divisão")

escolha = int(input('escolha um número entre 1 e 4: '))

if escolha not in [1, 2, 3, 4]:
    print('escolha um número válido')
else:
    resultado = operacoes.get(escolha)
    print(resultado(n1,n2))