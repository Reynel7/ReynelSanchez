from ReynelSanchez.Practice.src.classes.land import Land
class Car(Land):
    def __init__(self, name, price, hasMotor, usuGas):
        super().__init__(name, price, hasMotor)
        self.useGas = usuGas

    def display(self):
        print("name:" + self.name+ "price:"+ self.price+"hasMotor:"+ self.hasMotor + "useGas: "+ self.useGas)