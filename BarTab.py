class Tab:
    menu = {
        "wine": 10,
        "beer": 5,
        "beef": 12,
        "soda": 2,
        "chicken": 5,
        "cake": 6
    }
    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total+=self.menu[item]

    def printBill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100)*self.total
        finalTotal = self.total+tax+service

        for x in self.items:
            print(f"{x:20} - ${self.menu[x]:.2f}")

        print(f"{'Total':20} - ${finalTotal:.2f}")

        
BarTab = Tab()

BarTab.add("beer")
BarTab.add("chicken")
BarTab.add("cake")
BarTab.add("beer")

BarTab.printBill(10, 15)
