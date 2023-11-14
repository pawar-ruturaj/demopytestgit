import pytest


class Test_002:
    @pytest.mark.sum
    def test_sum_04(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
        else:
            assert False