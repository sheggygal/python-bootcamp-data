#ex1
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

list_1.extend(list_2)
print(list_1)

#ex2

for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

#ex3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
username = input("What is your name? ").capitalize()

if username in names:
    index = names.index(username)
    print(f"The index of {username} name is", index)
else:
    print(f"{username} is not in the list")

#ex4
num1 = float(input("Input the 1st number: "))
num2 = float(input("Input the 2nd number: "))
num3 = float(input("Input the 3rd number: "))

greatest_number = max(num1, num2, num3)

print("The greatest number is:", greatest_number)

#ex5
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
    if letter in 'aeiou':
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is a consonant.")

#ex6
word_string = input("Please enter 7 words, separated by a single space: ").lower()
word_list = word_string.split()

letter = input("Enter a character: ").lower()

for word in word_list:
    if letter in word:
        index = word.index(letter)
        print(f"The index of the first appearance of '{letter}' in '{word}' is: {index}")
    else:
        print(f"'{letter}' does not exist in '{word}'.")

#ex7
numbers = list(range(1, 1000001))

print("Minimum number in the list:", min(numbers))
print("Maximum number in the list:", max(numbers))

total_sum = sum(numbers)
print("Sum of all numbers from 1 to 1 million:", total_sum)

#ex8
numbers_str = input("Enter a sequence of comma-separated numbers: ")

numbers_list = numbers_str.split(',')

numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)

#ex9
import random

games_won = 0
games_lost = 0

while True:
    random_number = random.randint(1, 9)
    user_guess = int(input("Guess a number from 1 to 9: "))

    if user_guess == random_number:
        print("Winner!")
        games_won += 1
    else:
        print("Better luck next time.")
        games_lost += 1

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break

print("Total games won:", games_won)
print("Total games lost:", games_lost)