"""
485.最大连续的1
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

示例 1：
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:
输入：nums = [1,0,1,1,0,1]
输出：2

提示：
1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
"""
from typing import List
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # max = 0
    # k = 0
    # for i in range(len(nums)):
    #     if nums[i] == 1:
    #         k += 1
    #     if i < len(nums) - 1:
    #         if nums[i + 1] != 1:
    #             if k > max:
    #                 max = k
    #             k = 0
    # if k > max:
    #     max = k
    # return max

# [1,1,1,0,0]  前缀和算法（计算相连值是多少）
# 原始数据【1，1，1，0，1，1】
# 前缀和后【1，2，3，0，1，2】
    m = count = 0
    for x in nums:
        if x:
            count += 1
            m = max(m,count)
        else:
            count = 0
    return m

if __name__ == '__main__':
    nums = [0,1]
    print(findMaxConsecutiveOnes(nums))