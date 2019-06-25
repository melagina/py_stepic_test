'''
Created on 24 июн. 2019 г.

@author: m.elagina
'''
def task1():
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))** (1/2)
    print(s)
def task2():
    a = int(input())
    if (-15<a<=12) or (14<a<17) or (a>=19):
        print(True)
    else:
        print(False)
def task3():
    a = float(input())
    b = float(input())
    oper = input()
    if oper == '+':
        print(a+b)
    elif oper == '-':
        print(a-b)
    elif oper == '*':
        print(a*b)
    elif oper == 'pow':
        print(a**b)
    else: 
        if b == 0:
            print('Деление на 0!')
        elif oper == '/':   
            print(a/b)
        elif oper == 'mod':
            print(a%b)
        else:    
            print(a//b)
def task4():
    type=input()
    if type=='треугольник':
        a = float(input())
        b = float(input())
        c = float(input())
        p = (a+b+c)/2
        print((p*(p-a)*(p-b)*(p-c))** (1/2))
    elif type=='прямоугольник':
        a = float(input())
        b = float(input())
        print(a*b)
    elif type=='круг':
        r = float(input())
        print(3.14*(r**2))
def task5():
    a, b, c = int(input()), int(input()), int(input())
    d = a
    if b > a:
        a = b
        b = d
        if c > a:
            d = c
            c = a
            a = d
        if c > b:
            d = c
            c = b
            b = d               
    else:
        if a < c:
            d = c
            c = a
            a = d
        if b < c:
            d = c
            c = b
            b = d        
    print(a,'\n',b,'\n',c)
def task51():
    a, b, c = int(input()), int(input()), int(input())
    max, min, mid = a, b, c
    if max < b:
        max = b
    print(max , min, mid)
    if max < c:   
        max = c
    print(max , min, mid)
    if min > a:
        min = a        
    print(max , min, mid)
    if min > c:
       min = c
    print(max , min, mid)    
    mid = (a+b+c)-(min+max)    
    print(max,'\n', min,'\n', mid)
def task52():
    a,b,c = int(input()), int(input()), int(input())

    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print(a)
    print(b)
    print(c)   

def task6():
    for n in range(0,10):
        print(n)
#     n = int(input())
        if (n == 0) or (n%5 == 0) or (n%10 == 0) or (6 <= n%10 <= 9) or (11 <= n <=19) or (11 <= n%100 <=19):
            print(n, 'программистов')
        elif 2 <= n%10 <= 4:
            print(n, 'программиста')
        else:
            print(n, 'программист')
def task61():
    for n in range(0,20):
        print(n)
#         n = int(input())
        if (n == 1) or ((n%10 == 1) and n != 11 and n%100 != 11):
            print(n, 'программист')
        elif (2 <= n%10 <= 4) and not 12 <= n % 100 <= 14:
            print(n, 'программиста')
        else:
            print(n, 'программистов')
                    
def task7():
    n = int(input())
    a1 = n %10
    a2 = (n//10) % 10
    a3 = (n//100) % 10
    a4 = (n//1000) % 10
    a5 = (n//10000) % 10
    a6 = (n//100000) % 10
    if a1+a2+a3 == a4+a5+a6:
        print("Счастливый")
    else:    
        print("Обычный")
def task71():
    n=int(input())
    print("Счастливый" if n//100000+n//10000%10+n//1000%10==n//100%10+n//10%10+n%10 else "Обычный")        
task7()