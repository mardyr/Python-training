class WashingMachine():
    # create static variable
    saleCounter = 0

    # create constructor
    def __init__(self):
        WashingMachine.saleCounter +=1

    #create static method
    @staticmethod
    def WashingMachineCounter():
        print("Sold",WashingMachine.saleCounter,"washing machines")

    # create destructor
    def __del__(self):
        WashingMachine.saleCounter -=1
        del self



WashingMachine.WashingMachineCounter()

whirlpool = WashingMachine()

print(WashingMachine.saleCounter)

amica = WashingMachine()

print(WashingMachine.saleCounter)

WashingMachine.WashingMachineCounter()

del amica

WashingMachine.WashingMachineCounter()