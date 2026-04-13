# A dictionary is a mutable, unordered collection of items where each item has:

# a key (unique)
# a value
stu = {
    "name": "Rohan",
    "age": "21",
    "branch": "Mechanical"
}
# print(stu["age"])
# print(stu.get("age"))

# stu["branch"] = "cse"
# print(stu)
del stu["branch"]
print(stu)