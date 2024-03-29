# -*- coding: utf-8 -*-
"""LeetcodeTwoSumSolution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RB6TEq4SfsKegGsWaNbpleNxILUcPCiQ
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        for i, number in enumerate(nums):
            if target - number in check:
                return check[target - number], i
            check[number] = i