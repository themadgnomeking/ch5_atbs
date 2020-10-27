def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " "+ k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # your code goes here
    #receive the inventory and added items
    #compare the added items with inventory key
    #if the added item and key match add one to the value
    #create a new dictionary and output to display_inventory
    new_dict = {}
    item_count = 1

    for k, v in inventory.items():
        if v == 1:
            new_dict[k] = 1
        for item in addedItems:
            if item_count > len(addedItems):
                return new_dict
            elif item == k:
                v += 1
                new_dict[item] = v
                item_count += 1
            elif item != k:
                new_dict[item] = 1
                item_count += 1

#bring in the first key of the dictionary
#iterate through the list
#if a list item matches the key add to the value by 1


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(inv)
display_inventory(inv)