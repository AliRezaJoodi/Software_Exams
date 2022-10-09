# GitHub.com/AliRezaJoodi

import unittest
import budget

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.food = budget.Category("Food") # Creat new object
        self.clothing = budget.Category("Clothing")   # Creat new object
        self.car = budget.Category("Car") # Creat new object

    def test_deposit(self):
        self.food.deposit(100, "Initial deposit")
        command = self.food.ledger[0]
        answer = {'amount': 100, 'description': 'Initial deposit'}
        self.assertEqual(command, answer)

    def test_deposit_without_description(self):
        self.food.deposit(50.50)
        command = self.food.ledger[0]
        answer = {"amount": 50.50, "description": ""}
        self.assertEqual(command, answer)

    def test_withdraw(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(22.50, "Supermarket")
        command = self.food.ledger[1]
        answer = {"amount": -22.50, "description": "Supermarket"}
        self.assertEqual(command, answer)

    def test_withdraw_without_description(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(50.50)
        command = self.food.ledger[1]
        answer = {"amount": -50.50, "description": ""}
        self.assertEqual(command, answer)

    def test_get_balance(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(50.50, "Supermarket")
        command = self.food.get_balance()
        answer = 49.5
        self.assertEqual(command, answer)

    def test_check_funds_false(self):
        self.food.deposit(100, "Initial deposit")
        command = self.food.check_funds(120)
        answer = False
        self.assertEqual(command, answer)

    def test_check_funds_true(self):
        self.food.deposit(100, "Initial deposit")
        command = self.food.check_funds(50)
        answer = True
        self.assertEqual(command, answer)

    def test_withdraw_no_funds(self):
        self.food.deposit(100, "Initial deposit")
        command = self.food.withdraw(120)
        answer = False
        self.assertEqual(command, answer)

    def test_transfer_successfully1(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(20, "Supermarket")
        self.food.transfer(20, self.clothing)
        command = self.food.ledger[2]
        answer = {"amount": -20, "description": "Transfer to Clothing"}
        self.assertEqual(command, answer)

    def test_transfer_successfully2(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(20, "Supermarket")
        self.food.transfer(20, self.clothing)
        command = self.clothing.ledger[0]
        answer = {"amount": 20, "description": "Transfer from Food"}
        self.assertEqual(command, answer)

    def test_transfer_unsuccessful(self):
        self.food.deposit(100, "Initial deposit")
        command = self.food.transfer(120, self.clothing)
        answer = False
        self.assertEqual(command, answer)

    def test_object_print(self):
        self.food.deposit(100, "Initial deposit")
        self.food.withdraw(50.50, "Supermarket")
        self.food.transfer(10, self.clothing)
        command = str(self.food)
        answer="\
*************Food*************\n\
Initial deposit         100.00\n\
Supermarket             -50.50\n\
Transfer to Clothing    -10.00\n\
Total: 39.5\n\
"     
        self.assertEqual(command, answer)

    def test_create_spend_chart(self):
        self.food.deposit(900, "Initial deposit")
        self.clothing.deposit(900, "Initial deposit")
        self.car.deposit(900, "Initial deposit")
        self.food.withdraw(105.55)
        self.clothing.withdraw(33.40)
        self.car.withdraw(10.99)
        command = budget.create_spend_chart([self.food, self.clothing, self.car])
        answer = "\
Percentage spent by category\n\
100|          \n\
 90|          \n\
 80|          \n\
 70| o        \n\
 60| o        \n\
 50| o        \n\
 40| o        \n\
 30| o        \n\
 20| o  o     \n\
 10| o  o     \n\
  0| o  o  o  \n\
    ----------\n\
     F  C  C  \n\
     o  l  a  \n\
     o  o  r  \n\
     d  t     \n\
        h     \n\
        i     \n\
        n     \n\
        g     "       
        self.assertEqual(command, answer)

if __name__ == "__main__":
    unittest.main()
