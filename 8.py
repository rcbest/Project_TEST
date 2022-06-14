aliens = 2
password = "ALIENS"
print("Quickly! Aliens are invading the planet.")
print("You need to activate the global defence platform")
print("Hope you know the password, for Earth's sake...\n")
print("_________________________________________________")
print("    WELCOME TO THE GLOBAL DEFENCE NETWORK")
print("_________________________________________________\n")
guess = input("Please enter the password: ").upper()
while guess != password:
    print("\nINCORRECT PASSWORD.\n")
    aliens = aliens **2
    print("There are", aliens, "aliens now on Earth")
    if aliens > 74000000000:
        break
