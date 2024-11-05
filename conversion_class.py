"""
    this file is where the class "Currency Conversion" is written
"""


class CurrencyConversion:
    def __init__(self, money_amount, money_rate):
        self.m_amount = money_amount
        self.m_rate = money_rate

    def get_conversion(self):
        return self.m_amount * self.m_rate
