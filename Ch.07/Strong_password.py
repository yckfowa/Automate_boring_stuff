import re


def strong_password(pw: str):

    length_regex = re.compile(r'\w{8,}')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')

    if length_regex.search(pw) is None:
        print(f"The password needs to contain at least 8 characters")
        return False
    if upper_regex.search(pw) is None:
        print(f"The password needs to contain at least one uppercase")
        return False
    if lower_regex.search(pw) is None:
        print(f"The password needs to contain at one lowercase character")
        return False
    if digit_regex.search(pw) is None:
        print(f"The password needs to have at least one digit")
        return False
    print(f"Your password is strong")
    return True


strong_password('abcdfGaa1')