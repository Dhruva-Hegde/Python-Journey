print("------------Student marks------------")

a= input("Enter the student name")
b= int(input("enter the  physics marks"))
c=int(input("enter the  Chemistry marks"))
d=int(input("enter the  Maths marks"))

total=b+c+d
percentage=total/3

print(f"Name: {a}")
print(f"Physics marks: {b}")
print(f"Chemistry marks: {c}")
print(f"Maths marks: {d}")
print(f"Total marks: {total}")
print(f"Percentage: {percentage}%")
