def levenshtein_distance(s1, s2):

    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def autocorrect(word, words_file):

    with open(words_file, 'r', encoding='cp1251') as f:
        words_list = [line.strip() for line in f.readlines()]

    min_distance = float('inf')
    corrected_word = word
    for candidate in words_list:
        distance = levenshtein_distance(word, candidate)
        if distance < min_distance:
            min_distance = distance
            corrected_word = candidate

    return corrected_word

def ct(text_lev=None):
    if text_lev is None:
         text_lev =''

    words = text_lev.split()

    corrected_words = []
    words_file = 'RUS.txt'
    for word in words:
        corrected_words.append(autocorrect(word, words_file))

    corrected_text = ' '.join(corrected_words)
    return corrected_text



#Пример использования программы
# text = input("Введите текст: ")
# words = text.split()
#
# corrected_words = []
# words_file = 'RUS.txt'
# for word in words:
#     corrected_words.append(autocorrect(word, words_file))
#
# corrected_text = ' '.join(corrected_words)
# print("Исправленное: ",corrected_text)