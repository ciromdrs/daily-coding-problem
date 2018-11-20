'''
Run-length encoding is a fast and simple method of encoding strings. The
basic idea is to represent repeated successive characters as a single
count and character. For example, the string "AAAABBBCCDAA" would be
encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to
be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
'''

def encode(string):
    old = ''
    count = 0
    encoded = ''
    char = ''
    for char in string:
        if char == old:
            count += 1
        else:
            if count > 0:
                encoded += str(count) + old
            count = 1
        old = char
    if count > 0:
        encoded += str(count) + char
    return encoded
    
def decode(string):
    decoded = ''
    for i in range(0,len(string),2):
        n = int(string[i])
        c = string[i+1]
        decoded += n*c
    return decoded

print(encode("AAAABBBCCDAA") == "4A3B2C1D2A")
print("AAAABBBCCDAA" == decode("4A3B2C1D2A"))
