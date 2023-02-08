# -*- coding: utf-8 -*-
"""binary search3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17-cxtoTzbxm75TTbfivxVr61oRDD5e_U
"""
# LeetCode: 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

## Given two integer arrays nums1 and nums2, return an array of their intersection. 
## Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in set(nums1):
            if i in nums2:
                answer.append(i)
        return answer
    
# 더 짧은 풀이 by 유경
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
