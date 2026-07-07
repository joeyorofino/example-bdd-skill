from gc_content import gc_content


class TestGcContentPercentArgument:
    def test_percent_true(self):
        assert gc_content("GGGC", percent=True) == 100

    def test_percent_false(self):
        assert gc_content("GGGC", percent=False) == 1.0

    def test_percent_default(self):
        assert gc_content("GGGC") == 1.0
