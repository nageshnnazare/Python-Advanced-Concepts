# Multiple Inheritance

# inherit from multiple classes


class Vehicle:
    speed = 0
    
    def drive(self, speed):
        self.speed = speed
        print(f'Driving')

    def stop(self):
        self.speed = 0
        print(f'Stopped!')

    def display(self):
        print(f'Driving at {self.speed} speed')


class Freezer:
    temp = 0

    def freeze(self, temp):
        self.temp = 0;
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


class FreezerTruck(Freezer, Vehicle): # Method Resolution Order (MRO)
    def display(self):
        print(f'Is a Freezer: {issubclass(FreezerTruck, Freezer)}')
        print(f'Is a Vehicle: {issubclass(FreezerTruck, Vehicle)}')

        # super(Freezer,self).display()
        # super(Vehicle,self).display()

        Freezer.display(self)
        Vehicle.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-20)
print('*'*20)
t.display()