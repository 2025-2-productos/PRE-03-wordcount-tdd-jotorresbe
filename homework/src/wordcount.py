# Ejemplo para casos de uso

# python -m homework data/input data/output


import argparse

from homework.src._internals.read_all_lines import read_all_lines


def parse_args():

    parser = argparse.ArgumentParser(description="Count Word in files.")

    parser.add_argument(
        "input", type=str, help="Path to the input folder containing files to process"
    )

    parser.add_argument(
        "output", type=str, help="Path to the output folder containing files to process"
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output


# def parse_args(argv=None):
#     if argv is None:
#         argv = sys.argv

#     if len(argv) < 3:
#         print("Uso: python -m homework <input_folder> <output_folder>")
#         sys.exit(1)


#     input_folder = argv[1]
#     output_folder = argv[2]
#     return input_folder, output_folder
def preprocess_lines(lines):
    preprocessed = [line.strip().lower() for line in lines]
    return preprocessed

def split_lines_into_words(preprocessed_lines):
    words = []
    for line in lines:
        words.extend(line.split())
    return words

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def write_word_count(output_folder, word_count):
    output_path = f"{output_folder}/word_count.txt"
    with open(output_path, "w", encoding="utf-8") as file:
        for word, count in sorted(word_count.items()):
            file.write(f"{word}: {count}\n")

def main():
    # args = parse_args()

    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_lines_into_words(preprocessed_lines)
    word_count = count_words(words)
    write_word_count(output_folder, word_count)