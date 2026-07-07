from gc_content import gc_content


class TestGcContent:
    def test_mixed_sequence(self):
        assert gc_content("GCAT") == 0.5

    def test_all_gc(self):
        assert gc_content("GGGG") == 1.0
