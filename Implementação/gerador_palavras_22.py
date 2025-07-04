import numpy as np
# import matplotlib.pyplot as plt
# from collections import Counter
# import seaborn as sns

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
    '#': 41
}
indices_reverso = {v: k for k, v in indices.items()}

def gerar_palavra(matriz):
    palavra = ""
    letra_atual = "+"
    for i in range(matriz.shape[2]):
        linha = matriz[indices[letra_atual], :, i]
        soma = np.sum(linha)

        if soma == 0:
            probs = np.ones_like(linha) / len(linha)
        else:
            probs = linha / soma

        idx_escolhido = np.random.choice(len(probs), p=probs)
        nova_letra = indices_reverso[idx_escolhido]

        if nova_letra == "#":
            break
        palavra += nova_letra
        letra_atual = nova_letra

    return palavra

if __name__ == "__main__":
    print("Carregando matriz...")
    dados = np.load("m_const_letras.npz")
    matriz = dados['arr_0']

    print("Gerando palavras...")
    # tamanhos = []
    # palavras = []

    for _ in range(int(input("Insira quantas palavras a serem geradas: "))):
        palavra = gerar_palavra(matriz)
        print(palavra)
        # palavras.append(palavra)
        # tamanhos.append(len(palavra))
