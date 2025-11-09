#!/usr/bin/env python
# coding: utf-8

# # Bibliotecas do Python e introdução à manipulação de dados
# 
# A linguagem principal do Python é, por design, relativamente minimalista. Como outras linguagens de programação, o Python possui um ecossistema de módulos (bibliotecas de código) que complementam a linguagem base. Algumas dessas bibliotecas são “padrão”, ou seja, já vêm incluídas na sua distribuição do Python. Muitas outras bibliotecas de código aberto podem ser obtidas por meio de organizações que apoiam seu desenvolvimento.
# 
# Pense em uma biblioteca como uma coleção de funções e tipos de dados que você pode acessar para realizar certas tarefas de programação sem precisar implementar tudo do zero.
# 
# Este curso fará uso extensivo das seguintes bibliotecas:
# 
# * **[Numpy](http://numpy.org)** – biblioteca para trabalhar com arrays de dados.
# * **[Pandas](http://pandas.pydata.org)** – oferece estruturas de dados e ferramentas de análise de alto desempenho e fáceis de usar.
# * **[Scipy](http://scipy.org)** – biblioteca de técnicas para computação numérica e científica.
# * **[Matplotlib](http://matplotlib.org)** – biblioteca para criação de gráficos.
# * **[Seaborn](http://seaborn.pydata.org)** – interface de mais alto nível para o Matplotlib, que simplifica muitas tarefas de plotagem.
# * **[Statsmodels](http://www.statsmodels.org)** – biblioteca que implementa diversas técnicas estatísticas.
# 
# Este notebook apresenta as bibliotecas Pandas e Numpy, usadas para manipular conjuntos de dados. Na próxima semana, daremos uma visão geral das bibliotecas Matplotlib e Seaborn, utilizadas para produzir gráficos. O pacote Statsmodels será usado nos segundo e terceiro cursos da série, que introduzem análise estatística formal e modelagem.
# 
# # Documentação
# 
# Nenhum cientista de dados ou engenheiro de software memoriza todas as funcionalidades de todas as ferramentas que utiliza. Cientistas de dados eficazes aproveitam recursos (principalmente online) para resolver os desafios que enfrentam ao desenvolver código e analisar dados. A documentação é o recurso oficial e autoritativo para qualquer linguagem de programação ou biblioteca. Aqui estão os links para a documentação oficial da [linguagem Python](https://docs.python.org/3/) e da [Biblioteca Padrão do Python](https://docs.python.org/3/library/index.html#library-index).

# ### Importando bibliotecas
# 
# Ao usar Python, geralmente você começará seus scripts importando as bibliotecas que irá utilizar.
# 
# As instruções a seguir importam as bibliotecas Numpy e Pandas, atribuindo a elas nomes abreviados:

# In[2]:


import numpy as np
import pandas as pd


# ### Utilizando funções de bibliotecas
# 
# Após importar uma biblioteca, suas funções podem ser chamadas no seu código precedendo o nome da função com o nome da biblioteca. Por exemplo, para usar a função `dot` da biblioteca `numpy`, você escreveria `numpy.dot`. Para evitar ter que digitar repetidamente o nome da biblioteca nos scripts, é convencional definir uma abreviação de duas ou três letras para cada biblioteca. Por exemplo, `numpy` geralmente é abreviado como `np`. Isso permite usar `np.dot` em vez de `numpy.dot`. Da mesma forma, a biblioteca Pandas é tipicamente abreviada como `pd`.

# A próxima célula mostra como chamar funções de uma biblioteca importada:

# In[3]:


a = np.array([0,1,2,3,4,5,6,7,8,9,10]) 
np.mean(a)


# Como você pode ver, primeiro usamos a função `array` da biblioteca numpy para criar um array literal unidimensional e, em seguida, usamos a função `mean` da mesma biblioteca para calcular o valor médio (isso é chamado de array "literal" porque os dados são inseridos diretamente no notebook).

