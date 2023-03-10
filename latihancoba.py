def ifabc(a,b):
    sum = a + b
    dif = a - b
    if a == 5 or b == 5 or sum == 5 or dif == 5:
        print(False)
    else:
        print(True)

a = int(input("Value of a"))
b = int(input("Value of b"))

ifabc(a,b)