from test_example_package.example import add_one 
from test_example_package import helloAuthor, helloWorld

digit = 1
assert (add_one(digit) == digit + 1), f"Error in add_one() function"
print(f"add_one() Pass succesfully\n")

helloAuthor()
print(f"helloAuthor() Pass succesfully\n")

helloWorld()
print(f"helloWorld() Pass succesfully\n")

print("TEST OK!!")