# ## NumPy
# 
# NumPy é um pacote fundamental para computação científica com Python. Ele inclui tipos de dados para vetores, matrizes e arrays de ordem superior (tensores), além de várias funções matemáticas amplamente utilizadas, como logaritmos.
# 
# #### Arrays do Numpy (o ndarray)
# 
# Estamos principalmente interessados no objeto [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html), que é um array n-dimensional de valores, e nos métodos que nos permitem manipular esses arrays. Lembre-se de que uma lista do Python pode conter valores de diferentes tipos. Por exemplo, `[1, "porco", [3.2, 4.5]]` é uma lista com três elementos — um inteiro, uma string e outra lista que, por sua vez, contém dois valores de ponto flutuante. Listas com tipos heterogêneos são convenientes, mas não têm bom desempenho em computações numéricas em grande escala.
# 
# O `ndarray` do Numpy é um array homogêneo que pode ter qualquer número de eixos. Por ser homogêneo, todos os valores em um mesmo `ndarray` devem ter o mesmo tipo de dado (por exemplo, todos inteiros ou todos números de ponto flutuante).
# 
# Um array do Numpy é uma tabela de valores que pode ter qualquer número de "eixos". Um array unidimensional (1D) possui um único eixo e é análogo a uma lista do Python ou a um vetor matemático. Um array bidimensional (2D) tem dois eixos e pode ser visto como uma tabela ou matriz. Arrays de ordem superior (tensores) podem ser úteis em casos específicos, mas não são tão comuns. Como mencionado acima, todos os valores em um array Numpy têm o mesmo tipo de dado.
# 
# Arrays Numpy são indexados por uma sequência de posições inteiras com base zero — ou seja, `x[0]` é o primeiro elemento de um array 1D `x`. O número de eixos (dimensões) é chamado de “rank” do array; o formato (`shape`) de um array é uma tupla de inteiros que define o tamanho do array em cada dimensão.
# 
# Abaixo estão algumas expressões de linha única que ilustram o uso básico do Numpy.

# In[4]:


### Cria um array numpy de rank 1 com 1 eixo de comprimento 3.
a = np.array([1, 2, 3])

### Imprime o tipo do objeto
print("type(a) =", type(a))

### Imprime o formato (shape)
print("\na.shape =", a.shape)

### Imprime alguns valores de a
print("\nValores em a: ", a[0], a[1], a[2])

### Cria um array numpy 2x2
b = np.array([[1, 2], [3, 4]])

### Imprime o formato (shape)
print("\nb.shape =", b.shape)

### Imprime alguns valores de b
print("\nValores em b: ", b[0, 0], b[0, 1], b[1, 1])

### Cria um array numpy 3x2
c = np.array([[1, 2], [3, 4], [5, 6]])

### Imprime o formato (shape)
print("\nc.shape =", c.shape)

### Imprime alguns valores de c
print("\nValores em c: ", c[0, 1], c[1, 0], c[2, 0], c[2, 1])


# In[5]:


### Array 2x3 contendo zeros
d = np.zeros((2, 3))
print("d =\n", d)

### Array 4x2 contendo uns (1s)
e = np.ones((4, 2))
print("\ne =\n", e)

### Array constante 2x2 com valor 9
f = np.full((2, 2), 9)
print("\nf =\n", f)

### Array aleatório 3x3
g = np.random.random((3, 3))
print("\ng =\n", g)

### Array 2x2 com valores não inicializados
h = np.empty((2, 2))
print("\nh =\n", h)


# #### Indexação de Arrays e Aliasing
# 
# 
# É importante observar que arrays em Python podem compartilhar memória, caso em que a alteração dos valores em um array pode modificar os valores em outro array.

# In[6]:


### Cria um array 3x4
h = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("h=\n", h)

### Fatia o array para criar um sub-array 2x2
i = h[:2, 1:3]

print("\ni=\n", i)

print("\nh[0, 1] =", h[0, 1])

### Modifica a fatia
i[0, 0] = 1738

### Mostra como modificar a fatia também altera o objeto base
print("\nh[0, 1] =", h[0, 1])


# Se você quiser garantir que dois arrays não compartilham memória, use o método:

# In[7]:


h = np.zeros((3, 3))
i = h[0:2, 0:2].copy()
h[0, 0] = 99
print("h =\n", h)
print("\ni =\n", i)


# #### Tipos de Dados
# 
# Arrays do Numpy são homogêneos, e podemos obter o tipo de dado compartilhado por todos os elementos usando o atributo `dtype`.

# In[8]:


### Inteiro
j = np.array([1, 2])
print(j.dtype)  

### Ponto flutuante
k = np.array([1.0, 2.0])
print(k.dtype)         

### Forçar tipo de dado
l = np.array([1.0, 2.0], dtype=np.int64)
print(l.dtype)


# No momento, você não precisa saber muito sobre os diferentes tipos de dados numéricos.
# Resumidamente, int64 se refere a um número inteiro com sinal de 64 bits (ou 8 bytes), enquanto float64 se refere a um número de ponto flutuante de 64 bits, que pode aproximar qualquer número real.

