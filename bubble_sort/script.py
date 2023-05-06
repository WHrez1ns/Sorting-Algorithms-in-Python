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
