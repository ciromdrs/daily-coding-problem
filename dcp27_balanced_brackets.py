'''Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.'''

def eat(symbol, string):
    global i
    if i < len(string):
        if string[i] == symbol:
            i += 1
            return True
    return False

def B(string): # start symbol for balanced grammar
    if i == len(string):
        return True          # B -> ''
    elif string[i] == '(':   # B -> ( B )
        return eat('(', string) and B(string) and eat(')', string) and B(string)
    elif string[i] == '{':   # B -> { B }
        return eat('{', string) and B(string) and eat('}', string) and B(string)
    elif string[i] == '[':   # B -> [ B ]
        return eat('[', string) and B(string) and eat(']', string) and B(string)
    else:                    # B -> ''
        return True



s = "([])[]({})"
i = 0
print(B(s))

s = "([)]"
i = 0
print(B(s))

s = "((()"
i = 0
print(B(s))
