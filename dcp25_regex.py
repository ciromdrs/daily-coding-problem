'''Implement regular expression matching with the following special
characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.

For example, given the regular expression "ra." and the string "ray",
your function should return true. The same regular expression on the
string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function
should return true. The same regular expression on the string "chats"
should return false.'''

def isnullable(pattern):
    # assuming well-formed patterns, a pattern is nullable if every
    # single character is nullable, i.e. is followed by an *
    for i in range(0,len(pattern),2):
        if pattern[i] != '*':
            return False
    return True

def match(pattern, string):
    empty_pattern = pattern == ''
    empty_string  = string == ''
    
    if empty_string or empty_pattern:
        if empty_string and empty_pattern:
            return True
        elif empty_string and isnullable(pattern):
            return True
        else:
            return False

    i = 0
    j = 0
    while i < len(string) and j < len(pattern):
        c = string[i]
        p = pattern[j]

        if p == '.' or p == c:
            i += 1
            j += 1
        elif p == '*':
            p_1 = pattern[j-1]
            if p_1 == '.' or p_1 == c:
                i += 1
            else:
                return False
        else:
            return False
    return i == len(string)


print('match("ra.", "ray") =',match("ra.", "ray"))
print('match("ra.", "raymond") =',match("ra.", "raymond"))

print('match(".*at", "chat") =',match(".*at", "chat"))
# I believe it is correct for this next call to return true since, by
# the given definition, .* matches zero or more characters of any
# single character, what means any string
print('match(".*at", "chats") =',match(".*at", "chats"))

print('match("","") =', match('',''))
print('match("foo","") =', match("foo",""))
print('match("","foo") =', match("","foo"))
