from stats import word_count, char_count, char_dict_sorted
import sys

def get_book_text(filepath: str) -> list[str]:
    with open(filepath) as f:
        contents = f.read()

    return contents


def init():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def main():
    book_path = init()
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
   
    print("--------- Character Count -------")
    char_counts = char_count(book_text)
    char_counts_sorted = char_dict_sorted(char_counts)
    for item in char_counts_sorted:
        character = item["char"]
        if character.isalpha():
            print(f"{character}: {item["num"]}")

    print("============= END ===============")


if __name__=="__main__":
    main()