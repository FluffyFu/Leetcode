from solution import max_len
import pudb


def test():
    arr = ['un', 'iq', 'ue']
    assert 4 == max_len(arr)

    arr = ["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]
    # pudb.set_trace()
    assert 16 == max_len(arr)

    arr = ['e', 'aa']
    # pudb.set_trace()
    assert 1 == max_len(arr)
