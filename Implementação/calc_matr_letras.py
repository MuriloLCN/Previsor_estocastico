import spacy
import matplotlib.pyplot as plt
import numpy as np

np.set_printoptions(threshold=np.inf, linewidth=np.inf)
pln = spacy.load("pt_core_news_lg")

indices = {
        '+': 0,
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
        '#':41
    }

texto = ""

if __name__ == "__main__":
    
    print(f"Iniciando processamento")

    with open("corpus_juridico.txt", "r+", encoding="UTF-8") as arq:
        texto = arq.read() 
    
    print(f"Arquivo lido")

    texto = texto[0:999999] # Truncando p/ caber no pipeline do spacy

    print(f"Texto truncado")

    tokens = pln(texto)

    print(f"Tokens gerados")

    # Número de matrizes: 47

    # Tamanho da matriz: 42x42
    # 26 letras do alfabeto -> abcdefghijklmnopqrstuvwxyz
    # 14 letras especiais -> áàâãéêíîóôõùúç
    # 2 estados de controle -> <SOW> e <EOW>

    matriz = np.zeros((42, 42, 47))

    tamanhos = {}

    it = 0
    alvo = 999999

    for sentenca in tokens.sents:
        tamanho = len(sentenca)
        if tamanho in tamanhos.keys():
            tamanhos[tamanho] += 1
        else:
            tamanhos[tamanho] = 1

    # for token in tokens:
    #     if token.is_alpha:
    #         texto_token = "+" + token.text.lower() + "#"
    #         for k in range(len(texto_token) - 1):  # até penúltima letra
    #             a = texto_token[k]
    #             b = texto_token[k + 1]
    #             if a in indices and b in indices and k < 47:
    #                 ia = indices[a]
    #                 ib = indices[b]
    #                 matriz[ia][ib][k] += 1
    
    # print("Salvando resultados")

    # np.savez_compressed("m_const_letras.npz", matriz)
            

    tamanhos_ordenados = dict(sorted(tamanhos.items()))

    soma_total = sum(tamanhos_ordenados.values())
    
    plt.figure(figsize=(12, 6))
    plt.bar(tamanhos_ordenados.keys(), tamanhos_ordenados.values(), color='blue')
    plt.title(f'Distribuição do tamanho das palavras do córpus (Total de palavras: {soma_total:,})')
    plt.xlabel('Tamanho')
    plt.ylabel('Quantidade')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(range(1, len(tamanhos)), rotation=90)

    plt.tight_layout()
    plt.show()
