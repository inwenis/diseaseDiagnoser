import time

symptoms = input("Enter your symptoms and press [enter]")
if symptoms:
    print("processing...")
    print("accessing wikipedia...")
    print("accessing google...")
    time.sleep(2) # pretend you're actually doing something
    print("You have cancer");
input("Press [enter] to exit")
