isMale = True
isTall = False

if isMale and isTall:
    print("Male and Tall")
elif isMale and not(isTall):
    print("Male and not Tall")
elif not(isMale) and isTall:
    print("Not Male and Tall")

def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("num1 is the greatest")
    elif num2 > num1 and num2 > num3:
        print("num2 is the greatest")
    elif num3 > num1 and num3 > num2:
        print("num3 is the greatest")
    else:
        print("All are equal")

max_num(1, 2, 3)