#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:
def arrayCheck(nums):
    # CODE GOES HERE
    for num in nums:
        if num != 1 and num != 2 and num != 3:
            state = 'False'
            break
        else:
            state = 'True'
    print(state)

# arrayCheck([1, 1, 2, 3, 1])
# # → True
# arrayCheck([1, 1, 2, 4, 1])

# arrayCheck([1, 1, 2, 1, 2, 3])


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:


def stringBits(str):
    # CODE GOES HERE
    return str[::2]


stringBits('Hello')
stringBits('Hi')
stringBits('Heeololeo')

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#


def end_other(a, b):
    # CODE GOES HERE
    a = a.lower()
    b = b.lower()

    return (b.endswith(a) or a.endswith(b))


end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')
end_other('abc', 'abXabc')

#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'


def doubleChar(str):
    # CODE GOES HERE
    1+1
    #####################
    ## -- PROBLEM 5 -- ##
    #####################

    # Read this problem statement carefully!

    # Given 3 int values, a b c, return their sum. However, if any of the values is a
    # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
    # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
    # takes in an int value and returns that value fixed for the teen rule.
    #
    # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    # Define the helper below and at the same indent level as the main no_teen_sum().
    # Again, you will have two functions for this problem!
    #
    # Examples:
    #


def fix_teen(n):
    if 12 < n < 15 or 16 < n < 19:
        n = 0
        return n
    else:
        return n


def no_teen_sum(a, b, c):
    sum = fix_teen(a) + fix_teen(b) + fix_teen(c)
    print(sum)
    # CODE GOES HERE


no_teen_sum(1, 2, 3)
no_teen_sum(2, 13, 1)
no_teen_sum(2, 1, 14)

# CODE GOES HERE

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0


def count_evens(nums):
  count = 0
  for num in nums:
    if num%2 == 0:
      count += 1
  print(count)
    # CODE GOES HERE

count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])
