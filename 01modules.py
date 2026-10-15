"""
Modules are an extremely useful tool for organizing and reusing code.
A module is a python file that contains code, variable, functions, classes 
that you can include in another program
Just like function, Modules help make your code:
-reusable
-organized
-easier to maintain

DRY principle - "Don't repeat yourself"

Examples of built in modules:
time, random, os, math........

eg.
import math #importing the module
print(math.pi) #Using code from the module
"""
#import math
#Let's see the built in modules
#help("modules")
#help(math)

#import a module with an alias
import math as m 
print(m.pi)

#we could also import just specific functions from a module
from random import randint
print(randint(5,10))
