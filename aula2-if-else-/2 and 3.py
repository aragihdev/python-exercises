age = int(input("How old are you?"))

if age < 13:
    print("You're a kid.")
elif age < 18:
    print("You're a teenager.")
elif age < 65:
    print("You're an adult.")
else:
    print("You're old.")