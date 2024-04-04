first_angle = int(input("Please enter the first angle: "))
second_angle = int(input("Please enter the second angle: "))
third_angle = int(input("Please enter the third angle: "))


if first_angle <=0 and second_angle <=0 and third_angle <= 0:
    print("Numbers are invalid")
elif (first_angle + second_angle + third_angle) != 180:
    print("Numbers are invalid!")
elif (first_angle and second_angle and third_angle) < 90:
    print("This triangle is acute")
elif (first_angle or second_angle or third_angle) == 90:
    print("This is a right triangle")
elif (first_angle or second_angle  or third_angle) > 90:
    print("This is an obtuse triangle")
else:
    print("I have no idea what you did")

input('Press ENTER to exit')

#A right triangle has one angle of 90°
#A obtuse triangle has one angle of more than 90°
#A triangle is acute if all three angles are less than 90°