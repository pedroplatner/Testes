# Primeiro teste

# Devemos entender primeiramente que terá um loop quando o "K" for menor que 13

INDICE = 13 #definimos uma var "INDICE" com o valor de 13 que será o valor limite do loop
SOMA = 0    #definimos uma var "SOMA" com o valor de 0 que também usaremos para acumular as somas
K = 0       #definimos uma var "K" com o valor de 0 e sera incrementada a cada iteração do loop

while K < INDICE: #usamos o while que ira continuar enquanto a var "K" for menor que 13
    K = K + 1 #toda vez que o loop for executado a var "K" aumenta em 1, e tera seu limite quando chegar a 13
    SOMA = SOMA + K #aqui teremos a var "K" sendo somada ao valor atual da soma

print(SOMA) #No fim teremos o resultado 91, que é a soma dos números inteiros de 1 a 13

### O código basicamente calcula a soma dos dos numeros utilizando um loop que vai acumulando os valores em soma ###

########################################################################################

#Segundo teste

def is_fibonacci(n): #aqui temos uma função na qual recebe um numero como entrada e retorna verdeadeiro se o numero pertencer a sequência de fibonacci e falso caso nao seja da sequência
    fib_1, fib_2 = 0, 1 #Aqui começamos com duas var, inciando com os valor 0,1
    while fib_1 <= n: #Ja aqui temos um loop que ira continuar enquanto a var fib_1 for menor ou igual a "n"
        if fib_1 == n: #Aqui sera verificado se a var "fib_" é igual a n, caso seja siginifica que ele pertence a sequencia e a funçao retorna verdadeiro
            return True
        fib_1, fib_2 = fib_2, fib_1 + fib_2 #Aqui sera atualizado os valores de "fib_1 e fib_2" para os proximos numeros da sequencia
    return False #Se o loop terminar sem encontrar um numero igual a 'n' significa que nao ira pertencer a sequencia e a função retorna falso

num = int(input("Informe um número: ")) #Aqui solicitamos ao usuario que informe um numero e ele sera armazenado em 'num'

if is_fibonacci(num): #Aqui chamamos a funcão is_fibonacci com o valor 'num' como argumento e verifica se o resultado é verdadeiro
    print(f"{num} pertence à sequência de Fibonacci.") #Se o valor for verdadeiro, sera informado que pertence a sequencia
else:
    print(f"{num} não pertence à sequência de Fibonacci.") #Se o valor for falso, sera informado que nao pertence a sequencia


### O código verifica se o numero da var 'num' pertence à sequência de Fibonacci usando uma função que verifica se o numero inserido pelo usuario esta dentro da sequencia ###

########################################################################################

#Terceiro teste

import json #REALIZAMOS A IMPORTAÇÃO DO JSON

dados = '''
[
    {"dia": 1, "valor": 221.34},
    {"dia": 2, "valor": 190.47},
    {"dia": 3, "valor": 0.00},
    {"dia": 4, "valor": 320.11},
    {"dia": 5, "valor": 0.00},
    {"dia": 6, "valor": 400.24}
]
'''

faturamento = json.loads(dados) #Aqui realizaremos o carregamento dos dados

valores = [item["valor"] for item in faturamento if item["valor"] > 0] #Aqui realizamos os dias com faturamento

menor_valor = min(valores) #CALCULA O MENOR VALOR
maior_valor = max(valores) #CALCULA O MAIOR VALOR
media_mensal = sum(valores) / len(valores) #CALCULA A MÉDIA 

dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal) #Contar dias com faturamento acima da média

print(f"Menor valor: R${menor_valor}") #MOSTRA O MENOR VALOR
print(f"Maior valor: R${maior_valor}") #MOSTRA O MAIOR VALOR
print(f"Dias com faturamento acima da média: {dias_acima_da_media}") #MOSTRA O FATURAMENTO ACIMA DA MÉDIA 

### O código realiza o calculo do menor, maior e media dos valores dado da fonte de dados 'dados' usando o import json, usamos algumas funcoes do python para calcular elas e nos retornando as informaçoes do menor, maior e media dos valores dos 6 dias ###

########################################################################################

#Quarto teste

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_estados.values())#USAMOS A FUNÇÃO 'SUM' PARA CALCULAR O FATURAMENTO TOTAL

for estado, valor in faturamento_estados.items(): #CALCULAMOS O PERCENTUAL DE CADA ESTADO
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")

### O código nos mostra as informações de cada estado da lista, e utiliza a soma de todos eles, e depois fazemos a var 'percentual' dividir o valor pelo faturamento e multiplicar por 100 nos trazendo a porcentagem de cada estado ###

########################################################################################

#Quinto teste

def inverter_string(s):
    invertida = ''

    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string_original = input("Informe uma string: ")
string_invertida = inverter_string(string_original)
print(f"String invertida: {string_invertida}")

### Nesse codigo invertemos uma string sem usar o reverse, utilizamos um loop que percorre a string de trás para frente e nos tras o resultado que sera informado pelo input preenchido pelo usuario