birthdate_str = input("Enter your birthdate (DD/MM/YYYY): ")

day, month, year = map(int, birthdate_str.split('/'))

current_date = input("Enter the current date (DD/MM/YYYY): ")
current_day, current_month, current_year = map(int, current_date.split('/'))

age = current_year - year
if (current_month, current_day) < (month, day):
    age -= 1

leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

print("       ___iiiii___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

if leap_year:
    print("\nHappy leap birthday! You get two cakes and", end=" ")
else:
    print("\nHappy birthday! You get", end=" ")

if age >= 10:
    last_digit = int(str(age)[-1])  # Get the last digit of the age
    print(last_digit, "candles.")
else:
    print(age, "candles.")