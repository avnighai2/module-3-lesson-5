try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma:"))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Dividon by zero is error !!")

except SyntaxError:
    print('Comma is missing. Enter numbers seperated by a comma like this 1,2')

else:
    print("wrong input")

finally:
    print("this will execute no matter what")