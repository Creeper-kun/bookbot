def main():
    import sys
    from stats import get_num_words, num_letters, sort

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Get the data
    word_count = get_num_words(book_path)
    char_counts = num_letters(book_path)
    sorted_chars = sort(char_counts)

    # Print the report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Print character count section
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")

    # Print footer
    print("============= END ===============")
if __name__ == "__main__":
    main()