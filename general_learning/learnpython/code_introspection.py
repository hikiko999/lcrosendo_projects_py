# Use the help function to see what each function does.
# Delete this when you are done.
# help(dir)
# help(hasattr)
# help(id)

# Define the Vehicle class.
class Vehicle:
    name = "Lambo"
    kind = "car"
    color = "Red"
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# help(Vehicle)
print(dir(Vehicle))
print(hasattr(Vehicle,"kind"))
print(id(Vehicle.description))
car = Vehicle()
print(car.description())

# Print a list of all attributes of the Vehicle class.
# Your code goes here