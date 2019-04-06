
# coding: utf-8

# # Bem-Vindo ao Mundo Python!

# ## Variáveis e Tipos
# * Variáveis são **Locais de Memória**;
# * Os nomes de variáveis devem ser **mnemônicos**, ou seja, de **fácil memorização**;
# * Variáveis em Python são *"Case-sensitive"* e devem escritas com letras minúsculas, sem qualquer tipo de acentuação gráfica;
# * Nomes compostos de variáveis devem ser separados por subtraço, por exemplo: nome_variavel_composta;
# * Python é uma linguagem *dinamicamente tipada*, logo, não informamos o tipo de dados durante a declaração de cada variável;
# 
# ### Tipos de Dados Padrão
# Os tipos de dados primitivos do Python podem ser classificados como: numéricos, sequências, conjuntos e mapeamentos.
# 
# *Tipos Numéricos*
# 
# | Nome    | Descrição                    |  Versão               |
# |:--------|:-----------------------------|:----------------------|
# | int     | Números Inteiros             | Todas                 |
# | long    | Números inteiros Longos      | Python 2.x (Somente)  |
# | float   | Números de Ponto Flutuante   | Todas                 |
# | complex | Números Complexos            | Todas                 |
# 
# *Sequências*
# 
# | Nome         | Descrição                                                  |  Versão               |
# |:-------------|:-----------------------------------------------------------|:----------------------|
# | str          | Cadeia de Caracteres (String)                              | Todas                 |
# | bytes        | Sequência de números inteiros no intervalo de 0 a 255      | Python 3.x (Somente)  |
# | byte array   | Semelhante ao tipo bytes, porém, mutáveis                  | Python 3.x (Somente)  |
# | list         | Lista de itens geralmente homogêneos e mutáveis            | Todas                 |
# | tuple        | Sequência de itens heterogêneos e imutáveis                | Todas                 |
# 
# *Conjuntos*
# 
# | Nome       | Descrição                               |  Versão                |
# |:-----------|:----------------------------------------|:-----------------------|
# | set        | coleção não ordenada de objetos únicos  | Python 2.6 ou Superior |
# | frozen set | Semelhante ao tipo set, porém, imutável | Python 2.6 ou Superior |
# 
# *Mapeamentos*
# 
# | Nome       | Descrição                               |  Versão                |
# |:-----------|:----------------------------------------|:-----------------------|
# | dict       | Dicionários ou Array Associativos       | Todas                  |
# 
# 
# #### Objetos Mutáveis X Objetos Imutáveis
# De modo geral, os tipos de dados em Python podem ser diferenciados como mutáveis e imutáveis.
# 
# - **Objetos Mutáveis:** o conteúdo pode ser alterado após sua criação;
# - **Objetos Imutáveis:** o conteúdo **não pode ser alterado** após sua criação;
# 
# | Tipos Mutáveis       | Tipos Imutáveis                         |
# |:---------------------|:----------------------------------------|
# | array                | int, float, complex                     |
# | bytearray            | str                                     |
# | list                 | bytes                                   |
# | set                  | tuple                                   |
# | dict                 | frozenset                               |
# | -                    | bool                                    |

# In[1]:


# CONVERSÃO DE TIPO
# Aprendendo Conversão de Tipo Com Exemplos

# Números Inteiros
valor_int_1 = int(2.7) 
print(valor_int_1) # Saída: 2   

valor_int_2 = int(-3.9)
print(valor_int_2) # Saída: -3   

valor_int_3 = int("2")
print(valor_int_3) # Saída: 2  


# Números de Ponto Flutuante
valor_float_1 = float(7)
print(valor_float_1) # Saída: 7.0

valor_float_2 = float("4.5")
print(valor_float_2) # Saída: 4.5

valor_float_4 = float("2.7E-2")
print(valor_float_4) # Saída: 0.027

valor_float_5 = float(False)
print(valor_float_5) # Saída: 0.0

valor_float_6 = float(True)
print(valor_float_6) # Saída: 1.0


# Cadeia de Caracteres
valor_string_1 = str(4.5)
print(valor_string_1) # Saída: 4.5

valor_string_2 = str([1, 2, 3, 4, 5])
print(valor_string_2) # Saída: "[1, 2, 3, 4, 5]"


# Tipos Lógicos (Booleanos)
valor_bool_1 = bool(0)
print(valor_bool_1) # Saída: False

