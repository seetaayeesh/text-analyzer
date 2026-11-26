import re
from collections import Counter


def show_frequencies(label, counts):
    """Print the most common item and the full frequency list."""
    # Negative counts put the highest frequencies first. The item breaks ties.
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    if not ranked:
        return

    item, count = ranked[0]
    print(f"Most frequent {label}: '{item}' ({count} times)")
    print(f"{label.capitalize()} frequencies:")
    for item, count in ranked:
        print(f"{item!r}: {count}")


def main():
    text = input("Enter your text: ").strip()
    if not text:
        print("Please enter some text.")
        return

    # Count original characters, but use lowercase for frequency comparisons.
    normalized = text.lower()
    # Match letters and numbers, keeping Persian half-spaces inside words.
    words = re.findall(r"[^\W_]+(?:\u200c[^\W_]+)*", normalized)
    characters = Counter(char for char in normalized if not char.isspace())

    print(f"Total characters: {len(text)}")
    print(f"Total words: {len(words)}")
    show_frequencies("character", characters)
    show_frequencies("word", Counter(words))


if __name__ == "__main__":
    main()
