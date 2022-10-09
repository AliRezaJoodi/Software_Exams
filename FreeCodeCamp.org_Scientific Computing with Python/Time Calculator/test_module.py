# https://github.com/AliRezaJoodi
import unittest
import time_calculator

class TestFunction(unittest.TestCase):

    def test_8(self):
        command = time_calculator.add_time("5:01 AM", "0:00")    #no change
        answer = "5:01 AM"
        self.assertEqual(command, answer)

    def test_1(self):
        command = time_calculator.add_time("2:30 PM", "2:12")    #same period
        answer = "4:42 PM"
        self.assertEqual(command, answer)  

    def test_3(self):
        command = time_calculator.add_time("10:10 PM", "5:30")    #next day
        answer = "3:40 AM (next day)"
        self.assertEqual(command, answer)

    def test_5(self):
        command = time_calculator.add_time("1:59 AM", "24:00")   #24
        answer = "1:59 AM (next day)"
        self.assertEqual(command, answer)

    def test_6(self):
        command = time_calculator.add_time("11:59 PM", "24:03")  #2days later
        answer = "12:02 AM (2 days later)"
        self.assertEqual(command, answer)

    def test_7(self):
        command = time_calculator.add_time("8:15 PM", "355:00")  #high duration
        answer = "3:15 PM (15 days later)"
        self.assertEqual(command, answer)

    def test_9(self):
        command = time_calculator.add_time("4:30 PM", "2:02", "saturDay")  #same period with 1day
        answer = "6:32 PM, Saturday"
        self.assertEqual(command, answer)

    def test_10(self):
        command = time_calculator.add_time("2:59 AM", "24:00", "Friday")   #24 with day
        answer = "2:59 AM, Saturday (next day)"
        self.assertEqual(command, answer)

    def test_11(self):
        command = time_calculator.add_time("11:59 PM", "24:05", "Wednesday") #2days later with_day
        answer = "12:04 AM, Friday (2 days later)"
        self.assertEqual(command, answer)

    def test_12(self):
        command = time_calculator.add_time("8:10 PM", "350:02", "tuesday")   #high duration with 1day
        answer = "10:12 AM, Wednesday (15 days later)"
        self.assertEqual(command, answer)

if __name__ == "__main__":
    unittest.main()