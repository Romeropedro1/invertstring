# Função para verificar se um número está na sequência de Fibonacci
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Entrada do usuário
numero = int(input("Digite um número: "))

# Verificar se o número pertence à sequência
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
