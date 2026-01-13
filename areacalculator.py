# Hey let's make a Area Calulator as a part of my codex project, i'll probably add this to my Git and resume. This is very simple, let's do this.
print("Enter 1 for calculating area of SQUARE")
print("Enter 2 for calculating area of RECTANGLE")
print("Enter 3 for calculating area of TRIANGLE")
print("Enter 4 for calculating area of CIRCLE")
print("Enter 5 to Quit the Calculator")

i = int(input("Enter a number "))

if i == 1:
    print("You have chose SQUARE, Enter the dimentions below")
    side = float(input("Enter side of the square: "))

    area1 = side ** 2

    print("Area of square is = ", area1)

elif i == 2:
    print("You hace chose RECTANGLE, Enter the length and breadth below")
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))

    area2 = length * breadth

    print("Area of rectangle is = ", area2)

elif i == 3:
    print("You have chose TRIANGLE, Enter base and height below")
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter height of the triangle: "))

    area3 = 0.5 * (base * height)

    print("Area of the  Triangle is: ", area3)

elif i == 4:
    print("You have chose CIRCLE, Enter the radius below")
    radius = float(input("Enter the radius of circle: "))

    area4 = 3.1415 * (radius ** 2)

    print("Area of the circle is: ",area4)

elif i == 5:
    print("Quit!, Thank you for using the Area Calculator")

else:
    print("Invalid Input, Please refer to statement above")
          


     