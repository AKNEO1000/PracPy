feature = str(input("This feature requires you to be level 100, if you are level 100, type y. If not, type n: "))

if feature == "y":
    print("you can unlock the items.")
if feature == "n":
    print("this feature requires you to be level 100.")
else:
    print("please put valid arguments only.")