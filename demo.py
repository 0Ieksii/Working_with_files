import text_tools as tt
import os

def run_demo():
    print("=== Text Tools Project Demonstration ===")

    # 1 Write numbers from 1 to N into a file
    print("\n[1] Testing write_numbers(n):")
    n = 10
    tt.write_numbers(n)
    print(f"    - Created 'numbers.txt' with values 1 to {n}.")

    # 2 Read entire file content
    print("\n[2] Testing read_file(filename):")
    print(tt.read_file("txt.files/numbers.txt"))

    # 3 Count lines and characters in a file
    print("[3] Testing count_lines_chars(filename):")
    lines, chars = tt.count_lines_chars("txt.files/numbers.txt")
    print(f"    - 'numbers.txt' has {lines} lines and {chars} characters.")

    # 4 Read specific lines
    print("\n[4] Testing read_line(filename, line_number):")
    line_5 = tt.read_line("txt.files/input_file.txt", 5)
    print(f"    - The 5th line of 'input_file.txt' is: '{line_5}'")

    # 5 Merge multiple text files into one
    print("\n[5] Testing merge_files(output, *inputs):")
    tt.merge_files("txt.files/merged_facts.txt", "txt.files/1.txt", "txt.files/2.txt", "txt.files/3.txt")
    print("    - Merged 1.txt, 2.txt, and 3.txt into 'merged_facts.txt'.")

    # 6 Search for words inside a file
    print("\n[6] Testing find_word(filename, word):")
    word_to_find = "crocodile"
    matches = tt.find_word("txt.files/merged_facts.txt", word_to_find)
    if matches:
        print(f"    - Found '{word_to_find}' at these (line, position) coordinates:")
        for match in matches:
            print(f"      * {match}")
    
    # Missing word
    missing_word = "Python"
    if tt.find_word("txt.files/merged_facts.txt", missing_word) is None:
        print(f"    - Correctly identified that '{missing_word}' is not in the file.")

    # 7 Copy file contetn to another file (+reversing)
    print("\n[7] Testing copy_file and reverse_file:")
    tt.copy_file("txt.files/numbers.txt", "txt.files/numbers_reversed.txt")
    tt.reverse_file("txt.files/numbers_reversed.txt")
    print("    - Copied 'numbers.txt' to 'numbers_reversed.txt' and reversed the line order.")
    
    # 3 first lines of reversed file
    print("    - Content of 'numbers_reversed.txt' (first 3 lines):")
    with open("txt.files/numbers_reversed.txt", "r") as f:
        for _ in range(3):
            print(f"      {f.readline().strip()}")

    print("\n=== Demonstration Completed Successfully ===")


try:
    run_demo()
except FileNotFoundError as e:
    print(f"Error: Missing test file - {e}")