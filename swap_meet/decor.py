from swap_meet.item import Item

class Decor(Item):
    
    def __init__(self, condition=None, age=None):
        self.category = "Decor"
        super().__init__(self.category, condition, age)


    def __str__(self):
        return "Something to decorate your space."