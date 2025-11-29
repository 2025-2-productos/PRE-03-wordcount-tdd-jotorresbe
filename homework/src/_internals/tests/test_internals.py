import sys

from ..read_all_lines import read_all_lines
from ...wordcount import parse_args

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
