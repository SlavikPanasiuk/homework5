import pytest
from text_processor import convert_to_lowercase, tokenize_text, sentence_tokenize, word_count, character_count, unique_words, find_occurrences, average_word_length

@pytest.mark.parametrize('text, expected', [
    ("ТЕКСТ ДЛЯ ПРОВІРКИ", "текст для провірки"),
    ("Текст для провірки", "текст для провірки"),
    ("ТЕКСТ для провірки", "текст для провірки"),
])
                                          
def test_convert_to_lowercase(text, expected):
    assert convert_to_lowercase(text) == expected                                                             
                         
@pytest.mark.parametrize('text, expected', [
     ("текст для провірки", ["текст", "для", "провірки"]),
     ("Це тестовий текст", ["Це", "тестовий", "текст"])
])                                                                                       

def test_tokenize_text(text, expected):
    assert tokenize_text(text) == expected
 
@pytest.mark.parametrize('text, expected', [
    ("one one two two", 2),
    ("one two two", 2) 
])
                        
def test_unique_words(text, expected):
    assert unique_words(text) == expected 
                            
@pytest.mark.parametrize('text, expected', [
    ("перше реченя. друге реченя", ['перше реченя', ' друге реченя'] ),
    ("one. two", ['one', ' two'])
])
                             
def test_sentence_tokenize(text, expected):
    assert sentence_tokenize(text) == expected  
                         
@pytest.mark.parametrize('text, expected', [
    ("текст для провірки", 3),
    ("one two", 2)
])
                             
def test_word_count(text, expected):
    assert word_count(text) == expected
     
@pytest.mark.parametrize('text, expected', [
    ("текст для провірки", 18),
    ("one two three", 13)
])
           
def test_character_count(text, expected):
    assert character_count(text) == expected 

@pytest.mark.parametrize('text, keyword, expected', [
    ("one two two", "two", 2),
    ("one two two three three three", "three", 3)
])
          
def test_find_occurrences(text, keyword, expected):
    assert find_occurrences(text, keyword) == expected 

@pytest.mark.parametrize('text, expected', [
    ("текст для провірки", 6.0),
    ("one two three", 4.333333333333333)
])
       
def test_average_word_length(text, expected):
    assert average_word_length(text) == expected                              
                         
                         
                         
                         
                         
                         
                         
                         
                         

   