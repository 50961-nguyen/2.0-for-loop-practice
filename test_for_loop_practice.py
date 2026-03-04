import re
import sys
import builtins
from io import StringIO

filename = "for_loop_practice"


def run_program(inputs):
    """Helper: runs the student module with given inputs, returns printed output."""
    sys.modules.pop(filename, None)
    original_input = builtins.input
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    builtins.input = lambda _: inputs.pop(0)
    try:
        __import__(filename)
        return sys.stdout.getvalue()
    finally:
        builtins.input = original_input
        sys.stdout = original_stdout
        sys.modules.pop(filename, None)


def test_header_comments():
    """Students should have a docstring with author, date, and description"""
    with open(f"{filename}.py", encoding="utf-8") as f:
        kids_code = f.read()

    docstring_match = re.search(r'^\s*"""(.*?)"""', kids_code, re.DOTALL)
    assert docstring_match is not None, "You must include a header docstring using triple quotes (\"\"\")"

    docstring = docstring_match.group(1)

    author_match = re.search(r'author\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert author_match is not None, "Your header must include an 'author:' field"
    assert author_match.group(1).strip() != "", "Your 'author:' field must not be empty"

    date_match = re.search(r'date\s*:\s*(.+)', docstring, re.IGNORECASE)
    assert date_match is not None, "Your header must include a 'date:' field"
    assert date_match.group(1).strip() != "", "Your 'date:' field must not be empty"

    lines = [line.strip() for line in docstring.strip().splitlines()]
    description_lines = [
        line for line in lines
        if line
        and not re.match(r'author\s*:', line, re.IGNORECASE)
        and not re.match(r'date\s*:', line, re.IGNORECASE)
    ]
    assert len(description_lines) >= 1, "Your header must include a short description of the program"


def test_ipo_comments():
    """Students should have # Input, # Processing, and # Output comments"""
    with open(f"{filename}.py", encoding="utf-8") as f:
        kids_code = f.read()

    assert re.search(r'#.*input', kids_code, re.IGNORECASE), "You must include an '# Input' comment section"
    assert re.search(r'#.*processing|#.*output', kids_code, re.IGNORECASE), "You must include a '# Processing' and/or '# Output' comment section"


def test_all_wins():
    """10 wins should report 10 wins, 0 losses, 0 invalid"""
    out = run_program(["W"] * 10)
    assert "10" in out and "won" in out.lower(), \
        "Expected 10 wins in output"
    assert "0" in out and ("lost" in out.lower()), \
        "Expected 0 losses in output"


def test_all_losses():
    """10 losses should report 0 wins, 10 losses, 0 invalid"""
    out = run_program(["L"] * 10)
    assert "10" in out and ("lost" in out.lower()), \
        "Expected 10 losses in output"
    assert "0" in out and "won" in out.lower(), \
        "Expected 0 wins in output"


def test_mixed_results():
    """Mixed inputs should correctly count wins, losses, and invalid"""
    out = run_program(["W", "L", "WINSS", "W", "W", "W", "L", "L", "W", "W"])
    assert "6" in out and "won" in out.lower(), \
        "Expected 6 wins in output"
    assert "3" in out and ("lost" in out.lower()), \
        "Expected 3 losses in output"
    assert "1" in out and "invalid" in out.lower(), \
        "Expected 1 invalid input reported in output"
    assert "invalid" in out.lower(), \
        "Expected 'Invalid input' to be printed when bad input is entered"
