import text_processor as tp
print(tp.convert_to_lowercase("ТЕКСТ ДЛЯ ПРОВІРКИ"))
print(tp.tokenize_text("текст для провірки"))
print(tp.sentence_tokenize("one. two"))
print(tp.word_count("текст для провірки"))
print(tp.character_count("текст для провірки"))
print(tp.unique_words("текст для провірки текст"))
print(tp.find_occurrences("one two two three three three", "three"))
print(tp.average_word_length("one two three"))