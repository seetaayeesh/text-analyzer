# Text Analyzer

[راهنمای فارسی](README_FA.md)

Enter a line of text to count its characters and words and find which ones appear most often. The output includes a frequency list for both.

## Quick install on Ubuntu

Run this command in your terminal. It needs `curl` and Python 3.8 or later.

```bash
bash -o pipefail -c 'curl -fsSL https://raw.githubusercontent.com/seetaayeesh/text-analyzer/main/install.sh | bash'
```

Then launch the program.

```bash
~/.local/bin/text-analyzer
```

The installer uses your home directory. Run the same install command to update. If a prerequisite is missing, run `sudo apt update && sudo apt install curl python3` first.

## Run the program

Use Python 3.8 or later. From this repository’s folder, run the following command.

```bash
python3 main.py
```

On Windows, use `py main.py`. No extra packages are required.

## Try an example

The program continues with the full frequency lists after these summary lines.

```text
Enter your text: Hello hello, Python!
Total characters: 20
Total words: 3
Most frequent character: 'l' (4 times)
```

The most frequent word is `hello`, which appears twice.

## How the counts work

- The total character count includes internal spaces and punctuation. Leading and trailing whitespace is trimmed.
- Character frequencies skip whitespace. Words are made of letters or digits, and a Persian half-space can join two parts of a word.
- The program converts the text to lowercase before tallying frequencies with `Counter`. It lists the highest counts first and uses Python’s string order to break ties.

[MIT license](LICENSE)
