pi = 3.14159
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2*pi*radius


def area(radius:float) -> float:
    '''Takes the radius and finds the are of a circle'''
    return pi * (radius**2)

def main():
    print("Just testing.")
    print(area(7))
    print(pi)
    #Every python file has a special built in variable called __name__
    #If you run the file directly, __name__ is set to __main__
    #If you import the file __name__ is set to the name that script
    print(__name__)
    print("Just testing.")

if __name__ == "__main__":
    main()