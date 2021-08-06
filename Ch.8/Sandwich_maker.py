import pyinputplus as pyip

price_list = {'breads': {'wheat': 5, 'white': 3, 'sourdough': 6},
              'main': {'chicken': 7, 'turkey': 10, 'ham': 5, "tofu": 3},
              'cheeses': {'cheddar': 3, 'Swiss': 4, 'mozzarella': 3}}


def main():
    total = 0
    print("Welcome to SubWaiyi, please make your order ")
    bread_choice = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='What types of bread do you prefer?' + "\n")
    total += price_list['breads'][bread_choice]

    main_choice = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choices of main?" + '\n')
    total += price_list['main'][main_choice]

    cheese_choice = pyip.inputYesNo("Would you like any cheese?:")
    if cheese_choice == 'yes':
        cheese_select = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
        total += price_list['cheeses'][cheese_select]
        pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato (free of charge):")

    elif cheese_choice == "no":
        pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato (free of charge):")

    response = pyip.inputInt("How many sandwiches do you want: ", min=1)
    print(f"The total price would be ${response * total} dollars")
    exit()


if __name__ == "__main__":
    main()
