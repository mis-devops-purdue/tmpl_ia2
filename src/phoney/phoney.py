import csv


def load_numbers(filename):
    """Read the phone numbers from a CSV file.

    Parameter:
        filename: path to a CSV file whose first row is a header and whose
            first column holds one phone number per row.

    Returns:
        A list of the phone numbers as strings, exactly as they appear in the
        file (punctuation and all).

    Example:
        load_numbers("phone_numbers.csv")  ->  ["(765)494-1234", "3175551234", ...]
    """
    numbers = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        # The first row is the column title, not a phone number, so skip it.
        next(reader)
        for row in reader:
            # Keep the text untouched; cleaning it up is the job of the other functions.
            numbers.append(row[0])
    return numbers


def format_number(number):
    # TODO: Ignore every character that isn't a digit. If exactly 10 digits remain, return them as "(765) 494-1234". Otherwise return None.
    raise NotImplementedError


def is_valid_nanp(number):
    # TODO: Ignore every character that isn't a digit. Return True only if exactly 10 digits remain, the area code and the exchange each start with 2-9, and the area code is not N11 (middle and last digits both 1). Otherwise False.
    raise NotImplementedError


def count_by_areacode(numbers):
    # TODO: For every entry with exactly 10 digits (ignoring non-digits), count its area code. Return a dict like {"765": 212, "317": 140}. Skip entries with any other number of digits.
    raise NotImplementedError