valor_bool_2 = bool(1)
print(valor_bool_2) # Saída: True

valor_bool_3 = bool([])
print(valor_bool_3) # Saída: False - Lista Vazia

valor_bool_4 = bool([False])
print(valor_bool_4) # Saída: True - Lista Não Vazia

valor_bool_5 = bool({})
print(valor_bool_5) # Saída: False - Dicionário Vazio, o mesmo para Tupla

valor_bool_6 = bool("")
print(valor_bool_6) # Saída: False - String Vazia

valor_bool_7 = bool(" ")
print(valor_bool_7) # Saída: True - String Não Vazia

valor_bool_8 = bool(None)
print(valor_bool_8) # Saída: False

valor_bool_9 = bool(len)
print(valor_bool_9) # Saída: True

# Listas e Conjuntos
conjunto = set([1, 2])
lista = list(conjunto)
print(conjunto) # Saída: {1, 2}
print(lista)    # Saída: [1, 2]

valor_lista_1 = list({0: "Python", 1: "R"}) # dict: Lista de chaves
print(valor_lista_1) # Saída: [0, 1]

tupla = tuple(lista)
print(tupla) # Saída: (1, 2)

valor_lista_2 = list("ABC")
print(valor_lista_2) # Saída: ['A', 'B', 'C']


# In[ ]:


# Conversão IMPLÍCITA de Tipo
# Aprendendo Conversão de Tipo Com Exemplos

numero_inteiro = 7
numero_real = inteiro + 2.1
print(numero_real) # Saída: 9.1

cadeia_caracteres = "Meu int: " + str(numero_inteiro)
print(cadeia_caracteres)

numero_inteiro_2 = 4 + True
print(numero_inteiro_2) # Saída: 5 - O valor booleno é convetido implicitamente para inteiro


# ## Exercício 1
# *Calculando o IMC*
# 
# O Índice de Massa Corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está em seu peso ideal.
# O cálculo do IMC é determinado pela divisão da massa do indivíduo em quilogramas pelo quadrado de sua altura em metros.
# 
# 
# 
# $$IMC=\frac{massa}{(altura * altura)}$$
# 
# 
# 
# Escreva um programa que leia do usuário sua altura e peso e calcule seu IMC.
# 

# In[ ]:


# TODO: Complete o Código Abaixo
altura = float(input('Altura: '))
peso = float(input('  Peso: '))

imc = peso/(pow(altura,2))

print("   IMC: " + str(imc))


# ## Operadores
# 
# *Operadores Numéricos*
# 
# | Operador | Descrição       |
# |:---------|:----------------|
# | +        | Adição          |
# | -        | Subtração       |
# | *        | Multiplicação   |
# | /        | Divisão         |
# | **       | Expoente        |
# | %        | Módulo          |
# | //       | Divisão de Piso |
# 
# 
# *Operadores de Comparação*
# 
# | Operador | Descrição       |
# |:---------|:----------------|
# | ==       | Igual           |
# | !=       | Diferente       |
# | >        | Maior           |
# | <        | Menor           |
# | >=       | Maior Igual     |
# | <=       | Menor Igual     |
# 
# 
# *Operadores Lógicos*
# 
# | Operador | Descrição       |
# |:---------|:----------------|
# | and      | AND lógico      |
# | or       | OR lógico       |
# | not      | NOT lógico      |
# 
# *Caracteres Especiais*
# 
# | Operador | Descrição       |
# |:---------|:----------------|
# | #        | Comentário      |
# | \n       | Nova Linha      |
# 

# ## Exercícios
# 
# 1. O que o código a seguir imprime?
# 
# ```python
# print(“*\n**\n***\n****\n*****”)
# ```
# 
# 2. O que aparece na janela do console, quando cada uma das instruções abaixo são executadas, para: x = 2 e y = 3? Execute cada uma das linhas abaixos e, se necessário, faça os devidos ajustes no código.
#     1. *print(“x = ” + x);*
#     2. *print(“O valor de x + x é ” + (x + x));*
#     3. *print(“x = ”);*
#     4. *print((x + y) + “ = “ + (y + x));*
# 
# 
# 3. Escreva um programa que leia o nome, o sobrenome e o número de matrícula de um estudante. Em seguida, formate e imprima os dados lidos da seguinte forma: [matrícula] nome sobrenome.
# 
# 4. Escreva um programa que solicite do usuário dois números, e imprima o resultado da soma, subtração, multiplicação e divisão.
# 
# 5. Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².
# 
# 6. Escreva um programa que receba como entrada um número de 5 dígitos, separe o número em dígitos individuais e os imprima separados por 3 espaços cada um. Por exemplo, se o usuário digitar 42339, o programa deverá imprimir: 4    2    3    3.   Dica: utilize as operações de divisão e módulo para extrair cada dígito do número.

