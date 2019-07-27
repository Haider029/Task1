n = input("Please insert a string")
letter = 0
digit = 0
for i in n:
    if(i >= 'A' and i <= 'z'):
        letter += 1
    elif ( i>='0' and i <= '9'):
        digit += 1
print("Letters:",letter)
print("Digits:",digit)
