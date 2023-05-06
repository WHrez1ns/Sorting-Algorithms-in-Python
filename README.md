<a href="https://www.fiap.com.br/">
<img src="img/fiap.png" width="140" height="50">
</a> <br>

<a href="https://www.instagram.com/fiapoficial/">
<img src="img/ig.png">
</a>
<a href="https://www.youtube.com/@FiapBrasil">
<img src="img/yt.png">
</a>

# Sorting-Algorithms

## Checkpoint 12/05/2023

<br>

### Objetivo:

<br>

O grupo deverá escolher 3 algoritmos de ordenação e testá-los, escolhendo o mais rápido, implementá-los e medir o tempo gasto para realizar a ordenação de uma lista de senhas.

- Editor Utilizado: <a href="https://code.visualstudio.com/"> Visual Studio Code</a>.

- <a href="https://">

  Video Explicativo
  </a>

- <a href="https://"> Slides
  </a><br>

# Algoritmos de Ordenação escolhidos

## Algoritmo de Bubble Sort

Bubble Sort é um algoritmo de classificação (ou ordenação) simples que funciona comparando pares de elementos adjacentes em uma lista e trocando suas posições se estiverem na ordem errada. O algoritmo percorre a lista várias vezes, comparando e trocando os elementos adjacentes até que a lista esteja completamente ordenada.

O Bubble Sort é um dos algoritmos de classificação mais simples e intuitivos, mas também é um dos menos eficientes. Sua complexidade de tempo é O(n^2), o que significa que o tempo de execução do algoritmo aumenta exponencialmente com o tamanho da lista a ser classificada.

O processo de ordenação do Bubble Sort pode ser visualizado como "borbulhar" os elementos maiores para o final da lista, à medida que eles são comparados e trocados com os elementos adjacentes menores. A implementação do Bubble Sort é relativamente fácil, mas é mais adequada para listas pequenas ou já quase ordenadas, pois sua eficiência diminui drasticamente com o aumento do tamanho da lista.

## Algoritmo de Quick Sort

Quick Sort é um algoritmo de ordenação que utiliza a abordagem "divide and conquer" (dividir e conquistar) para ordenar uma lista de elementos. A ideia básica do Quick Sort é selecionar um elemento como pivô e rearranjar os outros elementos em relação a ele, de forma que os elementos menores que o pivô fiquem à esquerda e os elementos maiores à direita. Em seguida, o algoritmo é recursivamente aplicado para a sublista à esquerda e à direita do pivô, até que a lista completa esteja ordenada.

A escolha do pivô é uma parte importante do algoritmo, pois pode afetar significativamente a eficiência do Quick Sort. Idealmente, o pivô deve ser escolhido de forma a dividir a lista em duas partes iguais, mas isso nem sempre é possível. Uma das estratégias mais comuns é selecionar o elemento do meio como pivô, mas outras estratégias, como a seleção aleatória do pivô, também são utilizadas.

A complexidade de tempo do Quick Sort é O(n log n) em média, mas pode chegar a O(n^2) no pior caso, quando a escolha do pivô é feita de forma inadequada e a lista já está quase ordenada. No entanto, em geral, o Quick Sort é um algoritmo de ordenação muito eficiente e é amplamente utilizado em aplicações que envolvem grandes quantidades de dados a serem ordenados, como processamento de banco de dados e ordenação de arquivos.

O Quick Sort é um algoritmo in-place, o que significa que ele pode ser implementado de forma que a ordenação seja feita diretamente na lista de entrada, sem a necessidade de armazenar dados adicionais na memória. Isso o torna uma opção atraente em sistemas com recursos limitados de memória.

## Algoritmo de Merge Sort

Merge Sort é um algoritmo de ordenação que utiliza a abordagem "divide and conquer" (dividir e conquistar). A ideia básica do Merge Sort é dividir a lista de elementos a serem ordenados em duas metades menores, ordenar cada metade de forma recursiva e, em seguida, combinar as duas metades ordenadas em uma única lista ordenada.

O processo de divisão é repetido até que cada sublista contenha apenas um elemento, o que, por definição, já está ordenado. Em seguida, as sublistas são mescladas em pares, ordenando-as simultaneamente, até que a lista completa seja reconstruída.

A complexidade de tempo do Merge Sort é O(n log n), o que o torna um algoritmo de ordenação muito eficiente em comparação com outros algoritmos de complexidade quadrática, como o Bubble Sort. Além disso, o Merge Sort é estável, ou seja, a ordem relativa dos elementos com chaves iguais é mantida após a ordenação.

O Merge Sort é amplamente utilizado em aplicações que envolvem grandes quantidades de dados a serem ordenados, como processamento de banco de dados e ordenação de arquivos. Sua principal desvantagem é que requer espaço adicional na memória para armazenar as sub-listas durante o processo de ordenação, o que pode torná-lo menos eficiente em sistemas com recursos limitados de memória.

# Explicação dos códigos

## Código do Bubble Sort

### Função Bubble Sort - functions.py

```
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
```

O código apresenta uma implementação do algoritmo de ordenação Bubble Sort em Python.

A função <span style="color: yellow;"> **_bubble_sort_** </span> recebe uma lista de elementos como argumento e retorna a lista ordenada em ordem crescente. A lógica do algoritmo é simples: percorrer a lista várias vezes, comparando e trocando os elementos adjacentes até que a lista esteja completamente ordenada.

O primeiro passo do algoritmo é obter o comprimento da lista, que é armazenado na variável <span style="color: #123889;"> **_n_** </span>. Em seguida, o algoritmo percorre a lista utilizando dois loops <span style="color: #d40f47;"> **_for_** </span>. O loop externo (<span style="color: #d40f47;">**_for </span> i <span style="color: #d40f47;"> in </span> <span style="color: #00a624;"> range</span>(<span style="color: #123889;">n</span>)_**) é responsável por percorrer a lista n vezes, garantindo que todos os elementos sejam comparados e trocados, se necessário.

