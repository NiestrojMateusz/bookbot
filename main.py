def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    words_count = count_words(text)

    print(f"{words_count} found in text")
    chars_count = count_characters(text.lower())
    print(f"Characters found in text: {chars_count}")


def count_words(text):
    words = text.split()

    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()
