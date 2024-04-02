string1 = input('Enter 10 characters: ')

if len(string1)<10:
    print("Not long enough")
elif len(string1)>10:
    print("String too long")
elif len(string1)==10:
    print("Perfect match")

    first_char=string1[0]
    last_char=string1[-1]
    print(f"First character:{first_char}, last character:{last_char}")

    print("Constructing string character by character:")
    constructed_string = ""
    for i in range(len(string1)):
        constructed_string += string1[i]
        print(constructed_string)


