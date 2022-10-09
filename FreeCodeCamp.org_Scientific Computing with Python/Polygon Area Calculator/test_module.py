# GitHub.com/AliRezaJoodi

import unittest
import shape_calculator

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.rect = shape_calculator.Rectangle(3, 6)
        self.sq = shape_calculator.Square(5)

    # Square class to be a subclass of the Rectangle class.
    def test_subclass(self):
        command = issubclass(shape_calculator.Square, shape_calculator.Rectangle)
        answer = True
        self.assertEqual(command, answer)

    # Square class to be a distinct class from the Rectangle class.
    def test_distinct_classes(self):
        command = shape_calculator.Square is not shape_calculator.Rectangle
        answer = True
        self.assertEqual(command, answer)

    # square object to be an instance of the Square class and the Rectangle class.
    def test_square_is_square_and_rectangle(self):
        command = isinstance(self.sq, shape_calculator.Square) and isinstance(self.sq, shape_calculator.Rectangle)
        answer = True
        self.assertEqual(command, answer)

    def test_string_rectangle(self):
        command = str(self.rect)
        answer = "Rectangle(width=3, height=6)"
        self.assertEqual(command, answer)

    def test_string_square(self):
        command = str(self.sq)
        answer = "Square(side=5)"
        self.assertEqual(command, answer)

    def test_set_atributes1(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        command = str(self.rect)
        answer = "Rectangle(width=7, height=8)"
        self.assertEqual(command, answer)

    def test_set_atributes2(self):
        self.sq.set_side(2)
        command = str(self.sq)
        answer = "Square(side=2)"
        self.assertEqual(command, answer)

    def test_set_atributes3(self):
        self.sq.set_side(2)
        self.sq.set_width(4)
        command = str(self.sq)
        answer = "Square(side=4)"
        self.assertEqual(command, answer)

    def test_get_area_rectangle(self):
        command = self.rect.get_area()
        answer = 18
        self.assertEqual(command, answer)

    def test_get_area_squaree(self):
        command = self.sq.get_area()
        answer = 25
        self.assertEqual(command, answer)       

    def test_get_perimeter_rectangle(self):
        command = self.rect.get_perimeter()
        answer = 18
        self.assertEqual(command, answer)

    def test_get_perimeter_squaree(self):
        command = self.sq.get_perimeter()
        answer = 20
        self.assertEqual(command, answer)

    def test_get_diagonal_rectangle(self):
        command = self.rect.get_diagonal()
        answer = 6.708203932499369
        self.assertEqual(command, answer)

    def test_get_diagonal_squaree(self):
        command = self.sq.get_diagonal()
        answer = 7.0710678118654755
        self.assertEqual(command, answer)

    def test_get_picture_rectangle(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        command = self.rect.get_picture()
        answer = "\
*******\n\
*******\n\
*******\n"
        self.assertEqual(command, answer)     

    def test_get_picture_squaree(self):
        self.sq.set_side(2)
        command = self.sq.get_picture()
        answer = "\
**\n\
**\n"
        self.assertEqual(command, answer)   

    def test_get_picture_big(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        command = self.rect.get_picture()
        answer = "Too big for picture."
        self.assertEqual(command, answer)

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        self.sq.set_side(5)
        command = self.rect.get_amount_inside(self.sq)
        answer = 6
        self.assertEqual(command, answer)

    def test_get_amount_inside_rect2(self):
        rect2 = shape_calculator.Rectangle(4, 8)
        command = rect2.get_amount_inside(self.rect)
        answer = 1
        self.assertEqual(command, answer)

    def test_get_amount_inside_none(self):
        rect2 = shape_calculator.Rectangle(2, 3)
        command = rect2.get_amount_inside(self.rect)
        answer = 0
        self.assertEqual(command, answer)
        
if __name__ == "__main__":
    unittest.main()