# #### Aritmética com Arrays
# 
# Funções matemáticas básicas operam elemento a elemento nos arrays, e estão disponíveis tanto usando os símbolos de operadores (+, -, etc.) quanto como funções no módulo numpy:

# In[9]:


x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# Soma elemento a elemento; ambas produzem o array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print("x + y =\n", x + y)
print(np.add(x, y))

# Subtração elemento a elemento; ambas produzem o array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print("\nx - y =\n", x - y)
print(np.subtract(x, y))

# Multiplicação elemento a elemento; ambas produzem o array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print("\nx * y =\n", x * y)
print(np.multiply(x, y))

# Divisão elemento a elemento; ambas produzem o array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print("\nx / y =\n", x / y)
print(np.divide(x, y))

# Raiz quadrada elemento a elemento; produz o array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print("\nsqrt(x) =\n", np.sqrt(x))


# In[10]:


x = np.array([[1, 2], [3, 4]])
print("x =\n", x)

### Calcula a soma de todos os elementos; imprime "10"
print("\nsum(x) =", np.sum(x))

### Calcula a soma de cada coluna; imprime "[4 6]"
print("sum(x, axis=0) =", np.sum(x, axis=0)) 

### Calcula a soma de cada linha; imprime "[3 7]"
print("sum(x, axis=1) =", np.sum(x, axis=1))


# In[11]:


x = np.array([[1, 2], [3, 4]])
print("x =\n", x)

### Calcula a média de todos os elementos; imprime "2.5"
print("\nmean(x) =", np.mean(x))

### Calcula a média de cada coluna; imprime "[2 3]"
print("mean(x, axis=0) =", np.mean(x, axis=0)) 

### Calcula a média de cada linha; imprime "[1.5 3.5]"
print("mean(x, axis=1) =", np.mean(x, axis=1))


# # Manipulação de dados com Pandas
# 
# O Numpy é útil para cálculos matemáticos em que todos os dados são numéricos. Em ciência de dados, no entanto, lidamos frequentemente com dados heterogêneos, incluindo números, textos e valores temporais. O Pandas é uma biblioteca que fornece funcionalidades para trabalhar com esse tipo de dado, que é comum em aplicações reais de ciência de dados. O Pandas oferece ferramentas para manipulação de dados (por exemplo, transformar valores e selecionar subconjuntos), resumir informações, ler e escrever arquivos, entre várias outras tarefas.
# 
# A principal estrutura de dados com a qual o Pandas trabalha é chamada de [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). Trata-se de uma tabela bidimensional em que as linhas normalmente representam casos ou observações (por exemplo, participantes de um concurso de estrelinha), e as colunas representam variáveis. O Pandas também possui uma estrutura unidimensional chamada [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), que vamos encontrar ao acessar uma única coluna de um DataFrame.
# 
# O Pandas possui várias funções chamadas '`read_xxx`' para ler dados em diferentes formatos a partir de fontes "estáticas", como arquivos. Neste momento, vamos focar na leitura de arquivos '`csv`', onde "csv" significa "valores separados por vírgula". Um arquivo CSV é semelhante a uma planilha, mas é armazenado como texto, usando vírgulas para "delimitar" os valores em cada linha. Outros formatos importantes incluem Excel, JSON e SQL, apenas para citar alguns.
# 
# Este é o link para o arquivo `.csv` que exploraremos neste tutorial: [Cartwheel Data](o link leva à seção de conjuntos de dados nos Recursos deste curso).
# 
# Existem muitas outras opções no '`read_csv`' que são bastante úteis. Por exemplo, você pode usar a opção `sep='\t'` em vez do padrão `sep=','` se os campos do seu arquivo estiverem separados por tabulações em vez de vírgulas. Consulte [aqui](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) a documentação completa da função '`read_csv`'.

# ### Importando os Dados

# In[12]:


# Nome do arquivo que contém nosso arquivo .csv
fname = "Cartwheeldata.csv"

# Lê o arquivo .csv e armazena como um DataFrame do Pandas
df = pd.read_csv(fname)

# Imprime o tipo do objeto
type(df)


# ### Dicionário de Variáveis do "Cartwheeldata" dataset

# In[ ]:


