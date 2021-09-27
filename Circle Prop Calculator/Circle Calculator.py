#Name: Amruth Kanakaraj
#Student ID: 201547293



#in program comments are given only for first section as I've used the same concept in all sections.


#to calculate diameter (d), circumference (C) and area (A), given the radius (r) of a circle. option 1
def radiusGiven():
    while(1):
        #trying to eliminate most of valueErrors
        try:
            radius = float(input("Enter the given radius of the circle in cm: "))
        except ValueError:
            print("invlaid input. please input only numbers.")
            continue
        #checking the conditions of the input
        if radius >=0:
            diameter = 2*radius
            circumference = 2*3.14*radius
            area = 3.14*radius*radius
            break
        else:
            print("Invalid Input")
            continue
        #printing the output of the program
    print("The given radius of the circle 'r' is: ", radius,"cm\n"
          "The diameter of the circle 'd' is: ", diameter, "cm\n"
          "The circumference of the circle 'C' is: {:.2f}".format(circumference),"cm\n"
          "The area of the circle 'A' is: ", area, "cm^2")
    return

#to calculate diameter (d), area (A) and radius (r), given circumference (C) of a circle. option 2
def circumferenceGiven():
    while(1):
        try:
            circumference = float(input("Enter the circumference of the circle in cm: "))
        except ValueError:
            print("Input is not a number")
            continue
        if circumference >0:
            diameter = circumference/3.14
            radius = circumference/(2*3.14)
            area = (circumference)**2/(4*3.14)
            break
        else:
            print("Invalid input")
            continue 
    print("The given circumference of the circle 'C' is: ", circumference,"cm\n"
          "The diameter of the circle 'd' is: {:.2f}".format(diameter) , "cm\n"
          "The radius of the circle is: {:.2f}".format(radius), "cm\n"
          "The area of the circle is: {:.2f}".format(area),"cm^2")
    return

#to calculate diameter (d), radius (r) and circumference (C), given area (A) of a circle. option 3
def areaGiven():
    while(1):
        try:
            area = float(input("Enter the area of the circle in cm^2: "))
        except ValueError:
            print("Input is not a number")
            continue
        if area >0:
            diameter = 2*((area/3.14)**0.5)
            radius = (area/3.14)**0.5
            circumference = 2*3.14*((area/3.14)**0.5)
            break
        else:
            print("Invalid input")
            continue
    print("The given area of the circle 'A' is: ", area,"cm^2\n"
          "The diameter of the circle 'd' is: {:.2f}".format(diameter) , "cm\n"
          "The radius of the circle is: {:.2f}".format(radius), "cm\n"
          "The circumference of the circle 'C' is: {:.2f}".format(circumference),"cm")
    return

#main function program
def main():
    #main menu greetings
    while(1):
        print("Hi, Greetings, Welcome to main menu")
        print("Please choose the following from the Main Menu")
        print("Select 1 to find the diameter, circumference and area of the circle")
        print("Select 2 to find the diameter, radius and area of the circle")
        print("Select 3 to find the diameter, circumference and radius of the circle")
        print("Entre q to exit the program")
        
        #calling the functions below
        choice = input("Please enter your choice: ")
        if choice == '1':
            radiusGiven()
        elif choice == '2':
            circumferenceGiven()
        elif choice == '3':
            areaGiven()
        elif choice == "q":
            print('thankyou for using the services')
            break
        else:
            print('invalid option. try again!! \n\n')
            

main()