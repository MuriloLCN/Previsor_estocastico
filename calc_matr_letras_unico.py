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
        'ó':34,
        'ô':35,
        'õ':36,
        'ú':37,
        'ç':38,
        '#':39
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

    # Tamanho da matriz: 40x40
    # 26 letras do alfabeto -> abcdefghijklmnopqrstuvwxyz
    # 14 letras especiais -> áàâãéêíóôõúç
    # 2 estados de controle -> <SOW> e <EOW>

    matriz = np.zeros((40, 40))

    matriz[39][39] = 1

    tamanhos = {}

    it = 0
    alvo = 999999

    # for sentenca in tokens.sents:
    #     tamanho = len(sentenca)
    #     if tamanho in tamanhos.keys():
    #         tamanhos[tamanho] += 1
    #     else:
    #         tamanhos[tamanho] = 1

    for token in tokens:
        if token.is_alpha:
            texto_token = "+" + token.text.lower() + "#"
            for k in range(len(texto_token) - 1):  # até penúltima letra
                a = texto_token[k]
                b = texto_token[k + 1]
                if a in indices and b in indices:
                    ia = indices[a]
                    ib = indices[b]
                    matriz[ia][ib] += 1
    
    print("Salvando resultados")

    np.savez_compressed("m_const_letras_unico.npz", matriz)
            