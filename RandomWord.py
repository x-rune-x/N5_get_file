def create_word_list(hira_file, eng_file):
    hiragana_file_object = open(hira_file, "r", encoding="utf8")
    english_file_object = open(eng_file, "r")

    word_list = []

    for line in hiragana_file_object:
        hira_word = line.rstrip("\n")
        eng_word = english_file_object.readline()
        eng_word = eng_word.rstrip("\n")

        word_list.append((hira_word, eng_word))

    hiragana_file_object.close()
    english_file_object.close()

    return word_list


new_word_list = create_word_list("hiragana.txt", "english.txt")
print(new_word_list)
