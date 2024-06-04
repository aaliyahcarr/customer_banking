
""" Create a Account class with methods"""
class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_rate, months):
        self.balance = balance
        self.interest_rate = interest_rate
        self.months = months
    

    # This method sets the balance of the account.
    def set_balance(self, new_balance):
        """Sets the balance for the for the account"""
        self.balance = new_balance
        return self.balance

    # The method sets the interest gained for the account.
    def set_interest(self, new_interest_rate):
        """Sets the interest gained for the the account"""
        self.interest = new_interest_rate 
