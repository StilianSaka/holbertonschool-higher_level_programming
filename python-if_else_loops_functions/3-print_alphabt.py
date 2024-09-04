#!/usr/bin/python3
chars = ''.join(
    chr(i) for i in range(97, 123) if chr(i) not in {'q', 'e'}
)
print('{}'.format(chars), end='')
