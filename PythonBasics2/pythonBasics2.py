# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
    return int(n / 3)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  word = len(s)
  x = 1
  y = 1
  char_w = s[0]
  for i in range(0, word - 1):
    if s[i] == s[i + 1]:
      x += 1

    else:
      if x > y:
        y = x
        char_w = s[i]
      x = 1
  if x > y:
    y = x
    char_w = s[i]
  return char_w

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  i = 0
  j = len(s) - 1
  if i <= j:
    if s[i] == ' ':
      i += 1
    if s[j] == ' ':
      j -= 1
    if s[i].lower() != s[j].lower():
      return False
    i += 1
    j -= 1
  return True
