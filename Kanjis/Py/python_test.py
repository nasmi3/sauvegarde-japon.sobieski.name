def foo(age, name="name"):
    print("My quest is {name}")
    print("My age is {age}")

def foo2(age, name="name"):
    print(f"My quest is {name}")
    print(f"My age is {age}")
# print("test 1")
# foo(21, "Jules")

# print("test 2")
# foo(age = "21", "Jules")

print("test 3")
foo(21, name="Jules")

print("test 4")
foo2(21, name="Jules")
