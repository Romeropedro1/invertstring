# Função para inverter a string
def inverter_string(s):
    inversa = ""
    for i in range(len(s)-1, -1, -1):
        inversa += s[i]
    return inversa

# Entrada do usuário
string = input("Digite uma string: ")

# Exibir o resultado
print("String invertida:", inverter_string(string))
