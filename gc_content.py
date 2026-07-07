def gc_content(sequence):
    if not sequence:
        return 0.0
    gc_count = sum(1 for base in sequence if base in "GCgc")
    return gc_count / len(sequence)
