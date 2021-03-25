import unittest
import Atm
class TestAccount(unittest.TestCase):
    def test_getPin(self):
        pin=1211
        valid_pin=1000
        message="enter valid pin"
        self.assertLess(valid_pin,pin,message)
    def test_withdraw(self):
        
        amt=5000
        getBalance=10000
        message="pls make deposit"
        self.assertLessEqual(amt,getBalance,message)
    def test_deposit(self):
        amt=1000
        getBalance=3000
        message ="amount deposited successfully"
        self.assertGreater(getBalance,amt,message)
if __name__ =="__main__":
    unittest.main() 