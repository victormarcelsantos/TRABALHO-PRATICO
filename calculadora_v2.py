saida = ''

def adicao(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return 'Não foi possível realizar a divisão por 0'
    return a / b

def calculadora(num1, num2, operacao):
    operacao = operacao.lower()
    if operacao in ['+', 'adição', 'adicao']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtração', 'subtracao']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicação', 'multiplicacao']:
        resultado = multiplicacao (num1, num2)
    elif operacao in ['/', ' divisão', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = 'Operação inválida!'

    return resultado

while saida.lower() != 'n':
    print('\n--- Calculadora ---')

    n1 = float(input ('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    op = input('Digite a operação desejada (+, -, *, / ou nome da operação): ')

    resultado = calculadora(n1, n2, op)

    print('Resultado da operacao:', resultado)

    saida = input ('Deseja continuar? (S/N): ')

print('Programa encerrado!')