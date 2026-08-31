# day="monday"
# is_raining=False

# if day=="sunday" or "saturday":
#     if not is_raining:
#         print("visit")
#     else:
#         print("do not visit")
# else:
#     print("its weekday bro")


gender=input("enter your gender")
age=int(input("enter your age"))

if gender=="female":
    print("ticket is free")
else:
    if age<5:
        print("free")
    elif age<=12:
        print("discount")
    elif age>60:
        print("senior")
    else:
        print("full fare")