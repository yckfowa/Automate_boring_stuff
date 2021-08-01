def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(str(item), 0)
        inventory[item] += 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory(inv):
    print("===========================")
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(str(v).rjust(3) + ' ' + k.rjust(20).title())
        item_total += v
    print("Total number of items: " + str(item_total))
    print("===========================")


add_to_inventory(inv, dragonLoot)

display_inventory(inv)
