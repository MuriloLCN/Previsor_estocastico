def generator(path):
    word = ''
    with open(path, 'r', encoding='utf-8') as file:
        while True:
            char = file.read(1)
            if char.isspace():
                if word:
                    if len(word) > 46:
                        word = ''
                    yield word
                    word = ''
            elif char == '':
                if word:
                    if len(word) > 46:
                        word = ''
                    yield word
                break
            else:
                char = char.lower()
                if char in "abcdefghijklmnopqrstuvwxyz" + \
                           "áàâãéêíîóôõùúç":
                    word += char

# Instantiate the word generator.
# words = generator('wikipedia_pt.txt')

# Print the very first word.
# print(next(words))

# Print the remaining words.
# for word in words:
#     print(word)