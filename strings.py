'''
Created on 21 июн. 2019 г.

@author: m.elagina
'''
def string_test():
    a = 'asd'   
    b = 'fgh'
    c = a+b
    d = 'qwe'
    d *=3
    print(d, len(d))
    print('asd' == "asd")
    print('ac' > "acv")#сравнение как порядок в словаре, то, что раньше в ловате, то меньше
    print('a\nnewline')
def task1():
    print("239" < "30" and 239 < 30)
    print("239" < "30" and 239 > 30)
    print("239" > "30" and 239 < 30)
    print("239" > "30" and 239 > 30)       
# string_test()    
print("123" + "42") 