O loop interno (<span style="color: #d40f47;">**_for</span> j <span style="color: #d40f47;">in</span> <span style="color: #00a624;">range</span>(<span style="color: #9900b8;">0</span>, n-i-<span style="color: #9900b8;">1</span>)_**) percorre a lista a cada iteração do loop externo, comparando os elementos adjacentes e trocando-os, se necessário. O índice <span style="color: orange;">**_j_**</span> varia de 0 a **_n-i-<span style="color: #9900b8;">1_**</span>, garantindo que apenas os elementos ainda não ordenados sejam comparados.

A condição <span style="color: #d40f47;">**_if</span> lista[<span style="color: orange;">j</span>] > lista[<span style="color: orange;">j+1</span>]_** verifica se o elemento atual (**_lista[<span style="color: orange;">j</span>]_**) é maior que o próximo elemento (**_lista[<span style="color: orange;">j+1</span>]_**). Se a condição for verdadeira, os elementos são trocados utilizando a sintaxe **_lista[<span style="color: orange;">j</span>], lista[<span style="color: orange;">j+1</span>] = lista[<span style="color: orange;">j+1</span>], lista[<span style="color: orange;">j</span>]_**.

Ao final das iterações, a lista estará ordenada e é retornada pela função. A complexidade de tempo do Bubble Sort é O(n^2), onde **_n_** é o número de elementos na lista, o que pode tornar este algoritmo menos eficiente em comparação com outros algoritmos de ordenação, como o Merge Sort e o Quick Sort, para listas maiores.

### Script Bubble Sort - script.py

```
from functions import bubble_sort
import time
import matplotlib.pyplot

with open("wordlists/probable-v2-top12000.txt", "r") as arquivo:
    lista = arquivo.read().splitlines()
result = []
cont = 0
total = 0
while cont < 15:
    start_time = time.time()
    ordenada = bubble_sort(lista)
    end_time = time.time()
    total_time = end_time - start_time
    result.append(float(total_time))
    print("\033[30m--------------------------------------------------------")
    print("\033[34m", ordenada)
    print("\033[30m--------------------------------------------------------")
    print("\033[32mTempo de execução: {:.5f} segundos".format(total_time))
    print("\033[30m--------------------------------------------------------")
    print("\033[36mTamanho da wordlist: {} palavras".format(len(lista)))
    cont += 1
media = sum(result) / len(result)
print("\033[30m--------------------------------------------------------")
print("\033[33mTestes realizados:", result)
print("\033[30m--------------------------------------------------------")
print("\033[35mMédia de tempo: {}".format(media))
print("\033[30m--------------------------------------------------------")
matplotlib.pyplot.title(
    'Média do tempo de execução do Algoritmo de Bubble Sort')
matplotlib.pyplot.xlabel('Teste')
matplotlib.pyplot.ylabel('Tempo (s)')
matplotlib.pyplot.plot(result)
matplotlib.pyplot.ylim(0, 10)
matplotlib.pyplot.xlim(0, 10)
matplotlib.pyplot.show()
```

Este código realiza o teste de desempenho do algoritmo Bubble Sort em uma lista de palavras obtida de um arquivo.

O código começa importando a função <span style="color: yellow">**_bubble_sort_**</span> de um módulo chamado "functions" e também importa os módulos <span style="color: yellow">**_time_**</span> e <span style="color: yellow">**_matplotlib.pyplot._**</span> Em seguida, o código abre o arquivo <span style="color: #d40f47;">**"probable-v2-top12000.txt"**</span> que contém uma lista de palavras em ordem aleatória. O método <span style="color: #00a624;">**_read()_**</span> é usado para ler todo o conteúdo do arquivo e o método <span style="color: #00a624;">**_splitlines()_**</span> é usado para separar as linhas em uma lista de palavras.

A partir disso, o código entra em um loop while que é executado 15 vezes. A cada iteração, o algoritmo Bubble Sort é executado na lista de palavras e o tempo de execução é medido usando a função <span style="color: #00a624;">**_time.time()_**</span>. O tempo de execução é armazenado em uma lista <span style="color: orange;">**_result_**</span>.

Além disso, durante cada iteração, o código imprime a lista ordenada, o tempo de execução e o tamanho da lista de palavras. A cor do texto é definida usando códigos ANSI de escape. Isso é feito usando a sintaxe <span style="color: #123889;">**_\033[CORm_**</span>, onde "COR" é o código da cor e "m" é o código de fim de sequência. Por exemplo, <span style="color: #123889;">**_\033[32m_**</span> define a cor do texto para verde.

Após as 15 iterações, o código calcula a média dos tempos de execução e imprime os resultados. Em seguida, o código usa a biblioteca <span style="color: #00a624;">**_matplotlib.pyplot_**</span> para criar um gráfico da média dos tempos de execução. O gráfico mostra o tempo de execução em segundos no eixo Y e o número do teste no eixo X. A biblioteca <span style="color: #00a624;">**_matplotlib.pyplot_**</span> é usada para configurar as propriedades do gráfico e exibi-lo na tela.

### Gráfico da médio do tempo de execução

# Colaboradores

<a href="https://github.com/Aykie"> Júlia Barboza Brunelli</a>, <a href="https://github.com/NCalegariS"> Nicholas Calegari</a> e <a href="https://github.com/WHrez1ns"> Renan Dias</a>
<br>
**RM: 98558, 93912 e 99258.**