# # Questão 1
# ## O que o código a seguir imprime?

# In[20]:



print("*\n**\n***\n****\n*****")


# # Questão 2
# ##  O que aparece na janela do console, quando cada uma das instruções abaixo são executadas, para: x = 2 e y = 3? Execute cada uma das linhas abaixos e, se necessário, faça os devidos ajustes no código.
#     1. *print(“x = ” + x);*
#     2. *print(“O valor de x + x é ” + (x + x));*
#     3. *print(“x = ”);*
#     4. *print((x + y) + “ = “ + (y + x));*

# In[1]:


x = 2
y = 3
# Item 1
print("x = " + str(x))
# Item 2
print("O valor de x + x é "+ str(x + x));
# Item 3
print("y =  " + str(y));
# Item 4
print("(x + y) = " + str(y + x));


# # Questão 3
# ## Escreva um programa que leia o nome, o sobrenome e o número de matrícula de um estudante. Em seguida, formate e imprima os dados lidos da seguinte forma: [matrícula] nome sobrenome.

# In[3]:


matricula = input('Matrícula: ')
nome = str(input('Nome: '))
sobrenome = str(input('Sobrenome: '))
print(" [ " + str(matricula) + " ] " + nome + " " + sobrenome)


# # Questão 4
# ## Escreva um programa que solicite do usuário dois números, e imprima o resultado da soma, subtração, multiplicação e divisão.

# In[4]:


numero_1 = float(input('Número 1: '))
numero_2 = float(input('Número 2: '))

soma = numero_1 + numero_2

subtracao = numero_1 - numero_2

multiplicacao = numero_1 * numero_2

divisao = numero_1 / numero_2

print("Soma: " + str(soma))
print("Subtração: " + str(subtracao))
print("Multiplicação: " + str(multiplicacao))
print("Divisão: " + str(divisao))


# # Questão 5
# ## Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².

# In[7]:


import math
raio = float(input('Raio: '))

diametro = 2 * raio
circunferencia = 2 * math.pi
area = math.pi * pow(raio,2)

print("Diâmetro: " + str(diametro))
print("Cincunferência: " + str(circunferencia))
print("Área: " + str(area))


# # Questão 6
# ## Escreva um programa que receba como entrada um número de 5 dígitos, separe o número em dígitos individuais e os imprima separados por 3 espaços cada um. Por exemplo, se o usuário digitar 42339, o programa deverá imprimir: 4    2    3    3.   Dica: utilize as operações de divisão e módulo para extrair cada dígito do número.

# In[18]:


numero = int(input('Número: '))

