# https://github.com/AliRezaJoodi
import unittest
from arithmetic_arranger import arithmetic_arranger

class UnitTests(unittest.TestCase):

    def test_too_many_problems(self):
        command = arithmetic_arranger(["10 + 201", "1 - 4", "52 + 11", "25 + 14", "745 + 10", "61 + 10"])
        answer = "Error: Too many problems."
        self.assertEqual(command, answer)

    def test_incorrect_operator(self):
        command = arithmetic_arranger(["1 * 252", "1202 - 1", "42 + 12", "20 + 51"])
        answer = "Error: Operator must be '+' or '-'."
        self.assertEqual(command, answer)

    def test_too_many_digits(self):
        command = arithmetic_arranger(["24 + 25", "20 - 2", "78502 + 11", "1223 + 149"])
        answer = "Error: Numbers cannot be more than four digits."
        self.assertEqual(command, answer)

    def test_only_digits(self):
        command = arithmetic_arranger(["10A + 85", "2630 - 4", "21 + 85", "209 + 150"])
        answer = "Error: Numbers must only contain digits."
        self.assertEqual(command, answer)

    def test_arrangement(self):
        command = arithmetic_arranger(["5 + 523", "2520 - 4", "45 + 13", "123 + 63"])
        answer = "\
    5      2520      45      123\n\
+ 523    -    4    + 13    +  63\n\
-----    ------    ----    -----"
        self.assertEqual(command, answer)

    def test_solutions(self):
        command = arithmetic_arranger(["23 - 520", "2 - 3602", "35 + 40", "221 + 51"], True)
        answer = "\
   23         2      35      221\n\
- 520    - 3602    + 40    +  51\n\
-----    ------    ----    -----\n\
 -497     -3600      75      272"
        self.assertEqual(command, answer)

if __name__ == "__main__":
    unittest.main()
