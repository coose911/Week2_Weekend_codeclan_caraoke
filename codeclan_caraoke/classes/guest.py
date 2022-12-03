class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount
        return self.wallet
    
    def check_wallet_amount(self):
        return self.wallet

    