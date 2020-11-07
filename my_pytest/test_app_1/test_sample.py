import pytest
import sys
from my_pytest.test_app_1.sample import sum

@pytest.mark.skip(reason="You are the reason :D")
def test_sum():
    assert sum(1,2) == 3

@pytest.mark.skipif(sys.version_info >(3,7),reason="I want older interpreter")
def test_str():
    assert sum("a", "b") == "ab"


#ignore some exceptions
@ pytest.mark.xfail(sys.platform == "win32",reason = "don't run on windows")
def test_sum_list():
    assert sum([1],[2]) == [1,2]
    raise  Exception()