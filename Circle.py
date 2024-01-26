'''
Name: Ramya
Date: 21/01/24
Task: Object Oriented Programming Scheme
'''

# Created a Python Class called circle
class Circle:

    # Created a private variable called pi
    __pi = 3.14
    
    # Created a constructor of class Circle
    def __init__(self, radius):
        self.radius = radius
            
    # Created a method for finding area of circle
    def area_of_circle(self):
        area = self.__pi * self.radius * self.radius
        return area
    
    # Creating a method for finding perimeter of a circle
    def perimeter_of_circle(self):
        perimeter = 2 * self.__pi * self.radius
        return perimeter
    
# Created a list containing a list of radii
list_of_radii = [10,501,22,37,100,999,87,351]

# Execution of main method
if __name__ == "__main__":
    # Iterate over the list of radii
    for radius in list_of_radii:
        # Created an object for class Circle
        circle = Circle(radius)
        
        # Created variables to store area and perimeter of circle
        area = circle.area_of_circle()
        perimeter = circle.perimeter_of_circle()
        
        # Print the area and perimeter of each radius
        print(f"Area of the circle for {radius}: {area}")
        print(f"Perimeter of circle for {radius}: {perimeter:.2f}")
        print()