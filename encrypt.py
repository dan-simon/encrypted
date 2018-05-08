import sys

if sys.version_info < (3, 6, 0):
    raise Exception('Use Python 3!!! Otherwise you will lose your file!')

def encrypt(s, key):
    s = list(s)
    for i in range(100000):
        o = ord(key[i % len(key)])
        s[(o + i) % len(s)], s[(o - i) % len(s)] = \
        s[(o - i) % len(s)], s[(o + i) % len(s)]
    return ''.join(s)

def decrypt(s, key):
    s = list(s)
    for i in reversed(range(100000)):
        o = ord(key[i % len(key)])
        s[(o + i) % len(s)], s[(o - i) % len(s)] = \
        s[(o - i) % len(s)], s[(o + i) % len(s)]
    return ''.join(s)

if len(sys.argv) < 2:
    raise Exception('Pass the file as an argument.')

with open(sys.argv[1]) as f:
    s = f.read().strip()

with open(sys.argv[1], 'w') as f:
    f.write(encrypt(s, input('> ')))

'''
with open('save_3.txt') as f:
    s = f.read().strip()

with open('save_3.txt', 'w') as f:
    f.write(encrypt(s, input('> ')))
'''

'''

with open('save_3.txt') as f:
    s = f.read().strip()

print(len(s))

# The key is a 15-character string made of 2, 4, 6, 7, and 8. Which one, is the question.

# Can you figure it out?

key = '246782467824678'

print(decrypt(s, key))

'''
