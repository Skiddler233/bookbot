def main():
    def read_book(book):
        with open(f"books/{book}") as f:
            file_contents = f.read()
        words = file_contents.split()
        length = len(words)
        return length, words

    def num_char():
        length, words = read_book("frankenstein.txt")
        character_counts = {}
        for character in "abcdefghijklmnopqrstuvwxyz1234567890":
            character_counts[character] = 0

        for word in words:
            for char in word.lower():
                if char in character_counts:
                    character_counts[char] += 1
        return character_counts

    def report(book):
        length, words = read_book(book)
        character_count = num_char()
        print(f"--- Begin report of books/{book} ---")    
        print(f"{length} words found in the document.")
        for i in character_count:
            print(f"The '{i}' character was found {character_count[i]} times")
        print("--- End Report ---")
        
        
        
        
    report("frankenstein.txt")
main()