# Define the height of the pyramid
rows = 5

# Initialize the outer loop variable
i = 0

while i < rows:
    # Initialize the inner loop variable for spaces
    j = 0
    # Print spaces
    while j < rows - i - 1:
        print(" ", end="")
        j += 1
    
    # Initialize the inner loop variable for asterisks
    j = 0
    # Print asterisks
    while j < 2 * i + 1:
        print("*", end="")
        j += 1
    
    # Move to the next line
    print()
    
    # Increment the outer loop variable
    i += 1