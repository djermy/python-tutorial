# lesson 3, data types.
# integers are whole numbers.
# git@github.com:djermy/python-tutorial.gitage = 25
# floats are real numbers with decimal points.
money = 3.50

# strings are characters, "hello world"
firstName = "john"
lastName = "doe"
print(firstName + " " + lastName)

quote = """always code as if the guy who ends up maintaining
 your code will be a violent psychopath
  who knows where you live.
  -John Woods-"""
print(quote)

# bool = boolean, true/false
print(10>5)
print(5>10)

# type() = data type stored in a variable
print(type(country))
# print(type(age))
print(type(money))

# input() takes user input in the form of a string and can store it in variables
username = input("Please enter your name: ")
age = int(input("please enter your age: "))
print("hello " + username + "!")
print("age " + str(age))
print(type(username))
print(type(age))