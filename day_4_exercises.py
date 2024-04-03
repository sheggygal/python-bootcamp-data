#ex1
my_fav_numbers = {23,6,9}
my_fav_numbers.add(7)
my_fav_numbers.add(17)
print(my_fav_numbers)

fav_numbers_list = list(my_fav_numbers)

if fav_numbers_list:
    last_index = len(fav_numbers_list) - 1
    last_number = fav_numbers_list.pop(last_index)

my_fav_numbers = set(fav_numbers_list)

print("Removed the last number:", my_fav_numbers)
friend_fav_numbers = {13, 666}
family_numbers = my_fav_numbers.union(friend_fav_numbers)
print(family_numbers)

#ex2 No, it's impossible to add more objects into existing tupple. Cause tupples are immutable and can't be manipulated after creation

#ex3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
print(basket)

basket.remove("Blueberries")
print(basket)

basket.append("Kiwi")
print(basket)

basket.insert(0, "Apples")
print(basket)


apple_count = basket.count("Apples")
print(apple_count)


basket.clear()
print(basket)

#ex4 Float is data type that represents a real number with decimal points. Integer is a real number without decimals
sequence = []
start = 1.5
step = 0.5
end = 5

current_number = start
while current_number <= end:
    sequence.append(current_number)
    current_number += step

print(sequence)

sequence = [i/2 for i in range(3,13)]
print(sequence)

#ex5
for i in range(1,21):
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

#ex6
my_name = "Liudmila"

while True:
    user_name = input("What is your name? ").capitalize()
    if user_name == my_name:
        print("heyheyhey")
        break

    else:
        print("No, try again")

#ex7
fav_fruits_str = input("Please enter your favorite fruit(s), separated by a single space: ").lower()
fav_fruits_list = fav_fruits_str.split()


new_fruit = input("Please enter any fruit").lower()

if new_fruit in fav_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

#ex8
toppings = []

total_price = 10

while True:
    topping = input("Enter a topping , or call quit to finish: ").lower()
    if topping == "quit":
        break
    toppings.append(topping)

    total_price += 2.5

    print("Adding toppings")

print("\nToppings on your pizza:")
for topping in toppings:
    print("-" + topping)

print(f"\nTotal price of your pizza: ${total_price}")

#ex9

ticket_price_toddler = 0
ticket_price_child = 10
ticket_price_full = 15
total_cost = 0

num_family_members = int(input("Enter the number of people in your group: "))

for i in range(num_family_members):
    age = int(input(f"Enter the age of family member {i+1}: "))
    if age < 3:
        total_cost += ticket_price_toddler
    elif 3 < age < 12:
        total_cost += ticket_price_child
    else:
        total_cost += ticket_price_full
print("Total cost of your ticket: ", total_cost)

names = ['Mary', 'Dan', 'Stacy', 'Bibi']

permitted_names = []

for name in names:
    age = int(input(f"Please, enter your age, {name}: "))
    if age < 21:
        permitted_names.append(name)

print(f"you are too young to watch this. Go learn some useful shit, {permitted_names}")

#ex10

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich.lower()}")
