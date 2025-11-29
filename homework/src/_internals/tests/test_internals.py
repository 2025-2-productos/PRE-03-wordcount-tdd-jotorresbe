import os
import shutil
import sys

from ..read_all_lines import read_all_lines
from ...wordcount import parse_args, preprocess_lines, split_lines_into_words, count_words, write_word_count


# python -m homework data/input data/output


def test_parse_args():
    """Llamada en el prompt:
    $ python -m homework data/input data/output
    """

    test_args = ["homework", "data/input", "data/output"]
    sys.argv = test_args

    input_folder, output_folder = parse_args()

    assert input_folder == test_args[1]
    assert output_folder == test_args[2]


def test_read_all_lines():
    input_folder = "data/input"
    lines = read_all_lines(input_folder)
    assert len(lines) > 0
    assert any(
        "Analytics refers to the systematic computational analysis of data" in line
        for line in lines
    )

def test_preprocess_lines():
    lines = [" Hello, World!  ", "Python is GREAT."]
    preprocessed = preprocess_lines(lines)
    assert preprocessed == ["hello, world!", "python is great."]


def test_split_lines_into_words():
    preprocessed_lines = ["hello, world", "python is great."]
    words = split_lines_into_words(preprocessed_lines)
    assert words == ["hello", "world", "python", "is", "great"]

def test_count_words():
    words = ["hello", "world", "hello", "python"]
    word_count = count_words(words)
    assert word_count == {"hello": 2, "world": 1, "python": 1}

def test_write_word_count():
    output_folder = "data/output"
    word_count = {"hello": 2, "world": 1, "python": 1}

    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    write_word_count(output_folder, word_count)

    output_folder = os.path.join(output_folder, "word_count.tsv")
    assert os.path.exists(output_folder), "Output file was not created"

    with open(output_folder, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    assert lines == ["hello\t2\n", "python\t1\n", "world\t1\n"]
    
    #Clean up
    shutil.rmtree(output_folder)
"""
def test_parse_args(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["script.py", "data/input", "data/output"])
    input_folder, output_folder = parse_args()
    assert input_folder == "data/input"
    assert output_folder == "data/output"
"""


# def test_parse_args():
#     try:
#         subprocess.run(
#             ["python", "-m", "homework", "data/input", "data/output"],
#             check=True,
#         )
#     except subprocess.CalledProcessError as e:
#         raise Exception(f"Error running the homework script: {e}")
#     input_folder, output_folder = parse_args(["script.py", "data/input", "data/output"])
#     assert input_folder == "data/input"
#     assert output_folder == "data/output"
