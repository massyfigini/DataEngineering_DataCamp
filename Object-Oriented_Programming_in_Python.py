####################
# OOP Fundamentals #
####################

### Exploring object interface

# Print the mystery employee's name
print(mystery.name)

# Print the mystery employee's salary
print(mystery.salary)

# Give the mystery employee a raise of $2500
mystery.give_raise(2500)

# Print the salary again
print(mystery.salary)


### Create a class

# Create an empty class Employee
class Employee:
    pass

# Create an object emp of class Employee 
emp = Employee()

# Include a set_name method
class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Print the name of emp
print(emp.name)

class Employee:
  
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method
  def set_salary(self, new_salary):
    self.salary = new_salary
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)


### Using attributes in class definition

# 1
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 
  
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary attribute of emp
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500

# Print the salary attribute of emp again
print(emp.salary)

# 2
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, raise_amount):
        self.salary = self.salary + raise_amount 


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

print(emp.salary)
emp.give_raise(1500)
print(emp.salary)

# 3
class Employee:
    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12


    
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()

# Print mon_sal
print(mon_sal)


### Add a class constructor

# 1
class Employee:
    # Create __init__() method
    def __init__(self, name, salary=0):
        # Create the name and salary attributes
        self.name = name
        self.salary = salary
    
    # From the previous lesson
    def give_raise(self, amount):
        self.salary += amount

    def monthly_salary(self):
        return self.salary/12
        
emp = Employee("Korel Rossi")
print(emp.name)
print(emp.salary)     

# 2
class Employee:
  
    def __init__(self, name, salary=0):
        self.name = name
        # Modify code below to check if salary is positive
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
   
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

# 3
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
        
   # ...Other methods omitted for brevity ...
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)


### Write a class from scratch

# Write the class Point as outlined in the instructions
import numpy as np

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return np.sqrt(self.x**2 + self.y**2)

    def reflect(self, axis):
        if axis == "x":
            self.y = - self.y
        elif axis == "y":
            self.x = -self.x
        else:
            print("Error!")




################################
# Inheritance and Polymorphism #
################################

### Class-level attributes

# 1
# Create a Player class
class Player:
    MAX_POSITION = 10
    def __init__(self):
        self.position = 0


# Print Player.MAX_POSITION       
print(Player.MAX_POSITION)

# Create a player p and print its MAX_POSITITON
p = Player()
print(p.MAX_POSITION)

# 2
class Player:
    MAX_POSITION = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION
    

       
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()


### Changing class attributes

# 1
# Create Players p1 and p2
p1 = Player()
p2 = Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# Assign 7 to p1.MAX_SPEED
p1.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)

# 2
# Create Players p1 and p2
p1, p2 = Player(), Player()

print("MAX_SPEED of p1 and p2 before assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

# ---MODIFY THIS LINE--- 
Player.MAX_SPEED = 7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(p1.MAX_SPEED)
print(p2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)


### Alternative constructors

# 1
class BetterDate:    
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
        # Split the string at "-" and convert each part to integer
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return BetterDate(year, month, day)
        
bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)

# 2
# import datetime from datetime
from datetime import datetime

class BetterDate:
    def __init__(self, year, month, day):
      self.year, self.month, self.day = year, month, day
      
    @classmethod
    def from_str(cls, datestr):
        year, month, day = map(int, datestr.split("-"))
        return cls(year, month, day)
      
    # Define a class method from_datetime accepting a datetime object
    @classmethod
    def from_datetime(cls, datetime):
        year = datetime.year
        month = datetime.month
        day = datetime.day
        return cls(year, month, day)

# You should be able to run the code below with no errors: 
today = datetime.today()     
bd = BetterDate.from_datetime(today)   
print(bd.year)
print(bd.month)
print(bd.day)


### Create a subclass

# 1
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
  pass

# Define a Manager object
mng = Manager('Debbie Lashko',86500)

# Print mng's name
print(mng.name)

# 2
class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
  def give_raise(self, amount):
    self.salary += amount      
        
# MODIFY Manager class and add a display method
class Manager(Employee):
  def display(self):
    print('Manager ' + self.name)

mng = Manager("Debbie Lashko", 86500)
print(mng.name)

# Call mng.display()
mng.display()


### Method inheritance

# 1
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
  # Add a constructor 
    def __init__(self, name, salary=50000, project = None):

        # Call the parent's constructor   
        Employee.__init__(self, name, salary)

        # Assign project attribute
        self.project = project  

  
    def display(self):
        print("Manager ", self.name)

# 2
class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self,amount,bonus=1.05):
        Employee.give_raise(self,amount*bonus)
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)


### Inheritance of class attributes

# Create a Racer class and set MAX_SPEED to 5
class Racer(Player):
    MAX_SPEED = 5
 
# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_SPEED = ", p.MAX_SPEED)
print("r.MAX_SPEED = ", r.MAX_SPEED)

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)


### Customizing a DataFrame

# 1
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
    def __init__(self, *args, **kwargs):
        pd.DataFrame.__init__(self, *args, **kwargs)
        self.created_at = datetime.today()
    
    
ldf = LoggedDF({"col1": [1,2], "col2": [3,4]})
print(ldf.values)
print(ldf.created_at)

# 2
# Import pandas as pd
import pandas as pd

# Define LoggedDF inherited from pd.DataFrame and add the constructor
class LoggedDF(pd.DataFrame):
  
  def __init__(self, *args, **kwargs):
    pd.DataFrame.__init__(self, *args, **kwargs)
    self.created_at = datetime.today()
    
  def to_csv(self, *args, **kwargs):
    # Copy self to a temporary DataFrame
    temp = self.copy()
    
    # Create a new column filled with self.created_at
    temp["created_at"] = self.created_at
    
    # Call pd.DataFrame.to_csv on temp, passing in *args and **kwargs
    pd.DataFrame.to_csv(temp, *args, **kwargs)




####################################
# Integrating with Standard Python #
####################################

### Overloading equality

class BankAccount:
   # MODIFY to initialize a number attribute
    def __init__(self, number,balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        self.balance -= amount 
    
    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)


### Checking class equality

class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    # MODIFY to add a check for the type()
    def __eq__(self, other):
        return (self.number == other.number and type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)
print(acct == pn)


### String representation of objects

# 1
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
        Employee.str= """
            Employee name: {name}
            Employee salary: {salary}
        """.format(name = self.name, salary = self.salary)
        return Employee.str

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)

# 2
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      

    def __str__(self):
        s = "Employee name: {name}\nEmployee salary: {salary}".format(name=self.name, salary=self.salary)      
        return s
      
    # Add the __repr__method  
    def __repr__(self):   
        return 'Employee("{name}", {salary})'.format(name=self.name, salary=self.salary) 

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))


### Catching exceptions

# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1/x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")
 
a = [5,6,0,7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))


### Custom exceptions

# 1
# Define SalaryError inherited from ValueError
class SalaryError(ValueError): 
    pass

# Define BonusError inherited from SalaryError
class BonusError(SalaryError): 
    pass

# 2
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_RAISE = 5000

  def __init__(self, name, salary = 30000):
    self.name = name
    
    # If salary is too low
    if salary < MIN_SALARY:
      # Raise a SalaryError exception
      raise ValueError("Salary is too low!")
      
    self.salary = salary
      
# 3
class SalaryError(ValueError): pass
class BonusError(SalaryError): pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Rewrite using exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
       raise ValueError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
       raise ValueError("The salary after bonus is too low!")
      
    else:  
      self.salary += amount