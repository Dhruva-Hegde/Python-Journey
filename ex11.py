age=int(input("Enter your age"))

if age<5:
    print("Tickect is free")

elif age<=12:
    print("Discount")

elif age>=60:
    print("Senior")

else:
    print("full fare")