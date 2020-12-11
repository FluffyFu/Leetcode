from solution3 import WordDictionary
import pudb


def test_word_dictionary():
    wd = WordDictionary()
    wd.addWord('abc')
    assert wd.search('a') == False
    assert wd.search('a..') == True
