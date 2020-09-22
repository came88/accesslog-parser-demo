"""

This is a minimal python file with a test.

pytest .

"""


def maximum(l: list):
    """Fix this test, eg. using
    return max()

    :param l - a list of numbers
    :return the maximum number in the list

    @solution
    """
    if not isinstance(l, (list, tuple, set)):
        raise ValueError("Non una lista")
    if not l:
        raise ValueError("Non so il massimo di una lista vuota")
    best = next(iter(l))
    for n in l:
        if n > best:
            best = n
    return best


def test_one():
    """This is a nice test"""
    case = [4, 3, 2, 1, 0]
    expected = 4
    assert maximum(case) == expected


def test_two():
    """This is a nicer test"""
    case = [1, 3, 2, 4, 0]
    expected = 4
    assert maximum(case) == expected


def test_three():
    try:
        maximum([])
    except ValueError as e:
        assert e.args == ("Non so il massimo di una lista vuota",)
        
def test_four():
    """This is a string test"""
    case = ["matteo", "roberto", "lorenzo"]
    expected = "roberto"
    assert maximum(case) == expected

def test_five():
    """This is a string test"""
    try:
        maximum(5)
    except ValueError as e:
        assert e.args == ("Non una lista",)

def test_fail():
    assert 1 == 0  # This is supposed to fail
