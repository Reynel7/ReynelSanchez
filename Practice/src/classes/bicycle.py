from ReynelSanchez.Practice.src.classes.land import Land
class Bicycle(Land):
    def __init__(self, name, price, hasMotor, excerciseBike):
        super().__init__(name, price, hasMotor)
        self.excerciseBike = excerciseBike

    def display(self):
        print("name:" + self.name+ "price:"+ self.price+"hasMotor:"+ self.hasMotor + "excerciseBike: "+ self.excerciseBike)