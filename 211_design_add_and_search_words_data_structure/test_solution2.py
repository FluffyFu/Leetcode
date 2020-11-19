from solution2 import WordDictionary
import pudb


def test_word_dict():
    word_dict = WordDictionary()
    word_dict.addWord('bad')
    assert word_dict.search('bad') == True
    assert word_dict.search('.ad') == True
    assert word_dict.search('..d') == True

