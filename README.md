# BookBot

A Python command-line application that performs text analysis on novels and large text files. BookBot generates detailed statistics such as total word count and character frequency analysis for books like *Frankenstein*, *Moby-Dick*, and *Pride and Prejudice*.

---

## Overview

BookBot was built to strengthen core Python programming fundamentals, file handling, data processing, and command-line application development. The project focuses on analyzing raw text data and presenting structured reports directly in the terminal.

This project demonstrates:

- Python scripting and CLI development
- File I/O operations
- Data analysis using dictionaries and loops
- Sorting and formatting structured output
- Modular project organization

---

## Features

- Analyze entire `.txt` novels or text files
- Count the total number of words in a book
- Calculate character frequency statistics
- Generate clean terminal-based reports
- Works with public-domain books from [Project Gutenberg](https://www.gutenberg.org)

---

## Screenshots



---

## Example Output

```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
...
============= END ===============
```

---

## Tech Stack

- Python

---

## Project Structure

```bash
bookbot/
│── books/
│── main.py
│── stats.py
│── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/codeharman/bookbot.git
```

Move into the project directory:

```bash
cd bookbot
```

Ensure Python 3 is installed:

```bash
python3 --version
```

---

## Usage

Place a `.txt` book file inside the `books/` directory and run:

```bash
python3 main.py books/frankenstein.txt
```

---

## Skills Demonstrated

- Command-line application development
- Python functions and modules
- Dictionary-based data aggregation
- String manipulation and parsing
- Basic software architecture and project organization
- Problem-solving with real-world datasets

---

## Future Improvements

- Add support for multiple file formats
- Export reports to CSV or JSON
- Add visualization for word statistics
- Implement unit testing
- Add advanced NLP features such as sentiment analysis

---

## Learning Resources

Book data sourced from:

- [Project Gutenberg](https://www.gutenberg.org)

---

## License

This project is licensed under the MIT License.
