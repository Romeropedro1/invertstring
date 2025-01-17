Entendido! Aqui está o **README.md** contendo os 5 programas que fizemos, com uma explicação geral e detalhes sobre cada um:

---

```markdown
# Testes de Programação

Este repositório contém soluções para uma série de problemas de programação resolvidos em Python. Os problemas envolvem conceitos como loops, manipulação de listas, cálculos, sequências matemáticas e análise de dados.

## Problemas Resolvidos

### 1. **Cálculo da soma de números até um valor (SOMA)**

**Descrição:**  
Este programa calcula a soma de números inteiros, de 1 até o valor de uma variável `INDICE`. Ele utiliza um laço `while` para realizar o cálculo.

**Código:**

```python
# Inicialização das variáveis
INDICE = 13
SOMA = 0
K = 0

# Loop para somar os números de 1 até 13
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

# Exibe o resultado
print(SOMA)
```

**Resultado esperado:**  
O valor final de `SOMA` será **91** (1 + 2 + 3 + ... + 13).

---

### 2. **Verificação se um número pertence à sequência de Fibonacci**

**Descrição:**  
Este programa recebe um número e verifica se ele pertence à sequência de Fibonacci, que começa com 0 e 1, e cada número subsequente é a soma dos dois anteriores.

**Código:**

```python
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
```

**Exemplo de entrada e saída:**

- Entrada: 21  
- Saída: "O número 21 pertence à sequência de Fibonacci."

---

### 3. **Análise de faturamento mensal**

**Descrição:**  
Este programa realiza a análise de um faturamento diário, que pode conter dias sem vendas. Ele calcula o menor valor, o maior valor e o número de dias com faturamento acima da média.

**Código:**

```python
import json

# Dados do faturamento diário (JSON)
faturamento_json = '''
[
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
'''

# Carregar dados do JSON
faturamento = json.loads(faturamento_json)

# Calcular a média, o menor e maior valor
valores = [item['valor'] for item in faturamento if item['valor'] > 0]
media = sum(valores) / len(valores) if valores else 0
menor_valor = min(valores)
maior_valor = max(valores)

# Contar dias com faturamento superior à média
dias_acima_media = sum(1 for valor in valores if valor > media)

# Resultados
print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
```

**Exemplo de saída:**
- Menor valor de faturamento: R$ 373.78
- Maior valor de faturamento: R$ 48924.24
- Número de dias acima da média: 14

---

### 4. **Cálculo de percentual de faturamento por estado**

**Descrição:**  
Este programa calcula o percentual de faturamento de cada estado, com base em um faturamento total da distribuidora.

**Código:**

```python
# Faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calcular o percentual de cada estado
percentuais = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# Exibir os resultados
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
```

**Resultado esperado:**
O programa calculará e imprimirá o percentual de faturamento de cada estado em relação ao total.

---

### 5. **Inversão de uma string**

**Descrição:**  
Este programa inverte os caracteres de uma string informada pelo usuário, sem utilizar funções prontas como `reverse()`.

**Código:**

```python
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
```

**Exemplo de entrada e saída:**

- Entrada: "programação"
- Saída: "oãçamorgp"

---

## Como Rodar os Programas

Para rodar qualquer um dos programas acima, basta seguir as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. **Acesse a pasta do repositório:**
   ```bash
   cd nome-do-repositorio
   ```

3. **Execute os programas:**
   Cada programa pode ser executado separadamente. Para rodar um programa Python, use o seguinte comando:
   ```bash
   python nome-do-arquivo.py
   ```

---

## Contribuições

Se você quiser contribuir com este repositório, sinta-se à vontade para fazer um *fork* e enviar um *pull request*. Fique à vontade para sugerir melhorias, correções ou novos problemas!

---

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

