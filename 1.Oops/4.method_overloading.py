# Method Overloading / Default Parameters

# Create a Calculator class that can add two or three numbers using default parameters.


class Calculater:
    def __init__(self, *args):
        self.operands = args

    def add(self):
        s = 0
        for num in self.operands:
            s += num
        return s


cal = Calculater(1, 2)
print(cal.add())

cal = Calculater(1, 2, 4)
print(cal.add())