| Variável        | Tradução                | Descrição                                                                    |
| --------------- | ----------------------- | ---------------------------------------------------------------------------- |
| `ID`            | Código de identificação | Número único atribuído a cada participante do experimento.                   |
| `Age`           | Idade                   | Idade do participante (em anos).                                             |
| `Gender`        | Gênero                  | Sexo do participante (ex: masculino, feminino).                              |
| `GenderGroup`   | Grupo de gênero         | Classificação do participante com base em seu gênero (usado para análise).   |
| `Glasses`       | Usa óculos              | Indica se o participante usa óculos (ex: sim/não).                           |
| `GlassesGroup`  | Grupo de uso de óculos  | Categoria com base no uso ou não de óculos (ex: "usa", "não usa").           |
| `Height`        | Altura                  | Altura do participante (em centímetros ou metros, depende do dataset).       |
| `Wingspan`      | Envergadura dos braços  | Medida de ponta a ponta dos dedos com os braços estendidos (em cm ou m).     |
| `CWDistance`    | Distância do cartwheel  | Distância percorrida ao realizar um “cartwheel” (estrela lateral).           |
| `Complete`      | Completou a tarefa      | Indica se o participante completou a tarefa do experimento (sim/não).        |
| `CompleteGroup` | Grupo de conclusão      | Categoria baseada na conclusão da tarefa (ex: "completou", "não completou"). |
| `Score`         | Pontuação               | Pontuação atribuída ao desempenho do participante na tarefa.                 |


# ### Vendo os dados

# Podemos visualizar as primeiras linhas do nosso DataFrame chamando o método head().

# In[13]:


df.head()


# O método head() simplesmente mostra as 5 primeiras linhas do nosso DataFrame.
# Se você quiser ver, por exemplo, as 10 primeiras linhas dos dados, pode passar '10' como argumento para o método head:

# In[14]:


df.head(10)


# Como você pode ver, temos uma tabela bidimensional de valores, onde cada linha representa uma observação nos nossos dados de estrelinha, e cada coluna é uma variável que descreve alguma característica dos participantes.
# 
# Para visualizar os nomes das colunas, acesse o atributo 'columns' do DataFrame:

# In[15]:


df.columns


# Em um DataFrame, cada coluna possui um único tipo de dado, mas colunas diferentes podem ter tipos diferentes.
# Isso é importante, pois conjuntos de dados do mundo real contêm variáveis com diferentes tipos, mas dentro de uma mesma variável, todas as observações devem ter o mesmo tipo.
# Acesse o atributo dtypes do DataFrame para ver o tipo de dado de cada coluna.

# In[16]:


df.dtypes


# ### Fatiamento de DataFrames

# Como qualquer tabela, as linhas e colunas de um DataFrame do Pandas podem ser referenciadas por posição. Como o Python sempre começa a contar do 0, as linhas e colunas são numeradas como 0, 1, 2, etc.
# 
# DataFrames do Pandas também possuem "índices" de linha e coluna que, em muitos casos, são mais naturais de usar do que posições numéricas. Por exemplo, se nosso DataFrame contém informações sobre pessoas, podemos ter uma coluna chamada "Age" (Idade). Embora possamos saber que a coluna de idade está na posição 3 (a quarta coluna, por conta da indexação iniciada em zero), geralmente é preferível acessar essa coluna pelo nome ("Age") ao invés da posição (3). Um dos motivos é que podemos manipular o DataFrame e as posições das colunas podem mudar.
# 
# Os valores de índice padrão são simplesmente as posições numéricas. Em muitos casos, não substituímos os índices de linha padrão por outro índice, então não há diferença significativa entre operações baseadas em rótulos e operações baseadas em posição para linhas. No entanto, a maioria dos conjuntos de dados possui nomes de colunas informativos, então é incomum encontrar um DataFrame que use apenas índices de coluna padrão.
# 
# As formas mais comuns de indexar e selecionar valores de DataFrames do Pandas são relativamente diretas, embora também existam técnicas de indexação mais avançadas. Consulte [este link](https://pandas.pydata.org/docs/user_guide/indexing.html) para um tratamento mais completo sobre o assunto.
# 
# Há três formas principais de "fatiar" um DataFrame:
# 
# 1. `.loc()` — seleção com base nos valores dos índices  
# 2. `.iloc()` — seleção com base nas posições  
# 3. `.ix()` — (obsoleto e não recomendado)
# 
# Aqui, vamos abordar as funções de fatiamento `.loc()` e `.iloc()`.
# 
# ### Indexação com `.loc()`
# 
# O método `.loc()` para um DataFrame aceita dois valores de indexação separados por vírgula. O primeiro valor seleciona as linhas e o segundo valor seleciona as colunas. Um valor de indexação pode ser um único índice, um intervalo de índices ou uma lista contendo um ou mais índices. Abaixo fornecemos exemplos que cobrem alguns dos casos de uso mais comuns:

# In[17]:


# Retorna todas as observações da variável CWDistance
df.loc[:, "CWDistance"]


# A sintaxe a seguir é equivalente à que usamos acima:

# In[18]:


df["CWDistance"]


# A sintaxe a seguir também é equivalente aos dois exemplos anteriores, mas é um pouco desaconselhada (em casos raros, esse tipo de sintaxe pode causar conflitos entre nomes de métodos e nomes de variáveis, além de não funcionar quando os nomes das variáveis contêm espaços em branco ou símbolos de pontuação).

# In[19]:


df.CWDistance


# No exemplo a seguir, selecionamos todas as linhas para múltiplas colunas: ["CWDistance", "Height", "Wingspan"].

# In[20]:


df.loc[:,["CWDistance", "Height", "Wingspan"]]


# A sintaxe abaixo é equivalente:

# In[21]:


df[["CWDistance", "Height", "Wingspan"]]


# No exemplo abaixo, selecionamos um intervalo limitado de linhas para múltiplas colunas: ["CWDistance", "Height", "Wingspan"].
# Observe que estamos utilizando os valores de índice de linha padrão, que coincidem com as posições das linhas.

# In[22]:


df.loc[:9, ["CWDistance", "Height", "Wingspan"]]


# Abaixo, selecionamos um intervalo limitado de linhas para todas as colunas:

# In[23]:


df.loc[10:15]


# A função .loc() requer dois argumentos: os índices das linhas e os nomes das colunas que você deseja observar.
# 
# No caso acima, : especifica todas as linhas, e nossa coluna é CWDistance. df.loc[**:**, **"CWDistance"**]

# Agora, digamos que queremos retornar apenas as 10 primeiras observações:

# In[24]:


df.loc[:9, "CWDistance"]


# ### Indexação com `.iloc()`
# 
# O método `.iloc()` é usado para fatiamento baseado em posição.  
# Lembre-se de que o Python utiliza indexação iniciada em zero, portanto o primeiro valor está na posição zero.  
# Abaixo estão alguns exemplos:

# In[25]:


df.iloc[:4]


# In[26]:


df.iloc[1:5, 2:4]


# No próximo exemplo, combinamos fatiamento baseado em posição para as linhas com indexação baseada em rótulo para as colunas:

# In[27]:


df.iloc[1:5, :][["Gender", "GenderGroup"]]


# Podemos visualizar os tipos de dados das colunas do nosso DataFrame acessando o atributo .dtypes do DataFrame:

# In[28]:


df.dtypes


# O resultado indica que temos inteiros, números de ponto flutuante e objetos em nosso DataFrame.
# Uma variável com tipo de dado "object" geralmente contém strings, mas em alguns casos pode conter outros valores que estão "encapsulados" como objetos do Python.
# 
# Também podemos querer observar os diferentes valores únicos dentro de uma coluna específica. Vamos fazer isso para a variável Gender:

# In[34]:


# Lista os valores únicos na coluna df['Gender']
df["Gender"].unique()


# Há outra variável chamada GenderGroup, vamos considerá-la também:

# In[35]:


df["GenderGroup"].unique()


# Parece que essas duas variáveis podem conter informações redundantes. Vamos explorar isso mais a fundo exibindo apenas essas duas colunas:

# In[31]:


df[["Gender", "GenderGroup"]]


# Ao inspecionar essa saída, parece que essas variáveis contêm as mesmas informações, mas codificadas de formas diferentes.
# Podemos confirmar essa suspeita usando a [crosstab](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html) função crosstab do Pandas:

# In[32]:


pd.crosstab(df["Gender"], df["GenderGroup"])


# Pelo resultado acima, fica claro que todas as pessoas cujo Gender é "F" têm o valor 1 em GenderGroup, e todas as pessoas cujo Gender é "M" têm o valor 2.
# 
# O mesmo resultado pode ser obtido usando os métodos groupby() e size():

# In[33]:


df.groupby(['Gender','GenderGroup']).size()


# Novamente, a saída indica que temos duas combinações:
# 
# * Caso 1: Gender = F e GenderGroup = 1
# 
# * Caso 2: Gender = M e GenderGroup = 2
