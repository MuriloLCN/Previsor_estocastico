# gerar_matrizes_frases.py

import numpy as np
import spacy
# from collections import defaultdict
import re

pln = spacy.load("pt_core_news_lg")

def limpar(palavra):
    s = re.sub(r'[^a-zA-ZÀ-ÿ]', '', palavra.strip())
    return ''.join([i for i in s if i.isalpha()])

if __name__ == "__main__":

    print(f"Iniciando processamento")

    with open("corpus_juridico.txt", "r+", encoding="UTF-8") as arq:
        texto = arq.read() 
    
    print(f"Arquivo lido")

    texto = texto[0:999999] # Truncando p/ caber no pipeline do spacy

    print(f"Texto truncado")

    tokens = pln(texto)

    print(f"Tokens gerados")

    # tamanhos = {}
    
    # for sentenca in tokens.sents:
    #     t = len(sentenca.text.split())
    #     if t > 3 and t <= 30:
    #         if t not in tamanhos.keys():
    #             tamanhos[t] = 1
    #         else:
    #             tamanhos[t] += 1

    vocabulario = {}
    contagem = 2

#     matrizes = [defaultdict(lambda: defaultdict(int)) for _ in range(MAX_TAMANHO_FRASE)]

    print("Processando corpus...")

    for frase in tokens.sents:
        texto = frase.text.lower()
        palavras = texto.split(" ")

        
        palavras = [limpar(p) for p in palavras if p.strip()]

        palavras = [palavra for palavra in palavras if palavra != ""]

        if not texto:
            continue
        if len(palavras) > 45 or len(palavras) < 3:
            continue
        
        palavras = ["<SOP>"] + palavras + ["<EOP>"]
        
        for pl in palavras:
            if pl not in vocabulario.keys():
                vocabulario[pl] = 1
            else:
                vocabulario[pl] += 1

    vocabulario_truncado = {}

    for item in vocabulario.items():
        if item[1] > 5:
            vocabulario_truncado[item[0]] = item[1]

    vocabulario_truncado = dict(sorted(vocabulario_truncado.items(), key=lambda x: x[1]))

    numero_palavras = len(vocabulario_truncado)

    print(vocabulario_truncado)

    print(numero_palavras)

    indice_vocabulario = {
        palavra: (freq, idx) for idx, (palavra, freq) in enumerate(vocabulario_truncado.items())
    }

    matriz = np.zeros((numero_palavras, numero_palavras, 30))     

    print("Gerando matriz")

    for frase in tokens.sents:
        texto = frase.text.lower()
        palavras = texto.split(" ")

        for palavra in palavras:
            palavra = re.sub(r'[^a-zA-ZÀ-ÿ]', '', palavra)
            ind = ",.;1234567890    "
            for c in ind:
                palavra = palavra.replace(c, "")

        palavras = [palavra for palavra in palavras if palavra != ""]

        if not texto:
            continue
        if len(palavras) > 45 or len(palavras) < 3:
            continue
        
        palavras = ["<SOP>"] + palavras + ["<EOP>"]

        for i in range(len(palavras) - 1):
            if i >= 30:
                break
            
            palavra_atual = palavras[i]
            palavra_proxima = palavras[i + 1]

            if palavra_atual not in indice_vocabulario or palavra_proxima not in indice_vocabulario:
                continue

            idx1 = indice_vocabulario[palavra_atual][1]
            idx2 = indice_vocabulario[palavra_proxima][1]
            
            matriz[idx1, idx2, i] += 1

    print("Salvando matriz e vocabulário...")

    np.savez_compressed("m_frases.npz", matriz)

    with open("vocabulario_frases.txt", "w", encoding="utf-8") as f:
        for palavra, (freq, idx) in indice_vocabulario.items():
            f.write(f"{palavra}\n")

    print("Processamento finalizado.")


