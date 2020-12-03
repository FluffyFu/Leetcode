from solution2 import Solution


def test_solution():
    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    assert Solution().ladder_length(begin_word, end_word, word_list) == 5
