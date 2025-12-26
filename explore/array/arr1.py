"""
1929. 数组串联
已解答
简单
相关标签
premium lock icon
相关企业
提示
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

返回数组 ans 。

示例 1：
输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

示例 2：
输入：nums = [1,3,2,1]
输出：[1,3,2,1,1,3,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""


from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    # length = len(nums)
    # arr = [0] * (length*2)
    # for i in range(length):
    #     arr[i] = nums[i]
    #     arr[i + length] = nums[i]
    # return arr
    #解法1
    return nums.extend(nums)
    #解法2
    return nums*2


if __name__ == '__main__':
    nums = [1,2,1]
    arr=getConcatenation(nums)
    print(arr)