import time


def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x < pivo]
        maiores = [x for x in lista[1:] if x >= pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)


with open("wordlists/probable-v2-top12000.txt", "r") as arquivo:
    lista = arquivo.read().splitlines()


start_time = time.time()
ordenada = quick_sort(lista)
end_time = time.time()
total_time = end_time - start_time
print("--------------------------------------------------------")
print(ordenada)
print("--------------------------------------------------------")
print("Tempo de execução: {:.5f} segundos".format(total_time))
print("--------------------------------------------------------")
print("Tamanho da Wordlist: {} palavras".format(len(lista)))
