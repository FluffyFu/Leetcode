from solution import str2tree, stack_solution
import pudb


def test():
    s = "-4(2(3)(1))(6(5))"
    pudb.set_trace()
    # root = str2tree(s)
    root = stack_solution(s)
