from ReynelSanchez.Practice.src.classes.transporte import Transporte
class Land(Transporte):
    def __init__(self, name, price, hasMotor):
        super().__init__(name, price)
        self.hasMotor = hasMotor

    def display(self):
        print("name:" + self.name+ "price:"+ self.price+"hasMotor:"+ self.hasMotor)

