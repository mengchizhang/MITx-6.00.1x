x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("you've enter the same number")
    if y != 0:
        print("therefore, x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("Done")
name = "Vincent"
greet = "Hello there"
hello = name + greet
print(hello)
print(hello[::-1])
print(hello[::-2])
print(hello[1:4:-3])

x = 1
print(x)
x_str = str(x)
print("my fav num is", x, ".", "x = ", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)













