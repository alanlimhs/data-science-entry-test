def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    x = num/divisor #divide the numbers
    
    if(x.is_integer()): #check if the result is an integer
        return True
    else:
        return False



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
print(check_divisibility(10,2))
print(check_divisibility(7,3))
