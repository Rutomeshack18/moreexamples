def greet(first_name, last_name):
    print(f"Your name is {first_name} {last_name}")
greet("Meshack", "Ruto")


def area(length, width):
    return length * width
area_rectangle = area(3, 2)
print(area_rectangle)

#Function to check if a number is odd or even
def checker(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
checker(10)