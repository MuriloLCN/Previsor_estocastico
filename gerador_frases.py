import numpy as np

def carregar_vocabulario():
    vocab = {}
    vocab_inv = {}
    with open("vocabulario_frases.txt", "r", encoding="utf-8") as arq:
        for i,linha in enumerate(arq):
            linha = linha.replace("\n", "")
            vocab[linha] = i
            vocab_inv[i] = linha
    return vocab, vocab_inv

vocab, vocab_inv = carregar_vocabulario()
print(vocab)

def escolher_prox_palavra(matrizes, indice_palavra_atual, indice_matriz, vocab_inv):
    linha = matrizes[indice_palavra_atual, :, indice_matriz]
    
    if np.sum(linha) > 0 :
        probs = linha / np.sum(linha) 
    else:
        return vocab["<EOP>"]
    return np.random.choice(len(probs), p=probs)

def gerar_frase():
    global vocab, vocab_inv
    # print(vocab_inv)
    idx_SOP = vocab["<SOP>"]
    idx_EOP = vocab["<EOP>"]

    arq = np.load("m_frases.npz")
    matrizes = arq['arr_0']

    frase = []
    idx_atual = idx_SOP

    for pos in range(29):
        idx_proxima = escolher_prox_palavra(matrizes, idx_atual, pos, vocab_inv)
        palavra = vocab_inv[idx_proxima]

        if palavra == "<EOP>":
            break

        frase.append(palavra)
        idx_atual = idx_proxima

    return " ".join(frase)

if __name__ == "__main__":
    for _ in range(50):
        print("Frase gerada:", gerar_frase())
