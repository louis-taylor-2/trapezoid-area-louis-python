#Area of trapezoid
#This program will ask for the dimensions of a trapezoid. It will then calculate the area and display it to the user
print ("Today we will calculate the area of a trapezoid.")

#Get base 1 length from user and convert it to a float
base1 = float(input("Enter the length of the smallest base (cm): "))

#get base 2 length from user and convert it to a float
base2 = float(input("Enter the length of the largest base (cm): "))

#Get height from user and convert it to a float
height = float(input("Enter the height of the trapezoid (cm): "))

#Calculate the area of the trapezoid
area = (base1 + base2) / 2 * height

#display area
print ("the area of a trapezoid with a small base of " + str(base1) + " cm long, a large base of " + str(base2) + " cm long and a height of " + str(height) + " cm is " + str(area) + " cm^2.")