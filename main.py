def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = text.split()

    char_counts = get_char_count(text)
    counts_list = []
    for c in char_counts:
        counts_list.append((c , char_counts[c]))
    counts_list.sort(key=lambda tup: tup[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    for x in counts_list:
        print(f"The '{x[0]}' character was found {x[1]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    text = text.lower()
    count_map = {}
    for c in text:
        if c.isalpha():
            if c not in count_map:
                count_map[c] = 1
            else:
                count_map[c] +=1
    return count_map
        
main()