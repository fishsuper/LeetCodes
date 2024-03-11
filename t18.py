# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] 
# （若两个四元组元素一一对应，则认为两个四元组重复）


## 直接for循环查找，时间复杂度太高，超出时间限制
def fourSum(nums: list[int], target: int) -> list[list[int]]: 
        B = []
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    for l in range(k+1,n):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            a = [nums[i],nums[j],nums[k],nums[l]]
                            a.sort()
                            B.append(a)
        return B

A = [-1,1,-2,2,0,0,-3,3,5,-5,8,-8]
target = 0

output = fourSum(nums=A, target=0)

print('循环查找FourSum：', output)

## 理解以下代码的区别
a = [1,-1]
a.sort()
print(a)
# 而下面代码会输出none
a = [1,-1]
b = a.sort()
print(b)


## 避免重复元素，利用continue，复杂度仍然过高
num = [2,2,-2,2,2,-2]

num.sort()

print(num)

def fourSum2(nums: list[int], target: int) -> list[list[int]]: 
        nums.sort()
        B = []
        n = len(nums)
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,n):
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    for l in range(k+1,n):
                        if l>k+1 and nums[l]==nums[l-1]:
                            continue
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            #a = [nums[i],nums[j],nums[k],nums[l]]
                            #a.sort()
                            B.append([nums[i],nums[j],nums[k],nums[l]])
        return B

print('避免重复元素的查找：', fourSum2(num, 0))

## 低复杂度算法？双指针
def fourSum0(nums: list[int], target: int) -> list[list[int]]:
        quadruplets = list()
        if not nums or len(nums) < 4:
            return quadruplets
        
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        
        return quadruplets

print('双指针算法函数：', fourSum0(num, 0))

