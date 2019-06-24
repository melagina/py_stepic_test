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
    if a < b:
        max = b
        mid = a    
    
    print(max,'\n', min,'\n', mid)
       
task51()