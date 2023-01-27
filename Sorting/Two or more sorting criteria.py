#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# 출처: https://www.acmicpc.net/problem/10825

# 문제 소개: 학생 N명의 이름과 국어, 영어, 수학 점수에 대해 국어는 감소하는 순서대로, 영어는 증가하는 순서대로, 수학은 감소하는 순서대로, 
# 모든 점수가 같으면 이름 순으로 정렬하는 코드를 작성하시오


n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))
    
array = sorted(array, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for student in array:
    print(student[0], end = '\n')

