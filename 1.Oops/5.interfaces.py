from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class Gpay(Payment):
    def pay(self):
        print("paying with Gpay.. ")


class Phonepay(Payment):
    def credit(self):
        print("credit amount is")

    def pay(self):
        print("paying with phonepay")


gpay = Gpay()
ppay = Phonepay()

# for chr in [gpay, ppay]:
#     chr.pay()
