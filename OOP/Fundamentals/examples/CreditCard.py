class CreditCard:

    def __init__(self, customer, bank, account, limit):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def make_payment(self, amount):

        if self._balance - amount < 0:
            raise ValueError('not enough balance')

        self._balance -= amount

    def charge(self, price):

        if self._balance + price > self._limit:
            return False

        else:
            self._balance += price
            return True


class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, account, limit, apr):

        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):

        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
