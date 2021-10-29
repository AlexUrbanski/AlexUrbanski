import math 
# newtons method is a quick way to find when a function is equal to 0
# the more iterations that occur, the more accurate the approximation 
# I use 3 example functions where there is only 1 f(x) = 0 value to demonstrate how this can be done using python 

# will calculate when x^4 + 3x^3 -x - 10 = 0 using newtons method 
def fA(x):
  # function
  return x**4 + 3*x**3 - x - 10 

def fA1(x):
  # derivative
  return 4*x**3 + 9*x**2 - 1 

def newtonsA(iter = 5): # set default iterations to 5 if no value entered
  # set xnot original value to 2
  xnot = 2 
  # iterate iter times 
  for i in range(iter):
    xnot = xnot - (fA(xnot) / fA1(xnot))
  return xnot 

# the larger the number passed in, the more accurate the output
print ("the more xnots calculated, the more accurate the answer")
print ("f(x) = x^4 + 3x^3 - x - 10 , lets find when f(x) = 0 ")
user_iter = int(input("How many times would you like to find xnot?   ")) 
r = newtonsA(user_iter)
print (f"f(x) = 0  when x = {r} ")



# will calculate when cosx = x 
# f(x) = cosx - x 
# set cosx - x = 0 , then newtons method can be applied 

def fB(x):
  # function
  return math.cos(x) - x 

def fB1(x):
  # derivative 
  return -math.sin(x) - 1 

def newtonsB(iter = 5):
  xnot = 1 # arbitrary guess 
  for i in range(iter):
    xnot = xnot - (fB(xnot)/fB1(xnot))
  return xnot 
  
print ('\n'*3)
print ("cosx = x")
print ("f(x) = cosx - x , lets find when f(x) = 0 ")
user_iter = int(input("How many times would you like to find xnot?   ")) 
r = newtonsB(user_iter)
print (f"f(x) = 0  when x = {r} ")



# newtons method to find root 2 
def fC(x):
  # create a function when x = root 2, y = 0 
  # so , x^2 - 2
  return x**2 - 2

def fC1(x):
  # derivative 
  return 2*x - 1 

def newtonsC(iter = 5):
  xnot = 1 # close guess 
  for i in range(iter):
    xnot = xnot - (fC(xnot)/fC1(xnot))
  return xnot 

print ('\n'*3)
print ("approximate sqrt(2) using newtons method")
print ("create the function f(x) = x^2 - 2")
user_iter = int(input("How many times would you like to find xnot?   "))
r = newtonsC(user_iter)
print (f"root 2 approximation =  {r}")
