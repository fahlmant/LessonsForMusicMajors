
def hello(name):
	print("Hello, " + name)

def adder(num1, num2):
	num3 = int(num1) + int(num2)
	print("Sum " + num3)
	
name = input("What's your name?\n")
hello(name)
num1 = input("First Number: \n")
num2 = input("Second Number: \n")
adder(num1, num2)
