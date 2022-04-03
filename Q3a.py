def switch(module):
    statement = {
        "CSC1006": "Mathematics 2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structures and Algorithms",
        "CSC1009": "Object-Oriented Programming"

    }
    return statement.get(module, "not a Valid Module Code")


modulecode = input("Enter the Module Code: ")

print("The Module " + modulecode + " is " + switch(modulecode))