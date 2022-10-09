# GitHub.com/AliRezaJoodi

class Category:
  # When an object is created
  def __init__(self, category):
    self.category = category
    self.ledger = []

  # When an object is printed
  def __str__(self):
    s = self.category.center(30, "*") + "\n"
    for item in self.ledger:
      temporary = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      s = s + temporary[:30] + "\n"
    s = s + "Total: " + str(self.get_balance()) + "\n"
    return s

  # Append an amount and description to the ledger list
  def deposit(self, amount, description=""):
    temporary = {}
    temporary['amount'] = amount
    temporary['description'] = description
    self.ledger.append(temporary)

  # Append an negative amount and description to the ledger list
  # If there are not enough funds, nothing should be added to the ledger.
  # This method should return True if the withdrawal took place, and False otherwise. 
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      temporary = {}
      temporary['amount'] = -amount
      temporary['description'] = description
      self.ledger.append(temporary)
      return True
    else: 
      return False

  # Returns the current balance of the budget category based on the deposits and withdrawals that have occurred
  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item['amount']
    return balance

  # Does amount is greater than the balance?
  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  # Tranfer an amount to another budget category
  def transfer(self, amount, goal_category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + goal_category.category)
      goal_category.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False

def create_spend_chart(categories):
  s = "Percentage spent by category"

  spend = []
  for category in categories:
    temporary = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temporary = temporary + abs(item['amount'])
    spend.append(temporary)
  total = sum(spend)
  percentage=[]
  #percentage = [i/total * 100 for i in spend]
  for i in spend:
    percentage.append(i/total*100)  

  for i in range(100, -1, -10):
    s = s + "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j > i:
        s = s + " o "
      else:
        s = s + "   "
    s = s + " " # Create a whitespace in the end
  s = s + "\n    ----------"

  length_categories = []
  for item in categories:
    length_categories.append(len(item.category))
  max_length = max(length_categories)

  for i in range(max_length):
    s =s + "\n    "
    for j in range(len(categories)):
      if i < length_categories[j]:
        s = s + " " + categories[j].category[i] + " "
      else:
        s = s + " " + " " + " "
    s = s + " " # Create a whitespace in the end

  return s
