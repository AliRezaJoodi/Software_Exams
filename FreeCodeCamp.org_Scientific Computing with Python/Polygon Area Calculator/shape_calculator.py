# GitHub.com/AliRezaJoodi

class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    #s = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    s = "Rectangle(width={}, height={})"
    s = s.format(self.width, self.height)
    return s

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = (self.width * self.height)
    return area

  def get_perimeter(self):
    perimeter = ((2 * self.width) + (2 * self.height))
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2) + (self.height ** 2)) ** 0.5
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      picture = "Too big for picture."
    else: 
      picture = ("*" * self.width + "\n") * self.height
    return picture

  def get_amount_inside(self, shape):
    piece_width = self.width // shape.width
    piece_height = self.height // shape.height
    amount_inside = piece_width * piece_height
    return amount_inside


class Square(Rectangle):

  def __init__(self, length):
    super().__init__(length, length)

  def __str__(self):
    s = "Square(side={})"
    s = s.format(self.width)
    return s

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side
