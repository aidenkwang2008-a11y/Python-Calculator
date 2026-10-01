Valid = False

while not Valid:
    Shape = str(input("Enter the shape (circle, square, rectangle) you want to calculate the area of:"))
    if Shape != "circle" and Shape != "square" and Shape != "rectangle":
        print("You did not enter a valid shape. Make sure to enter 'circle', 'square', or 'rectangle' with no capital letters.")
        continue
    else:
        Valid = True
        print("Proceeding...")

if Shape == "circle":
    Radius = float(input("Enter your radius:"))
    Area = 3.1415 * Radius**2
    print("The area of your circle is:", Area)
elif Shape == "square":
    Side = float(input("Enter your side length:"))
    Area = Side**2
    print("The area of your square is:", Area)
elif Shape == "rectangle":
    Length = float(input("Enter your side length:"))
    Width = float(input("Enter your width:"))
    Area = Length * Width
    print("The area of your rectangle is:", Area)

Continue_Answer = "Placeholder"

while Continue_Answer != "yes" or Continue_Answer != "no":
    Continue_Answer = str(input("Do you want to calculate another shape area? (yes/no):"))
    if Continue_Answer == "yes":
        Valid = False
    elif Continue_Answer == "no":
        print("Thank you for using the area calculator!")
        break
    else:
        print("You did not enter a valid answer. Make sure to enter 'yes' or 'no' with no capital letters.")
