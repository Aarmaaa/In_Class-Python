class Table(object):
    def __init__(self, seats, color, type, age):
        self.seats = seats
        self.color = color
        self.type = type
        self.age = age

    def clean(self):
        print("the table is clean")

    def set_food(self):
        print("the food have been served")

    def full(self):
        print("the table is full")

table1 = Table(4,"brown", "wooden", "old")    
table2 = Table(6, "gray", "glass", "new")

table1.clean()
table2.full()
table1.set_food()