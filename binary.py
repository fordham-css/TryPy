'''
binary.py
----------
Computes the decimal value of a binary string
- Lists
- Loops
----------
Python Demo Workshop, March 22nd 2017
'''

### Declare variables to be used

# List Data Structure
binary = [] #  binary = list()
VALUES = [0, 1] # VALUES[0] = 0; VALUES[1] = 1

# Integer Data Type
decimal = 0

# Bool Data Type
flag = True

### While Loop
# Will continue to execute code as long as condition is True (1)
while flag:
    bit = raw_input('Please enter a 1 or 0 (enter break to finish string: ')

    # BREAK CASE
    # Want to catch before typecasting bit to int, as we care about this string value
    if bit == 'break':
        break # Avoid inserting 'break' into binary[]

    ## ERROR HANDLING
    # More can be read here: https://docs.python.org/3/tutorial/errors.html
    try:
        bit = int(bit) # Convert string bit to int

        # ERROR CASE[2]: Not 1 or 0
        if bit not in VALUES:
            print('ERROR[2] Must be 1 or 0 (enter break to finish string)')

        # BASE CASE
        else:
            binary.insert(0, bit) # Places bit in first position of binary string [0 -> (1)0, 1010 -> (0)1010, ...]
            print('String now looks like: {0}\n'.format(binary)) # No, it reall is that easy to print a list

    # ERROR CASE[1]: String entered
    except ValueError:
        print('ERROR[1]: Must be a number, not a string (enter break to finish string')


### For Loop
# Will start and conclude in pre defined condition
#       -> len() built in method used to find length of list
#           ex.
#           > a = [1, 2, 3, 4]
#           > len(a) # 4  
for i in range(len(binary)):
    # Get current bit 
    bit = binary[i]

    # If bit is 0, ignore
    if bit == 0:
        continue # Will advance to next loop iteration

    # Else, compute value and add to result
    else:
        exp = len(binary) - i - 1 # Power to raise 2 to [a=[1,1]; i=0; exp => len-i-1 = 1]
        res = pow(2, exp) # 2 to the power of exp [pow(2,3) -> 2^3]
        decimal += res

### Print final values
## String concatenation, inline for loops, and multi-line formatting

# We want to convert binary list into a nice string to print out
binaryString = ''.join(str(bit) for bit in binary) # NOW WE'RE DOING REAL PYTHON!!! [For Each Loop]

# String Concatenation 
print '-' * 75 # Prints out '' 75 times

# Multi-line formats
# Take advantge of the flexibility offered by whitespace to format line cleanly
print('The binary string: {0}\
       \nThe decimal value: {1} '
       .format(binaryString, decimal)
       )

'''
-- BONUS --
1) While effective, the built in list method insert() we use can be ineffecient
as the size of the list increases [O(N) complexity]. Implement a module-level
Data Structure to hold the binary string before computation [Collections Module Deque]
    - https://docs.python.org/3/library/collections.html#collections.deque

HINT: Will need to import the collections module in your program. How can you generate an instance of
a Deque Class?
~~~~~~~~~~~~~~~~~
2) The for loop we currently use to calculate the decimal value works, but can be made more
clean through the use of a For Each Loop. But we also need to keep a tab on the index, which a basic 
<for thing in List> does not grant. How can you keep track of index in a For Each Loop?

HINT: If you want to grab more than one value from the list (say a bit and its index), you're gonna
need to supply two values to the for loop
'''
