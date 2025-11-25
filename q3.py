def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct: #check for the value of key in dct
        print(dct[key]) #print the value if match

    dct[key]=value #update the value of key with new one

    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))