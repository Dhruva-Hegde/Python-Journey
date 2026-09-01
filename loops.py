a=True
attempt=1
while a :
    if attempt%2!=0:
        attempt=attempt+1
        continue
        
    print(f"try {attempt}")
    attempt=attempt+1
    if attempt>100:
        break

print("stop")