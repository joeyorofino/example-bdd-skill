def gc_content(sequence, percent=False):
    if not sequence:
        return 0.0
    gc_count = sum(1 for base in sequence if base in "GCgc")
    proportion = gc_count / len(sequence)
    return proportion * 100 if percent else proportion
