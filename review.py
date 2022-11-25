# reviewing all classes that came before the point I started in (lesson 1XX)

x = 34
y = 'hello'

print(type(x)) #to get the current type of a variable
print(type(y))

#so we can check types

name = input("What is your name?")
if (type(name) !=  str):
    print("This is not a string!")
else:
    print("Hello " + name + "!")