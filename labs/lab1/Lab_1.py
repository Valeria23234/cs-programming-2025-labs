# 1
a = 0
b = 'l'
c = False
d = 2.5

# 2
name = 'Lera'
age = 22
print(name, age)

# 3
q = 342
w = 56.2
e = '43'

result = q + w + int(e)
print(result)

# 4
a = 3
b = 8
result = (a + 4 * b) * (a - 3 * b) + a ** 2
print(result)

# 5
lenth = int(input())
width = int(input())

R = 2 * (lenth + width)
T = lenth * width

print(R, T)


#6
print("*   *   *\n"
      " * * * *\n"
      "  *   *   ")


#7
Y = 89
U = 2
print(Y > U)
print(Y < U)
print(Y == U)
print(Y >= U)
print(Y <= U)
print(Y != U)

print(Y + U)
print(Y - U)
print(Y * U)
print(Y / U)
print(Y // U)
print(Y ** U)
print(Y % U)


#8
name = 'Лера'
age = 22
print(f'Меня зовут {name}, мне {age} лет.')

#9
z = 'Съешь еще '
x = 'этих мягких '
c = 'французских булок, '
v = 'да выпей '
b = 'чаю.'
print(z + x + c + v + b)


#10
m = 'Нет! Да! '
print(m * 4)


#11
a,s,d = input().split(',')
result = (int(a) + int(d))// int(s)
print('Результат вычисления : ', result)

#12
text = input()
print(text)
print(text[:4])
print(text[-2:])
print(text[4:8])
print(text[::-1])
