from swap_meet.item import Item

class Clothing(Item):
    
    def __init__(self, condition=None, age=None):
        self.category = "Clothing"
        super().__init__(self.category, condition, age)


    def __str__(self):
        return "The finest clothing you could wear."