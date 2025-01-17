# Dados fornecidos
dados = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]

# Funções de análise
def calcular_total(dados):
    return sum(item['valor'] for item in dados)

def calcular_media(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    return sum(valores) / len(valores) if valores else 0

def identificar_maior_valor(dados):
    return max(dados, key=lambda x: x['valor'])

def identificar_menor_valor(dados):
    return min(dados, key=lambda x: x['valor'])

# Resultados
total = calcular_total(dados)
media = calcular_media(dados)
maior_valor = identificar_maior_valor(dados)
menor_valor = identificar_menor_valor(dados)

# Exibição dos resultados
print(f"Total das vendas no mês: R$ {total:.2f}")
print(f"Média das vendas no mês: R$ {media:.2f}")
print(f"Maior valor de venda: Dia {maior_valor['dia']} - R$ {maior_valor['valor']:.2f}")
print(f"Menor valor de venda: Dia {menor_valor['dia']} - R$ {menor_valor['valor']:.2f}")
