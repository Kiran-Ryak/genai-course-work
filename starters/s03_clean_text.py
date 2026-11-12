"""clean_text.py: clean and mask a customer message before it goes to a model (Session 3 lab)

Fill in each function body. Do not change the function names: the tests call them.
Check your work from the adv-genai folder:  uv run pytest tests/test_s03.py
"""


def normalise_spaces(text):
    """Remove spaces at both ends and squeeze repeated spaces into one."""
    pass   # YOU: replace this line


def mask_pan(word):
    """A PAN looks like ABCDE1234F: 5 letters, 4 digits, 1 letter. Keep only the last 4 characters."""
    pass   # YOU: replace this line


def mask_phone(word):
    """A phone number is exactly 10 digits. Keep only the last 4 digits."""
    pass   # YOU: replace this line


def unique_lines(lines):
    """Drop repeated lines, keeping the first of each, in the original order."""
    pass   # YOU: replace this line


def word_counts(text):
    """Count how many times each word appears, ignoring upper and lower case."""
    pass   # YOU: replace this line


def mask_message(text):
    """Clean the spaces, then mask every PAN and phone number in the message."""
    pass   # YOU: replace this line


MESSAGES = [
    "  Hello,   I applied for a home loan   last week.  ",
    "My PAN is ABCDE1234F and my phone is 9876543210",
    "My PAN is ABCDE1234F and my phone is 9876543210",
    "Please   call me back about the loan  status",
]

if __name__ == "__main__":
    for line in unique_lines(MESSAGES):
        print(mask_message(line))
    print(word_counts("Loan status please. Home loan status"))
