# imports:
import json
import os.path

# Inventory Class:
class Inventory:
    pets ={}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0;
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        
        self.pets[key] = q
        print(f'Added {qty} {key} : total = {self.pets[key]}')
    
    def remove(self, key, qty):
        q = 0;
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        
        if q < 0:
            q = 0

        self.pets[key] = q
        print(f'Removed {qty} {key} : total = {self.pets[key]}')       

    def display(self):
        for key, value in self.pets.items():
            print(f'{key} = {value}')

    def save(self):
        print(f'Saving inventory...')

        with open('inventory.txt', 'w') as f:
            json.dump(self.pets,f)

        print(f'Saved..')

    def load(self):
        print(f'Loading inventory...')

        if not os.path.exists('inventory.txt'):
            print(f'Skipping, nothing to load !')
            return

        with open('inventory.txt', 'r') as f:
            self.pets = json.load(f)

        print(f'Loaded..')


def main():
    inv = Inventory()

    while True:
        action = input('Action: add, remove, save, list, save, exit: ')

        if action == 'exit':
            break

        if action == 'add' or action == 'remove':
            key = input('Enter the animal : ')
            qty = int(input('Enter the quantity : ')) 

            if action == 'add':
                inv.add(key, qty)
            
            if action == 'remove':
                inv.remove(key, qty)
        
        if action == 'list':
            inv.display()

        if action == 'save':
            inv.save()

    inv.save()    


if __name__ == '__main__':
    main()
    