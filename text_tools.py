def write_numbers(n):
    with open("txt.files/numbers.txt", "w", encoding="utf-8") as output:
        for i in range(1, n + 1):
            print(i, file=output)
        # output.writelines([str(i) + "\n" for i in range(1, n + 1)])


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as reading:
        return reading.read()


def count_lines_chars(filename):
    with open(filename, "r", encoding="utf-8") as reading:
        text = reading.read()
        lines = len(text.splitlines())
        chars = len(text)
        return (lines, chars)


def read_line(filename, line_number):
    with open(filename, "r", encoding="utf-8") as reading:
        for number, line in enumerate(reading.readlines(), 1):
            if number == line_number:
                return line.rstrip()
        return None
    

def merge_files(output_filename, *input_files):
    with open(output_filename, "w", encoding="utf-8") as output:
        for file in input_files:
            output.write(f"**** {file} ****\n")
            with open(file, "r", encoding="utf-8") as reading:
                output.write(reading.read()+"\n")


def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as reading, open(destination, "w", encoding="utf-8") as output:
        output.write(reading.read())


def reverse_file(filename):
    with open(filename, "r", encoding="utf-8") as reading:
        lines = reading.readlines()[::-1]
    with open(filename, "w", encoding="utf-8") as writing:
        writing.writelines(lines)


def find_word(filename, word):
    with open(filename, "r", encoding="utf-8") as reading:
        match_list = []
        word_lower = word.lower()
        for number, line in enumerate(reading.readlines(), 1):
            line_lower = line.lower()
            start = 0
            while True:
                pos = line_lower.find(word_lower, start)
                if pos == -1:
                    break
                match_list.append((number, pos))
                start = pos + 1
    if match_list:
        return match_list
    return None


# write_numbers(10)
# read_file("numbers.txt")
# print(read_line("input_file.txt", 5))
# print(count_lines_chars("numbers.txt"))
# merge_files("result.txt", "1.txt", "2.txt", "3.txt")
# copy_file("result.txt", "result_copy.txt")
# reverse_file("result_copy.txt")
# print(find_word("result.txt", 'crocodile'))