import math

def area(base,height):
        """Return the area of a triangle with dimension base
        and height
        >>>are(10,20)
        100.0
        >>>area(3.4, 7.5)
        12.75
        """
        return base * height/2
def perimeter(side1,side2,side3):
        '''(number, number, number)-> number
        Return the perimeter of the a triangle with sides
        of lenght side1, side2,side3.
        >>>perimeter(3,4,5)
        12.0
        >>>perimeter(10.5, 6, 9.3)
        25.8
        '''
        return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
        '''(numbers, number, number)--> float
        Return the semiperimeter of a triangle with sides
        of lenght side 1, side2, side3.
        >>> semiperimeter (3, 4, 5)
        6.0
        >>> semiperimeter (10.5, 6, 9.3)
        12.9
        '''
        return perimeter(side1,side2,side3)/2

def choose(base,height, base2, height2):
        print('bigger slice is', max(area(base,height),area(base2,height2)))
        return max(area(base,height),area(base2,height2))

def area_hero(side1, side2, side3):
        '''
        returning the area of a triangle of
        lenght side1, side2, side3.
        (number,number,number)-> float
        >>>area_hero(3,4,5)
        6.0
        >>>area_hero(10.5,6,9.3)
        7.73168584850189
        '''
        semi= semiperimeter(side1,side2,side3)
        area= math.sqrt(semi * (semi-side1) * (semi-side2) * (semi - side3))
        return area

