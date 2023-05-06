class Fruit:
    taste="sweet"
    def __init__(self,colour,price,name):
        self.colour=colour
        self.price=price
        self.name=name
    def buy_fruits(self):
        
        return f"I bought 4 {self.taste} {self.colour} {self.name} at {(self.price *4)ksh}"

    def make_juice(self):
        return f"i made {self.taste} {self.colour} juice from {self.name} "

    
