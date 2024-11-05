"""
    this file is where the class CurrencyConversion is written. 
    The class creates an object in order to process the conversion between two currency
"""


class CurrencyConversion:
    def __init__(self, money_amount, money_rate):
        self.m_amount = money_amount
        self.m_rate = money_rate

    def get_conversion(self):
        """
        This meethod returns the converted currency amount
        """
        return self.m_amount * self.m_rate
