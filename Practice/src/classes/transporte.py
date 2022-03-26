class Transporte:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def display(self):
        print("name:" + self.name+ "price:"+ self.price)

