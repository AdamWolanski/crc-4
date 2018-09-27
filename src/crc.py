def xor(x, y):
    ret = []

    for i in range(1, len(y)):
        if x[i] == y[i]:
            ret.append('0')
        else:
            ret.append('1')

    return ''.join(ret)

def mod2div(x, y):
    size = len(y)
    tmp = x[0:size]
    while size < len(x):
        if tmp[0] == '1':
            tmp = xor(y, tmp) + x[size]
        else:
            tmp = xor('0'*size, tmp) + x[size]
        size += 1

    if tmp[0] == '1':
        tmp = xor(y, tmp)
    else:
        tmp = xor('0'*size, tmp)

    return tmp

def encode(data, key):
    tmp = (''.join(format(ord(x), 'b') for x in data))
    key_size = len(key)
    appended_data = tmp + '0'*(key_size-1)
    remainder = mod2div(appended_data, key)

    return tmp + remainder

'''
tmp_input = 'lalalaaaxx123'
print tmp_input
data = (''.join(format(ord(x), 'b') for x in tmp_input))
print data
key = '1001'

ans = encode(data, key)
print ans

crc = ans[-(len(key)-1):]
print crc
'''

'''
key = '1001'

f = open('text.txt','rb')
file_lines = (sum(1 for line in open('text.txt')))

f2 = open('t1.txt', 'a')
data = f.readline()
ans = encode(data, key)

print ans
crc = ans[-(len(key)-1):]

print crc
f2.write(data.rstrip() + ' ' + crc + '\n')
f2.write(data.rstrip() + ' ' + crc + '\n')

f.close()
f2.close()
'''
