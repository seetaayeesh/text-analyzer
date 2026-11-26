import re
import sys
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


def read_text():
    """Read one valid line, or return None when input ends."""
    encoding = sys.stdin.encoding or "utf-8"
    while True:
        print("Enter your text: ", end="", flush=True)
        # Decode one line at a time so a bad line cannot discard the next one.
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        try:
            return line.decode(encoding).strip()
        except UnicodeDecodeError:
            print("Invalid text encoding. Please enter the text again.")


def main():
    text = read_text()
    if text is None:
        return
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
