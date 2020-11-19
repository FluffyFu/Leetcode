from solution import Trie
import pudb


def test_trie():
    trie = Trie()
    trie.insert('apple')
    assert trie.search('apple') == True
    assert trie.search('app') == False
    assert trie.startWith('app') == True
    trie.insert('app')
    assert trie.search('app') == True
