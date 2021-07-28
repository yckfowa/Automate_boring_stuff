<<<<<<< HEAD
def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    elif number % 2 == 1:
        print(3*number+1)
        return 3*number+1


try:
    n = int(input("Enter a number: "))
    while n != 1 and n > 0:
        n = collatz(n)
except ValueError:
    print("Please enter a (positive) integer instead of string.. program exits...")

=======

def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    elif number % 2 == 1:
        print(3*number+1)
        return 3*number+1


try:
    n = int(input("Enter a number: "))
    while n != 1 and n > 0:
        n = collatz(n)
except ValueError:
    print("Please enter a (positive) integer instead of string.. program exits...")

>>>>>>> b6635c9564d6f61fc50c0b2f94c066a5e5a58140
