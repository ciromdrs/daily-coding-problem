'''Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character
        alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original
        url. If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?'''

S = {}

def __randstr__():
    c = 1
    while True:
        s = str(c).zfill(6)
        yield s
        c += 1
randstr = __randstr__()

def shorten(url):
    if url not in S:
        S[url] = randstr.__next__()
    return S[url]

def restore(short):
    return S.get(short)

print(shorten('google.com'))
print(shorten('example.com'))
print(shorten('google.com'))
