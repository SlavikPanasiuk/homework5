def convert_to_lowercase(text):
    return text.lower()

def tokenize_text(text):
    return text.split()

def sentence_tokenize(text):
    return text.split(".")

def word_count(text):
    return len(text.split()
               )
def character_count(text):
    return len(text)

def unique_words(text):
    words = set(text.split())
    return len(words)

def find_occurrences(text, keyword):
    words = text.split()
    c = 0
    for w in words:
        if w == keyword:
         c += 1
    return c  

def average_word_length(text):
  words = text.split()
  total_length = sum(len(word) for word in words)
  return total_length / len(words)


