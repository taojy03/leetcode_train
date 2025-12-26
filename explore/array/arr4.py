"""
645.错误的集合
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。
给定一个数组 nums 代表了该集合发生错误后的结果。
请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""

from typing import List
#法一：数学法,通过集合求解
def findErrorNums1(nums: List[int]) -> List[int]:
    total = sum(range(1, len(nums) + 1))
    num1 = sum(set(nums))
    num2 = sum(nums)
    repeat = num2 - num1
    lose = total - num1
    return [repeat, lose]

#法二：循环数组法，先排序，两端单独看，中间数值差
def findErrorNums2(nums: List[int]) -> List[int]:
    arr = [0] * 2
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            arr[0] = nums[i]
        if nums[i + 1] - nums[i] == 2:
            arr[1] = nums[i] + 1

    if nums[-1] != len(nums):
        arr[1] = len(nums)
    if nums[0] != 1:
        arr[1] = 1

    return arr

#法3：哈希表法，统计 nums 序列中每个元素出现的次数，返回一个计数字典（Counter 对象）
def findErrorNums3(nums: List[int]) -> List[int]:
    from collections import Counter
    dict = Counter(nums)
    for i in range(1, len(nums) + 1):
        num = dict.get(i, 0)
        if num == 2:
            repeat = i
        if num == 0:
            lose = i
    return [repeat, lose]


if __name__ == '__main__':
    nums = [37,62,43,27,12,66,36,18,39,54,61,65,47,32,23,2,46,8,4,24,29,38,63,39,25,11,45,28,44,52,15,30,21,7,57,49,1,59,58,14,9,40,3,42,56,31,20,41,22,50,13,33,6,10,16,64,53,51,19,17,48,26,34,60,35,5]
    findErrorNums1(nums)
    print(findErrorNums1(nums))
    findErrorNums2(nums)
    print(findErrorNums2(nums))
    findErrorNums3(nums)
    print(findErrorNums3(nums))