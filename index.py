"""Menu program for the phoney package: format phone numbers and explore the phone_numbers.csv file."""
from phoney.phoney import count_by_areacode, format_number, is_valid_nanp, load_numbers

DATA_FILE = "phone_numbers.csv"
MENU = """
F - Format a phone number
V - Count valid phone numbers
A - Look up an area code
T - Top five area codes
X - Exit"""


class NotWritten(Exception):
    """A function the student has not written yet."""


def call(function, *args):
    """Call function(*args), turning NotImplementedError into NotWritten."""
    try:
        return function(*args)
    except NotImplementedError:
        raise NotWritten(function.__name__) from None


def format_option(numbers):
    entry = input("Phone number: ")
    result = call(format_number, entry)
    print(result if result is not None else "That isn't a 10-digit number.")


def valid_option(numbers):
    count = sum(1 for number in numbers if call(is_valid_nanp, number))
    print(f"{count:,} of the {len(numbers):,} phone numbers are valid.")


def area_code_option(numbers):
    code = input("Area code (3 digits): ").strip()
    if len(code) != 3 or not code.isdigit():
        print("An area code is exactly 3 digits.")
        return
    count = call(count_by_areacode, numbers).get(code, 0)
    print(f"{count:,} phone numbers have area code {code}.")


def top_option(numbers):
    counts = call(count_by_areacode, numbers)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    print("Top five area codes:")
    for place, (code, count) in enumerate(ranked[:5], start=1):
        print(f"  {place}. {code}  {count:,} phone numbers")


OPTIONS = {"F": format_option, "V": valid_option, "A": area_code_option, "T": top_option}


def main():
    numbers = load_numbers(DATA_FILE)
    print(f"There are {len(numbers):,} phone numbers in the file.")
    while True:
        print(MENU)
        try:
            choice = input("Choose an option: ").strip().upper()
        except EOFError:
            break
        if choice == "X":
            print("Good bye!")
            break
        if choice not in OPTIONS:
            print("Please choose F, V, A, T or X.")
            continue
        try:
            OPTIONS[choice](numbers)
        except NotWritten as unwritten:
            print(f"{unwritten} isn't written yet.")


if __name__ == "__main__":
    main()
