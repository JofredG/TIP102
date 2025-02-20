def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood! My name is {name}.")

greeting("Michael")
greeting("Winnie the Pooh")


def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old bear.")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)


def get_item(items, x):
    if items[x]:
        return items[x]
    else:
        return None



items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
