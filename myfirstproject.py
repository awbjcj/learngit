from functools import reduce

'''def mul(x, *nums):
    p = x
    for n in nums:
         p = p * n
    return p
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')'''

'''def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else :
        move(n-1, a, c, b)    
        move(1, a, b, c)
        move(n-1, b, a, c)
move(4, "A", "B", "C")'''
'''def trim(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    else:
        return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')'''

'''def triangles():
    init = [1]
    while True:
        yield init
        output = [init[i] + init[i+1] for i in range(len(init)-1)]
        init = [1] + output + [1]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')'''

'''def normalize(name):
    char_ord = list(map(ord, name))
    if char_ord[0] > 96:
        char_ord[0] -= 32
    char_ch = chr(char_ord[0])
    for ch in [x + 32 if x < 97 else x for x in char_ord[1:]]:
        char_ch += chr(ch)
    return char_ch

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)'''

'''def prod(L):
    return reduce(lambda x,y:x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')'''

def convert(ch):
    return ord(ch)-48

def str2float(s):
    pos = s.find(".")
    bigger_than_zero = list(map(convert, s[0:pos]))
    smaller_than_zero = list(map(convert, s[pos+1:]))
    return reduce(lambda x,y:10*x+y, bigger_than_zero) + reduce(lambda x,y:10*x+y, smaller_than_zero)*0.1**(len(smaller_than_zero))


print('str2float(\'114.514\') =', str2float('114.514'))
if abs(str2float('114.514') - 114.514) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')