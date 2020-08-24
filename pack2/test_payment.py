import unittest
class test_payment(unittest.TestCase):
    def test_paymentRupess(self):
        print("Payment in rupees")
    def test_paymentDollors(self):
        print("Payment in dollors")
    def test_paymentPound(self):
        print("Payment in pound")
if __name__=="__main__":
    unittest.main()