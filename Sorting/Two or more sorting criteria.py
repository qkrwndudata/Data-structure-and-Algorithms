#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))
    
array = sorted(array, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in array:
    print(student[0], end = '\n')

