r = "Hello"

def greet():
    r= "Hi"
    print(r)
greet()
print(r)
count = "Original Variable"
def variable1():
    count = "New Variable"
    def variable():
        print(count)
    variable()
variable1()
print(count)
