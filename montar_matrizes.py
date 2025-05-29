from iterador_palavras import generator
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)


def contar_tamanho_palavras():
    qtd_tamanhos = {}
    for palavra in generator("wikipedia_pt.txt"):
        tamanho = len(palavra)
        if tamanho in qtd_tamanhos:
            qtd_tamanhos[tamanho] += 1
        else:
            qtd_tamanhos[tamanho] = 1
    
    print(dict(sorted(qtd_tamanhos.items())))

"""
Resultado para todo o dataset:

{
01: 30499652, 
02: 59074605, 
03: 35201237, 
04: 27337236, 
05: 33462486, 
06: 33209654, 
07: 29756618, 
08: 26206394, 
09: 18169382, 
10: 14037035, 
11: 7913312, 
12: 5035885, 
13: 2970877, 
14: 1489926, 
15: 841864, 
16: 334196, 
17: 149484, 
18: 108497, 
19: 55165, 
20: 41382, 
21: 25900, 
22: 18127, 
23: 10160, 
24: 6858, 
25: 4712, 
26: 4189, 
27: 2909, 
28: 2132, 
29: 1663, 
30: 1511, 
31: 1545, 
32: 1145, 
33: 1094, 
34: 868, 
35: 852, 
36: 782, 
37: 669, 
38: 606, 
39: 761, 
40: 584, 
41: 631, 
42: 539, 
43: 562, 
44: 566, 
45: 457, 
46: 972
}
"""

def gerar_histograma_tamanho_palavras():

    valores = {
        1: 30499652, 2: 59074605, 3: 35201237, 4: 27337236, 5: 33462486, 6: 33209654,
        7: 29756618, 8: 26206394, 9: 18169382, 10: 14037035, 11: 7913312, 12: 5035885,
        13: 2970877, 14: 1489926, 15: 841864, 16: 334196, 17: 149484, 18: 108497,
        19: 55165, 20: 41382, 21: 25900, 22: 18127, 23: 10160, 24: 6858, 25: 4712,
        26: 4189, 27: 2909, 28: 2132, 29: 1663, 30: 1511, 31: 1545, 32: 1145,
        33: 1094, 34: 868, 35: 852, 36: 782, 37: 669, 38: 606, 39: 761, 40: 584,
        41: 631, 42: 539, 43: 562, 44: 566, 45: 457, 46: 972
    }

    soma_total = sum(valores.values())

    plt.figure(figsize=(12, 6))
    plt.bar(valores.keys(), valores.values(), color='skyblue')
    plt.title(f'Distribuição de quantidade de letras (Total de palavras: {soma_total:,})')
    plt.xlabel('Tamanho')
    plt.ylabel('Quantidade')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(1, 47), rotation=90)

    plt.tight_layout()
    plt.show()

def gerar_matrizes():
    # Número de matrizes: 47

    # Tamanho da matriz: 42x42
    # 26 letras do alfabeto -> abcdefghijklmnopqrstuvwxyz
    # 14 letras especiais -> áàâãéêíîóôõùúç
    # 2 estados de controle -> <SOW> e <EOW>

    indices = {
        '<SOW>': 0,
        'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26,
        'á':27,
        'à':28,
        'â':29,
        'ã':30,
        'é':31,
        'ê':32,
        'í':33,
        'î':34,
        'ó':35,
        'ô':36,
        'õ':37,
        'ù':38,
        'ú':39,
        'ç':40,
        '<EOW>':41
    }
    
    matrizes = [np.zeros((42,42)) for _ in range(47)]

    print("Iniciando processamento das palavras")

    it = 0
    for palavra in generator("wikipedia_pt.txt"):

        it += 1

        if it % 1000000 == 0:
            print(f"Progresso: {it/1000000}/326")

        if palavra == '':
            continue

        # print(f"Palavra {it}: {palavra}")

        matrizes[0][indices["<SOW>"]][indices[palavra[0]]] += 1
        matrizes[len(palavra)][indices[palavra[-1]]][indices["<EOW>"]] += 1
        for i, char in enumerate(palavra[:-1]):
            letra_inicio = char
            letra_fim = palavra[i+1]
            matrizes[i+1][indices[letra_inicio]][indices[letra_fim]] += 1

    np.savez("matrizes_salvas_nao_normalizadas.npz", *matrizes)
    for i, matriz in enumerate(matrizes):
        print(f"\nMatriz {i+1}:\n{matriz}")


if __name__ == "__main__":
    # contar_tamanho_palavras()
    # gerar_histograma_tamanho_palavras()
    gerar_matrizes()
    pass