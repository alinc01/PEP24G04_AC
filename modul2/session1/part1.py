# variables

my_str = "Hello World"

print(
    my_str,
    "New String"
)

my_str = "Hello World2"

print(
    my_str,
    "New String"
)

my_str = 100000
print(
    my_str,
    "New String"
)

# compare
print(my_str == "100000")  ## str object not equal to int bject

# operations
result = 100 + 100
print(result)

result = result + 10
print(result)

result += 10
print(result)

result = 100 * 100
print(result)

result *= 3
print(result)
print(type(result))

result = 10/2
print(result)
print(type(result))

result = 5.5
print(result)
print(type(result))

result1 = "10"
result2 = "20"
print(result1 + result2)

result1 = 10
result2 = "20"
print(result1 * result2)




# input function

result1 = input("Set Value1: ")
print(result1)
print(type(result1))

result2 = input("Set Value2: ")
print(result2)
print(type(result2))

print("Result of multipling", int(result1) * int(result2))

# result = print("Set Value: ")
# print(result)
# print(type(result))

