# -*- coding: utf-8 -*-
"""Day 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-DQNzWchLrWQzrfY_T8EJuJt-dNgOpo8
"""

a="Ayesha"
print(a)
print(a[3:])
print(a[:-3])

x=7
print(type(x))
print(type(9.07))
y=float(x)
print(y)
print(type(y))
z=str(x)
print(z)
print(type(z))

str='welcome to python programming'
for i in str:
  print(i)

print(str)
print('python' in str)

num=1
while(num<10):
  print(num)
  num=num+1

num=10
while(num>0):
  print(num)
  num=num-1

for i in range(1,10,2):
  print(i)

for i in range(10,0,-1):
  print(i)