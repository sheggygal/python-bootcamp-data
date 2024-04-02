#ex1

print("Hello world\n" * 4, end='')

#ex2
result = (99 ** 3) * 8
print(result)

#ex3
#Predict the output of the following code snippets:
# 5 < 3 expected False
# 3 == 3 expected True
# 3 == "3" expected False
# "3" > 3 expected error
# "Hello" == "hello" expected False

#ex4
comp_brand = "Asus"
print(f"I have an {comp_brand} computer")

#ex5
name = "Liudmila"
age = 34
shoe_size = 36
info =f"My name is {name}, I'm {age} and I need AirJordans size {shoe_size} right now!"
print(info)

#ex6
a=10
b=8.9
if a>b:
    print("Hello world!")

#ex7
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#ex8
my_name = "liudmila"

user_name = input("What is your name? ")

if user_name == my_name:
    print("ha-ha, silly name")
else:
    print(f"Nice to meet you, {user_name}")

#ex9
height = int(input("What is your height in centimeters? "))

if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")