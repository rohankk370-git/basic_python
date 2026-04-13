# def Wish(fname, lname ):
#     print("good morning !", fname, lname)
#     print("how are you !")
#     print("heyy!")
# Wish("harry", "das")
# Wish("rohan", "kumar")

def add(a, b):
    # print(a + b)
    return a + b

c = add(4, 3)
print(c)

# function_default value

def greet(name ="user", city = "delhi"):
    print("hello", name, city)

greet()
greet("rohan")