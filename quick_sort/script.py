from functions import quick_sort
import time


with open("wordlists/probable-v2-top12000.txt", "r") as arquivo:
    lista = arquivo.read().splitlines()


start_time = time.time()
ordenada = quick_sort(lista)
end_time = time.time()
total_time = end_time - start_time
print("\033[30m--------------------------------------------------------")
print("\033[34m", ordenada)
print("\033[30m--------------------------------------------------------")
print("\033[32mTempo de execução: {:.5f} segundos".format(total_time))
print("\033[30m--------------------------------------------------------")
print("\033[36mTamanho da wordlist: {} palavras".format(len(lista)))
