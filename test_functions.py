import helper

class TestMath:
    def test_one(self):
        assert helper.doAdd(1, 2) == 3

    def test_two(self):
        assert helper.doSub(3, 1) == 2

