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
def main():
    # args = parse_args()

    input_folder, output_folder = parse_args()
    lines = read_all_lines(input_folder)
