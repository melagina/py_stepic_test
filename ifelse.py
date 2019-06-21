'''
Created on 21 июн. 2019 г.

@author: m.elagina
'''
def division():
    a=  4   
    b = 5
    m = a
    if b  > m:
        m = b
    print(m)    
def zero_division():
    a = int(input())
    b = int(input())
    if b != 0:    
        print(a/b)
    else:
        print("division impossible")    
        b = int(input('input not nullable denominator'))
        if b == 0:
            print("error! you donkey cannot insert anything but zero")
        else:    
            print(a/b)
def task1():
    a = int(input())
    b = int(input())
    h = int(input())
    if a>b:
        print("неверные данные")
        return             
    if a <= h <= b:
        print("Это нормально")    
    elif h < a:
        print("Недосып")
    else:
        print("Пересып")
def task2():
    n = int(input())
    if n < 1900 or n > 3000:
        return
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print('Високосный')
    else:    
        print('Обычный')
task2()        
        
        