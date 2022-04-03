from re import A


def average (x,y):
    a = (x+y)/2
    return a


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
avg = average(x,y)

print("The average of " + str(x) + " and " + str(y) + " is: " + str(avg))