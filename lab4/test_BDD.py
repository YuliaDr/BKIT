import re
from pytest_bdd import scenario, given, then, parsers
from lab1 import get_roots

@scenario("BDD.feature", "Get roots of a biquadratic equation")
def test_roots():
    pass

@given(parsers.parse('I give coefficients {a:d}, {b:d}, {c:d}'), target_fixture='res')
def give_roots(a, b, c):
    return get_roots(a, b, c)

@then('I get {roots} roots')
def get_result(roots, res):
    roots = list(map(int, roots.split()))
    assert res == roots