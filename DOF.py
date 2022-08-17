#TO FIND OUT THE DEGREE OF FREEDOM OF LINKED MECHANISMS 


#To accept the input from the user 
l = int(input("Enter number of links"))
j = int(input("Enter number of joints"))


#Formula for degree of freedom 
DOF = (3*(l-1)-2*j)

# printig the degree of freedom 
print("The degree of freedom is ", DOF )

#Conditions to display the types of mechanisms 
if (DOF==0):
    print("The mechanism has zero degree of freedom and the mechanism is a structure")
elif (DOF <= 0):
    print("The mechanism has negative degree of freedom which means the mechanism is impossible")
elif (DOF == 1):
    print("The mechanism has a single degree of freedom")
else:
    print("The mechanism has multiple degree of freedom")
