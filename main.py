def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    get_chars_report(text, book_path)

def get_count_words(text):
    words = text.split()

    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_characters_dict(text):
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_sotrted_counted_alphabethical_chars_list(text, descending):
    chars_count = get_count_characters_dict(text.lower())
    chars_count_dict_list = chars_count_dict_to_list(chars_count)
    chars_count_dict_list.sort(key=lambda c: c['count'], reverse=descending)
    filtered_chars_list = filter(lambda c: c["char"].isalpha(), chars_count_dict_list)

    return list(filtered_chars_list)

def chars_count_dict_to_list(chars_dict):
    chars_list = []

    for char in chars_dict:
        chars_list.append({"char": char, "count": chars_dict[char]})

    return chars_list

def get_chars_report(text, path):
    print(f"--- Begin report of {path} ---")
    words_count = get_count_words(text)
    print(f"{words_count} words found in the document\n")
    sorted_chars_list = get_sotrted_counted_alphabethical_chars_list(text, True)

    for char_item in sorted_chars_list:
        print(f"The \'{char_item['char']}\' character was found {char_item['count']} times")

    print("--- End report ---")


main()
