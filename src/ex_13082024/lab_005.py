# Take a user input a,b and calculatethe sum,multiplication,division and subtraction

num1 = int(input("enter the no1"))
num2 = int(input("enter the no2"))

# we need to convert string to integer so we need to use int
# we can not subtract, multiply and division to string
# str -> int
print(type(num1))
print(type(num2))

print("sum is", num1+num2)
print("sub is", num1-num2)
print("Mul is", num1*num2)
print("Div is", num1/num2) # python is very smart language ex (3/2 -> 1.5)