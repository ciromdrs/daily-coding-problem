'''Write an algorithm to justify text. Given a sequence of words and an
integer line length k, return a list of strings which represents each
line, fully justified.

More specifically, you should have as many words as possible in each
line. There should be at least one space between each word. Pad extra
spaces when necessary so that each line has exactly length k. Spaces
should be distributed as equally as possible, with the extra spaces, if
any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-
hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox",
"jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the
following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

def justify(line,k):
    n = k - linelen(line) # n is the number of spaces to be added
    if len(line) == 1: # single word, add right padding
        return line[0] + ' '*n

    i = 0
    while n > 0:
        line[i] += ' '
        n -= 1
        i = (i+1) % (len(line)-1)
    res = line[0]
    for w in line[1:]:
        res += ' ' + w
    return res

def linelen(l):
    length = 0
    if len(l) > 0:
        length += len(l[0])
        for w in l[1:]:
            length += 1+len(w)
    return length

words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
    "dog"]
k = 16

line = [] # auxiliar
res  = [] # resulting justified text
for w in words:
    if len(w) + linelen(line) > k:
        res += [line]
        line = []
    line += [w]
if line != []:
    res += [line]

for i in range(len(res)):
    res[i] = [justify(res[i],k)]

for line in res:
    print(line)
