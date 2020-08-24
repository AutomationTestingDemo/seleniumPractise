import unittest
from pack1.TestLogin import Test_Login
from pack1.testSignup import TestSignup
from pack2.test_payment import test_payment
from pack2.TC_paymentReturns import Test_paymentReturns

#getting all the tests from all the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_Login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSignup)
tc3 = unittest.TestLoader().loadTestsFromTestCase(test_payment)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Test_paymentReturns)

#creating test suites
sanitytest = unittest.TestSuite([tc1,tc2])
functionaltest=unittest.TestSuite([tc3,tc4])
masterSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])
# unittest.TextTestRunner().run(sanitytest)
# unittest.TextTestRunner().run(functionaltest)
unittest.TextTestRunner(verbosity=2).run(masterSuite)
