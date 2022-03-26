from ReynelSanchez.Practice.src.classes.transporte import Transporte
from ReynelSanchez.Practice.src.classes.land import Land
from ReynelSanchez.Practice.src.classes.car import Car
from ReynelSanchez.Practice.src.classes.bicycle import Bicycle
if __name__ == "__main__":
    print("hola")

    transporte1 = Transporte("tren", "15")
    transporte2 = Land("auto", "15", "True")
    transporte3 = Car("liz", "25", "False", "True")
    transporte4 = Bicycle("fabiola", "30", "True", "False")

    transporteList = [transporte1, transporte2, transporte3, transporte4]

    for trans in transporteList:
        trans.display()