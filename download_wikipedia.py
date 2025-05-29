from datasets import load_dataset
from tqdm import tqdm
import os

OUTPUT_FILE = "wikipedia_pt.txt"
DATASET_NAME = "dominguesm/wikipedia-ptbr-20230601"


def is_valid_text(text):
    # Ignora textos com fórmulas ou marcações típicas
    blacklist = ["<math>", "{{", "}}", "<ref", "</ref>"]
    return not any(b in text for b in blacklist)


def save_wikipedia_text(output_file):
    print(f"Carregando dataset '{DATASET_NAME}'...")
    dataset = load_dataset(DATASET_NAME, split="train")

    print(f"Salvando texto limpo em '{output_file}'...")
    with open(output_file, "w", encoding="utf-8") as f:
        for item in tqdm(dataset, desc="Processando artigos"):
            text = item.get("text", "")
            if is_valid_text(text):
                f.write(text.strip() + "\n\n")

    print(f"\n✅ Concluído! Texto salvo em: {output_file}")


if __name__ == "__main__":
    save_wikipedia_text(OUTPUT_FILE)
