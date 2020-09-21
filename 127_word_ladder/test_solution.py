from solution import Solution, Solution_2
import pudb


def test_solution():
    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    assert Solution().ladder_length(begin_word, end_word, word_list) == 5

    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log']

    assert Solution().ladder_length(begin_word, end_word, word_list) == 0

    begin_word = 'hot'
    end_word = 'dog'
    word_list = ['hot', 'dog']

    # pudb.set_trace()
    assert Solution().ladder_length(begin_word, end_word, word_list) == 0


def test_solution_2():
    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

    # pudb.set_trace()
    assert Solution_2().ladder_length(begin_word, end_word, word_list) == 5

    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log']

    assert Solution_2().ladder_length(begin_word, end_word, word_list) == 0

    begin_word = 'hot'
    end_word = 'dog'
    word_list = ['hot', 'dog']

    assert Solution_2().ladder_length(begin_word, end_word, word_list) == 0
