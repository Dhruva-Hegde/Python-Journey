pin="1234"
trails=0

while trails<3 :
    print(f"trail {trails}")
    trails=trails+1
    input_pin=input("enter pin")
    if input_pin==pin:
        print("correct")
        break
    else:
        print("INCORRECT")


