import argparse


def gc_content(sequence, percent=False):
    if not sequence:
        return 0.0
    gc_count = sum(1 for base in sequence if base in "GCgc")
    proportion = gc_count / len(sequence)
    return proportion * 100 if percent else proportion


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence")
    parser.add_argument("--percent", action="store_true")
    args = parser.parse_args()

    print(gc_content(args.sequence, percent=args.percent))


if __name__ == "__main__":
    main()
