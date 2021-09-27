#input
num1 = float(input("enter the first number"))
num2 = float(input("enter the second number"))

operator = input("Please entre '+' for addition/n Please enter '-' for subtraction/n Please enter '/' for division/n Please enter '//' for division with rounded value/n Please enter '*' for multiplication")
#validation
if (operator == '+' or operator == '-' or operator == '/' or operator == '//' or operator == '*'):  
#operation
    if operator == '+': 
        ans = num1+num2
    elif operator == '-':
        ans = num1-num2
    elif operator == '/':
        if num2 != 0:
            ans = num1/num2
        else:
            print("The denominator entered is '0', hence division is not possible") 
    elif operator == '//':
        if num2 != 0:
            ans = num1//num2
        else:
            print("The denominator entered is '0', hence division is not possible")
    else:
        ans = num1*num2
else:
    print("enter valid operator")
print("your ans is", ans)