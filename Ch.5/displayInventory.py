
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(stuff):
    print("===========================")
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v).rjust(3) + ' ' + k.rjust(20).title())
        item_total += v
    print("Total number of items: " + str(item_total))
    print("===========================")


display_inventory(inventory)
