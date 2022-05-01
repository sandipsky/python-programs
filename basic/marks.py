try:
    a = int(input("Enter your marks"))
except Exception:
    print("Not a number")
else:
    if a>80:
        print("Examplory")
    elif a>75 and a<=79:
        print("Distinction")
    elif a>60 and a<=74:
        print("First class")
    elif a>50 and a<=59:
        print("Second class")
    elif a>45 and a<=49:
        print("Third Class")
    elif a<45:
        print("Try again")
    else:
        print("Enter marks between 0 to 100")