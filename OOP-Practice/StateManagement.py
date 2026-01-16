class OnlinePayment:
    def __init__(self):
        self.balance = 0

    def insert_credit(self, amount):
        self.balance += amount

    def buy(self, price):
        if self.balance >= price:
            self.balance -= price

cart1 = OnlinePayment()
cart1.insert_credit(200)
cart1.buy(150)

print(cart1.balance)