digito_1 = int(numero//10000)%10
digito_2 = int(numero//1000)%10
digito_3 = int(numero//100)%10
digito_4 = int(numero//10)%10
digito_5 = numero%10

print("Dígito 1: " + str(digito_1))
print("Dígito 2: " + str(digito_2))
print("Dígito 3: " + str(digito_3))
print("Dígito 4: " + str(digito_4))
print("Dígito 5: " + str(digito_5))

print(str(digito_1) + "   " +  str(digito_2) + "   " +  str(digito_3) + "   " +  str(digito_4) + "   " + str(digito_5) )


# In[ ]:


# TODO: Escreva seu código abaixo

# resultado = ?

print(resultado)


# ## Estruturas de Controle 
# 
# 
# ### Estruturas de Seleção
# 
# As estruturas de seleção *if* e *if/else* são usadas para controle da execução sequêncial de um programa. Na prática, se uma determinada condição lógica for avaliada como verdadeira, o interpretador Python executa todos os comandos dentro do bloco da estrutura de seleção. Em Python, para a estruturas de seleção única usamos a palavra-chave *if* e para estruturas de seleção múltiplas usamos o nome *elsif*. 
# 
# ```python
#  if condicao1:
#     # Executa quando a condição1 for verdadeira
#  elsif condicao2:
#     # Executa quando a condição2 for verdadeira
#  else:
#     # Executa quando todas condições não forem satisfeitas
# ```
# 
# ### Estruturas de Repetição
# 
# O Python possui duas estruturas de repetição, são elas: *for* e *while*. A estrutura de repetição *for*, em sua sintaxe, difere um pouco, por exemplo, das linguagens de programação baseadas em C, onde definimos uma condição de parada (i < n) e um passo de iteração (i++). O comando *for* é usado para percorrer os itens de qualquer sequência (p. ex.: lista, string ou tupla) para que eles apareçam em série ou simplesmente como um laço de repetição (*loop*). 

# In[ ]:


cores  = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"]

for cor in cores:
    print("Eu ♥ " + cor)


# Se você possui alguma experiência anterior com programação, deve estar se perguntando neste exato momento, como podemos percorrer os itens de uma sequência usando índices? Para tal, podemos utilizar a função range() em conjunto com a função len(). A função *range(start, stop, step)* do Python, retorna uma sequência de números, começando em 0 (zero) por padrão, e incrementando de um em um, até o fim de um número especificado como parâmetro. A função len(), por sua vez, retorna o número de itens de uma determina sequência. Acompanhe abaixo, alguns exemplos de como essas funções podem ser usadas em conjunto com a instrução *for* para indexar itens de uma lista.

# In[21]:


# EXEMPLOS - Função range()
lista1 = range(5)
lista2 = range(10, 20, 2)
lista3 = range(1, 5)
lista4 = range(5, -1, -1)

print("EXEMPLOS: Função range()\n")

for item in lista1:
    print(item) # Para range(5) Saída: [0, 1, 2, 3, 4]

print("\n") 
    
for item in lista2:
    print(item) # Para range(10, 20, 2) Saída: [10, 12, 14, 16, 18]

print("\n")     
    
for item in lista3:
    print(item) # Para range(1, 5) Saída: [1, 2, 3, 4]

print("\n")     
    
for item in lista4:
    print(item) # Para range(1, 5) Saída: [1, 2, 3, 4]
    
    
print("\n")     
    
    
# EXEMPLOS - for, range() e len
print("EXEMPLOS: for, len() e range()\n")


# Imprimindo lista de cores
cores  = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Anil", "Violeta"]
n = len(cores) # a função len() retorna o número de elementos

for i in range(n):
    print(cores[i])

print("\n")

for i in range((n - 1), -1, -1):
    print(cores[i])


# for aninhado para impressão de um padrão numérico
for i in range(10):
    for j in range(i):
        print(i, end=" ")    # Imprime o número
    print("\n")              # Adiciona quebra de linha ao final de cada linha




# Assim como o for, a estrutura de repetição while é usada para repetir um trecho de código várias vezes, porém, no while a repetição continua enquanto uma condição lógica definida seja verdadeira (True), veja alguns exemplos abaixo: 
# 
# ```python
# while condicao: # enquanto condição for verdadeira
#     # Executa algum(ns) comando(s)
#     # Atualiza variável de controle
# ```

# In[ ]:


contador = 0                 # Define uma variável de controle que será avaliada na condição

while contador < 10:         # enquanto a condição (contador < 10) for verdadeira
    print(contador)          # Executa algum comando: print(contador)
    contador = contador + 1  # Atualiza a variável de controle
    
print("\n")


# EXEMPLO: Algoritmo Fatorial Iterativo
n = 3
i = 1
resultado = 1

while i <= n:
    resultado = resultado * i
    i = i + 1
    
print("Fatorial de %d é %d" % (n, resultado))
    


# ### Técnicas de Looping
# 
# 1. Ao percorrer dicionários, a chave e o valor, podem ser recuperados ao mesmo tempo através do método *items()*;
# 
# ```python
# websites = {'site': "Python Software Foundation", 'url': "https://www.python.org/"}
# 
# for key, value in websites.items():
#     print(key, value)
#     
# # Saída
# # site Python Software Foundation
# # url https://www.python.org/
# ```
# 
# 2. Ao percorrer sequências, índice e o item, podem ser recuperados ao mesmo tempo através do método *enumerate()*;
# 
# ```python
# rgb = ["Red", "Green", "Blue"]
# 
# for i, item in enumerate(rgb):
#     print(i, item)
#     
# # Saída
# # 0 Red
# # 1 Green
# # 2 Blue
# ```
# 
# 3. Para percorrer duas ou mais sequências ao mesmo tempo, as entradas podem ser emparelhadas através da função *zip()*;
# 
# 
# ```python
# condinomes_android = ["Petit Four", "Eclair",  "Honeycomb", "Ice Cream Sandwich", "Lollipop", "Marshmallow", "Nougat", "Oreo", "Pie"]
# versoes_android = ["1.1", "2.0 – 2.1", "3.0 – 3.2.6", "4.0 – 4.0.4", "5.0 – 5.1.1", "6.0 – 6.0.1", "7.0 – 7.1.2", "8.0 – 8.1", "9.0"]
# 
# for codinome, versao in zip(condinomes_android, versoes_android):
#     print(codinome, versao)
#     
# # Saída
# # Petit Four 1.1
# # Eclair 2.0 – 2.1
# # Honeycomb 3.0 – 3.2.6
# # Ice Cream Sandwich 4.0 – 4.0.4
# # Lollipop 5.0 – 5.1.1
# # Marshmallow 6.0 – 6.0.1
# # Nougat 7.0 – 7.1.2
# # Oreo 8.0 – 8.1
# # Pie 9.0
# ```
# 
# 4. Para iterar em uma sequência ordenada sem alterar a ordem dos elementos utilize o metodo *sorted()* que irá retornar uma nova lista ordenada sem alterar a original
# 
# ```python
# estados_sudeste_brasileiro = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Espírito Santo"]
# 
# for estado in sorted(set(estados_sudeste_brasileiro)):
#     print(estado)
#     
# # Saída
# # Espírito Santo
# # Minas Gerais
# # Rio de Janeiro
# # São Paulo    
#     
# ```

# ## Exercícios
# 
# 1. Escreva um programa que leia dois números inteiros que determine e verifique se o primeiro é um múltiplo do segundo. Por exemplo: se o usuário digitar 15 e 3, o primeiro número será múltiplo do segundo; se o usuário digitar 2 e 4, o primeiro número não será múltiplo do segundo. Dica: use o operador módulo para obter o resto da divisão.
# 
# 2. Escreva um programa que calcule o quadrado e o cubo dos números de 0 a 10, e imprima os valores em forma de tabela. Número | Quadrado | Cubo
# 
# 3. Escreva um programa que receba dois números inteiros como entrada e verifica qual deles é o maior.
# 
# 4. Escreva um programa que leia apenas uma letra do alfabeto como entrada e classifique-a como vogal ou consoante. Seu programa deverá aceitar como entrada apenas um caractere, ou seja, se o usuário digitar dois ou mais caracteres, o sistema deverá informar ao usuário a entrada rejeitada.
# 

# ## Funções
# 
# Métodos são blocos de códigos reutilizáveis que realizam tarefas específicas dentro de um programa. Em Python, definimos funções usando a palavra-chave *def*, seguida pelo nome da função, a lista formal de parâmetros entre parêntesis, e, finalizando a assinatura do método com dois pontos (:). É importante lembrar que todas as instruções após a assinatura do método e que formam o corpo da função, devem ser identadas para funcionamento correto do código.
# 
# ```python
# def soma(a, b):
#     """Retorna a soma de dois números inteiros"""
#     return a + b;
# 
# 
# # Exemplo de uso da função
# resultado_soma = soma(12, 15) 
# print(resultado_soma) # Saída: 27
# 
# ```
# 
# Você deve ter notado o comentário logo após a assinatura do método; este tipo de comentário é o que chamamos de *docstring*, e serve para documentarmos as funções para posteriormente, gerarmos automaticamente com auxílio de ferramentas, uma documentação online ou impressa do seu programa. Por isso, comente sempre seu código e escreva-o de maneira mais clara possível para que outras pessoas consigam ler e compreender facilmente o que seu código faz.
# 
# ### Declaração de Argumentos
# 
# Existem 3 formas diferentes, que podem ser combinadas entre si, para definirmos funções com número variável de argumentos, são elas:
# 
# **1. Valores Padrão de Argumento**: declaramos um valor padrão para um ou mais argumentos no seguinte formato: *"arg = value"*; de tal forma que damos a opção de não especificar valores para tais argumentos e usarmos os valores padrão definidos.
# 
# ```python
# def exibir_mensagem(mensagem, cortar_apos = 4):
#     print(message[:cortar_apos]
# 
# # Exemplo de uso da função
# exibir_mensagem("mensagem")     # Saída: mens
# exibir_mensagem("mensagem", 6)  # Saída: mensag
# ```
# 
# **2. Argumentos por Palavras-Chave**: semelhante a técnica anterior, argumentos por palavra-chave nós declaramos os argumentos no formato *"arg = value"*, lembrando que em uma chamada de função as variáveis passadas como parâmetro devem seguir a mesma ordem dos argumentos na assinatura do método.
# 
# ```python
# def desenha_retangulo(x, y, width = 800, height = 600):
#     # Instruções
#     
# # Exemplo de uso da função
# desenha_retangulo(0, 0)                               # Argumento por posição usando valores padrão do restante 
# desenha_retangulo(0, 0, width = 1280)                 # Argumento com uma palavra-chave
# desenha_retangulo(0, 0, width = 1280, height = 1024)  # Argumento com duas palavras-chave
# desenha_retangulo()                                   # Erro: required argument missing
# desenha_retangulo(color = "#CCCCCC")                  # Erro: argumento por palavra-chave desconhecido
# desenha_retangulo(0, 0, x = 200, y = 300)             # Erro: valores duplicados par ao mesmo argumento
# 
# ```
# 
# **3. Listas de Argumentos Arbitrários**: o Python permite você criar listas de argumentos com tamanho variável, de forma que toda vez que você chamar a função você possa especificar qualquer quantidade de argumentos que serão empacotados em uma variável do tipo tupla.
# 
# ```python
# # O último argumento é marcado com uma asterisco 
# # para indicar que após os dois primeiros parâmetros
# # qualquer dado enviado para a função será empacotado em uma tupla.
# def nome_funcao(primeiro_arg, segundo_arg, *restante):
#     # Instruções
#     
# ```
# 
# ### Passagem por Valor ou Por Referência?
# 
# Em Python, objetos passados como argumentos para as funções são passados por *referência*, ou seja, não é feita uma cópia deles para o corpo da função. Desta forma, quando passamos uma lista enorme como argumento, não haverá a cópia  de todos os seus itens para um novo local em memória. Não se esqueça que até mesmo números inteiros são objetos para o Python. 
# 
# Ao passar objetos mutáveis (p. ex: listas e dicionários) como parâmetro, eles podem ser alterados pela função que os chamou e as alterações são visíveis para a função chamadora. Já os objetos imutáveis (p. ex: inteiros e strings), não podem ser alterados pela função chamada, logo, a função chamadora pode ter certeza de que a função chamada não irá alterar os valores das variáveis.
# 

# ## Exercícios
# 
# 1. Uma empresa quer transmitir dados pelo telefone, mas está preocupada com a interceptação telefônica. Todos os seus dados são transmitidos  como inteiros de quatro dígitos. Ela pediu para que você escreva um programa que criptografe seus dados, para que eles possam ser transmitidos com mais segurança. Seu aplicativo deve ler um inteiro de quatro dígitos fornecidos pelo usuário e criptografá-lo da seguinte forma: substitua cada dígitos por (a soma desse dígitos mais 7) módulo 10. Em seguida, troque o primeiro dígito pelo terceiro e troque o segundo dígito pelo quarto e imprima o inteiro criptografado.
# 
# 2. Implemente a função par que retorna verdadeiro se um número inteiro passado como parâmetro for par ou falso caso ele seja ímpar. Teste seu programa chamando a função para verificar os números de 0 à 10.
# 
# 3. Escreva um programa que leia 3 números inteiros referente ao comprimento dos lados de um triângulo e classifique como: triângulo equilátero, isósceles ou escaleno.
# 
# 4. Escreva um programa que aceita um número como entrada e insere hífens (-) entre dois números pares. Por exemplo, se receber o número 02368859 como entrada, a saída do programa deverá ser: 0-236-8-859.
# 
# 5. Escreva um programa que encontre o item mais frequente de um vetor. Exemplo: [2, 7, 7, 7, ‘#’, ‘#’, ‘#’, ‘@’, 3, ‘#’, 6]  // Saída: # aparece 4 vezes
# 
# 6. Um número de Armstrong de 3 dígitos é um inteiro pelo qual a soma dos cubos dos seus dígitos é igual ao seu número. Por exemplo: o número inteiro 371 é um número de Armstrong, porque 3³ + 7³ + 1³ = 371. Escreva um programa que verifique se um número de 3 dígitos fornecido como entrada é um número de Armstrong.
# 
# 7. Escreva uma função ue receba uma string e conte o número de vogais dentro dela, por exemplo: entrada: ‘Ciência de Dados’, saída: 7 vogais
# 
# 8. Implemente em Python o algoritmo de Busca Binária
# 
# 9. Escreva uma função que receba algum valor como parâmetro e retorne seu tipo
# 
# 10. Escreva uma função que receba um lista numérica como parâmetro e retorne os segundos maiores e menores números da sequência, por exemplo: entrada [1, 2, 3, 4, 5, 6, 7, 8, 9], saída [2, 8].
# 
# 12.  Escreva uma função que receba um número inteiro como entrada (px.: 32243) e retorne o número invertido (px.: 34223).

# ## Exercicio 1
#  Uma empresa quer transmitir dados pelo telefone, mas está preocupada com a interceptação telefônica. Todos os seus dados são transmitidos como inteiros de quatro dígitos. Ela pediu para que você escreva um programa que criptografe seus dados, para que eles possam ser transmitidos com mais segurança. Seu aplicativo deve ler um inteiro de quatro dígitos fornecidos pelo usuário e criptografá-lo da seguinte forma: substitua cada dígitos por (a soma desse dígitos mais 7) módulo 10. Em seguida, troque o primeiro dígito pelo terceiro e troque o segundo dígito pelo quarto e imprima o inteiro criptografado. 

# In[9]:


numero = int(input('Número: '))

digito_1 = (int(numero//10000 + 7)%10) 
digito_2 = (int(numero//1000 + 7)%10) 
digito_3 = (int(numero//100 + 7)%10) 
digito_4 = (int(numero//10 + 7)%10)      

numero_criptografado = str(digito_3) + '' + str(digito_4) + '' + str(digito_1) + '' + str(digito_2)

print("Número Criptografado: " + str(numero_criptografado))


# ## Exercicio 2
# Implemente a função par que retorna verdadeiro se um número inteiro passado como parâmetro for par ou falso caso ele seja ímpar. Teste seu programa chamando a função para verificar os números de 0 à 10.

# In[8]:


def verificaPar(numero):
    if int(numero) % 2 == 0:
        return True;
    else:
        return False;

print(verificaPar(0))
print(verificaPar(1))
print(verificaPar(2))
print(verificaPar(3))
print(verificaPar(4))
print(verificaPar(5))
print(verificaPar(6))
print(verificaPar(7))
print(verificaPar(8))
print(verificaPar(9))
print(verificaPar(10))


# ## Exercicio 3
# Escreva um programa que leia 3 números inteiros referente ao comprimento dos lados de um triângulo e classifique como: triângulo equilátero, isósceles ou escaleno.

# In[17]:


def verificaTriangulo(ladoA, ladoB, ladoC):
    if not (ladoA+ladoB)>ladoC and (ladoA+ladoC)>ladoB and (ladoB+ladoC)>ladoA:
       print("Os lados fornecidos não formam um triângulo.")
    elif ladoA==ladoB and ladoA==ladoC:
       print("O triângulo é equilátero.")
    elif ladoA!=ladoB and ladoA!=ladoC and ladoB!=ladoC:
       print("O triângulo é escaleno.")
    else:
      print("O triângulo é isósceles.")
 
ladoA = int(input('Lado A: '))
ladoB = int(input('Lado B: '))
ladoC = int(input('Lado C: '))

verificaTriangulo(ladoA, ladoB, ladoC)


# ## Exercicio 4
# Escreva um programa que aceita um número como entrada e insere hífens (-) entre dois números pares. Por exemplo, se receber o número 02368859 como entrada, a saída do programa deverá ser: 0-236-8-859.

# In[32]:


numero = str(input('Número: '))
retorno=''
for n in range(len(str(numero))):
     if int(numero[n]) % 2 == 0 and int(numero[n + 1]) % 2 == 0:
        retorno = retorno +  str(numero[n]) + '-';
     else:
        retorno = retorno +  str(numero[n])
        
print(retorno)


# ## Exercicio 5
# Escreva um programa que encontre o item mais frequente de um vetor. Exemplo: [2, 7, 7, 7, ‘#’, ‘#’, ‘#’, ‘@’, 3, ‘#’, 6] // Saída: # aparece 4 vezes

# In[133]:


def verificaItemFrequente(lista):
    contador = 0
    item = ''
    for n in range(len(lista)):
        quantidade = 0
        for j in range(len(lista)):
            if(lista[n] == lista[j]):
                quantidade = quantidade + 1;
        
        if(quantidade > contador):
            item = str(lista[n])
            contador = quantidade;
            
    print("O item " + item + " aparece " + str(contador) + " vezes.")

verificaItemFrequente([2, 7, 7, 7, '#','#', '#', '@', 3, '#', 6])


# ## Exercicio 6
# Um número de Armstrong de 3 dígitos é um inteiro pelo qual a soma dos cubos dos seus dígitos é igual ao seu número. Por exemplo: o número inteiro 371 é um número de Armstrong, porque 3³ + 7³ + 1³ = 371. Escreva um programa que verifique se um número de 3 dígitos fornecido como entrada é um número de Armstrong.

# In[41]:


numero = str(input('Número: '))
valor = 0
for n in range(len(str(numero))):

    valor = valor + pow(int(numero[n]),3)

if(valor == int(numero)):
    print ("É um número de Armstrong")
else:
    print ("Não é um número de Armstrong")


# ## Exercicio 7
# Escreva uma função que receba uma string e conte o número de vogais dentro dela, por exemplo: entrada: ‘Ciência de Dados’, saída: 7 vogais

# In[114]:


def verificaVogal(letra):
    vogais = ['a', 'e', 'i', 'o', 'u','á', 'é', 'í', 'ó', 'ú','â', 'ê', 'ô','ã','õ']
    return letra.lower() in vogais;

def ContaVogais(texto):
    contador = 0
    for n in range(len(str(texto))):
        if verificaVogal(str(texto[n])):
            contador = contador + 1;
    return contador;

print(ContaVogais("Bruna"))
print(ContaVogais("Paralelepipedo"))
print(ContaVogais("Ciência de Dados"))
    


# ## Exercicio 8
# Implemente em Python o algoritmo de Busca Binária

# In[145]:


def buscaBinaria(lista, pInicial, pFinal, valor): 
    while pInicial <= pFinal: 
        media = int(pInicial + (pFinal - pInicial)/2); 
        if lista[media] == valor: 
            return media 
        elif lista[media] < valor: 
            pInicial = media + 1
        else: 
            pFinal = media - 1
    return -1
    
lista = [2,3,4,10,40]
valor = 4
resultado = buscaBinaria(lista, 0, len(lista)-1, valor) 
  
if resultado != -1: 
    print("Item encontrado na posição % d" % resultado)
else: 
    print ("Item não encontrado na lista")


# ## Exercicio 9
# Escreva uma função que receba algum valor como parâmetro e retorne seu tipo

# In[44]:


def verificaTipo(valor):
    return type(valor)

print(verificaTipo("String"))
print(verificaTipo(True))
print(verificaTipo(120))


# ## Exercicio 10
# Escreva uma função que receba um lista numérica como parâmetro e retorne os segundos maiores e menores números da sequência, por exemplo: entrada [1, 2, 3, 4, 5, 6, 7, 8, 9], saída [2, 8].

# In[135]:


def retornaSegundoMaiorMenor(lista):
    maior = max(int(item) for item in lista)
    menor = min(int(item) for item in lista)
    lista.remove(maior)
    lista.remove(menor)
    maior = max(int(item) for item in lista)
    menor = min(int(item) for item in lista)
    print("Maior: " + str(maior))
    print("Menor: " + str(menor))
    
retornaSegundoMaiorMenor([1, 2, 3, 4, 5, 6, 7, 8, 9])


# ## Exercicio 11
# Escreva uma função que receba um número inteiro como entrada (px.: 32243) e retorne o número invertido (px.: 34223).

# In[93]:


def inverteNumero(numero):
    tamanho = len(str(numero)) - 1
    num = ''
    while tamanho >= 0:
        num = str(num) + numero[tamanho]
        tamanho = tamanho - 1;
    return num;  
   
print(inverteNumero("32243"))

