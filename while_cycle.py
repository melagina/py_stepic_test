'''
Created on 27 июн. 2019 г.

@author: m.elagina

'''
from builtins import int

def task1():
    a = 5
    while a > 0:
        print(a, end=' ')
        a -= 1

def task2():
    i = 0
    counter = 0
    while i <= 10:
        counter += 1
        i = i + 1
        if i > 7:
            i = i + 2
    print(i)
    print(counter)
def task3():
    c = 1
    while c<=6:
        print('*' * c)
        c += 1
def task4():
    i = 0
    while i < 5:
        print('*')
        if i % 2 == 0:
            print('**')
        if i > 2:
            print('***')
        i = i + 1
def task5():
    s = 0
    i = 0
    while i<=1:
        s += i
        i +=1
    print(s)    
    
def task6():
    a = int(input())
    s = a
    while a != 0:
        a = int(input())
        s += a
    print(s) 
def task61():
    s, n = 0, int(input())
    while n:
        s, n = s + n, int(input())
    print(s)
def task62():
    a = int(input())
    s = 0
    while a != 0 :
        s += a
        a = int(input())
    print(s)    
def task7():
    a = int(input())   
    b = int(input())
    if a < b:
        a, b = b, a
    i = 1
    while (a*i)%b != 0:
       i += 1 
    print(a*i)   
def task71():
    a, b = int(input()),int(input())      
    if a < b:
        a, b = b, a
    i = a
    while i % b != 0: i += a
    print(i)     
def task7_evklid():
#     алгоритм евклида
    a,b=int(input()),int(input())
    ab=a*b
    while b!=0:
        a,b=b,a%b
    out=ab//a
    print(out)    
            
       
task7()
