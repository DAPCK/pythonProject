#s = 'C:\d\new.txt'
# print(s) не працює через переноси
# s = r'C:\d\new.txt'
# print(s) r - robust string
# s = 'Py' 'thon'
# print(s)
# - зклеювання строк

# s1 = 'Hello, '
# s2 = 'world!'
# s3 = s1 + s2
# print(s3)
# "+" - конкатинація строк

# name = 'John'
# age = 20
# print('My name is ' + name + " I'm " + str(age))
# змінна "age" переведена з int в строку (str) тому що не можна додавати текст і число

#print('hi ' * 5)
# "* 5" - кількість разів виведення строки тобто ми отримаємо 5 раз "hi"
# s = 'Hello world!'
# print(s[0])
# print(s[-12])
# [] - индексація символів тобто [0] виводить перший символ Н оскільки нумерація з 0
# а [-12] виводить також Н оскільки в фразі лише 12 символів і зі знаком "-"
# відлік починається з кінця фрази а тому починається не з "0" а з "-1"
#s[0] = 'D' - немає можливості переписати перший символ через те що тип str є незмінним

'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2 -1
'''
#[X:Y:Z] - оператор зрізу не всі переметри обовязкові початок,кінець, шаг зрізу
s = 'Hello world!'

print(s[0:12]) #Hello world!
print(s[-1]) #!
print(s[0:5]) #Hello
print(s[:5]) #Hello
print(s[6:]) #world!
print(s[::2]) #Hlowrd
print(s[::-1]) #!dlrow olleH
print(s[:5] + s[6:]) #Helloworld!