from unicodedata import name
import unittest
from employ import Employee

class TestEmployee(unittest.TestCase):

    # either you can create employee instance in every method or can use setup method 
    # to create instance of the class

    def setUp(self):
        self.emp_1 = Employee('Corey','Schafer', 50000)
        self.emp_2 = Employee('sue','Smith',33323)
        

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'sue.Smith@email.com')

        self.emp_2.first = 'Hon'
        self.emp_1.first = 'Jan'

        self.assertEqual(self.emp_1.email,'Jan.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Hon.Smith@email.com')


    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'sue Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay,52500 )
        self.assertEqual(self.emp_2.pay, 34989.15)



if __name__ == '__main__':
    unittest.main()
    