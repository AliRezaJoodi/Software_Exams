# GitHub.com/AliRezaJoodi

import copy
import random

class Hat:

  # Arbitrary Keyword Arguments (**kwargs)
  # You do not know how many keyword arguments that will be passed into your function
  # The function will receive a dictionary of arguments and convert to correct contents.
  # Example for input: {"red": 2, "blue": 1}
  # Converted to: ["red", "red", "blue"]
  def __init__(self, **kwargs):
    ##print(kwargs)
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    ##print (self.contents)

  def draw(self, number):
    drawn_ball = []
    drawn_balls = []
    if number < len(self.contents):
      for i in range(number):
        choice = random.randrange(len(self.contents))
        ##print ("choice=", choice)
        drawn_ball = self.contents[choice]
        drawn_balls.append(drawn_ball)
        self.contents.pop(choice)
        ##drawn_balls.append(self.contents.pop(choice))
        ##print (drawn_ball)
        ##print (drawn_balls)
        ##print (self.contents)
    else:
      drawn_balls = self.contents
    #print ("drawn_balls=", drawn_balls)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  #expected_balls_number = []
  #for key, value in expected_balls.items():
      #expected_balls_number.append(value)
  num_accepted = 0

  for i in range(num_experiments):
    copy_hat = copy.deepcopy(hat)
    drawn_balls = copy_hat.draw(num_balls_drawn)
    #print("drawn_balls", drawn_balls)

    expected_balls_number = []
    acceptable_drawn_balls = []
    for key, value in expected_balls.items():
      expected_balls_number.append(value)
      acceptable_drawn_balls.append(drawn_balls.count(key))
    #print(acceptable_drawn_balls)

    if acceptable_drawn_balls >= expected_balls_number:
      num_accepted = num_accepted + 1

  probability = num_accepted/num_experiments

  return probability