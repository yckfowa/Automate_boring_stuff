spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = []

def list_to_string(arr: list) -> str:

    if arr:
        arr[-1] = 'and ' + arr[-1]
        return ", ".join(arr)
    else:
        return f"list is empty"


print(list_to_string(spam))

