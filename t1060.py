# t1060 给出一个有序数组 A，数组中的每个数字都是 独一无二的，找出从数组最左边开始的第 K 个缺失数字

def KthMissingNumber(A, K):
    headNumber = A[0]
    tempNumber = headNumber
    k = 0
    index = 0
    while k < K:
        tempNumber += 1
        if A[index+1] != tempNumber:
            k += 1
        else:
            index += 1
        
    return tempNumber

A = [4, 7, 9, 11, 15, 20]
K = 10

print('The Kth missing number in array A:', KthMissingNumber(A, K))

def KthMissing(A,K):
    n = len(A)
    global index
    for i in range(n):
        if A[i]-A[0]-i > K:
            index = i
            break
    temp = A[index-1]    
    k = A[index-1]-A[0]-(index-1)
    while k < K:
        temp += 1
        k += 1
    return temp

'''
    super_index = len(A)-1
    lower_index = 0
    index = (super_index + lower_index)//2

    while B[index] < K:
        if (A[index]-A[0])-index < K:
            lower_index = index
            index = (super_index + lower_index)//2
        elif (A[index]-A[0])-index > K:
            super_index = index
            index = (super_index + lower_index)//2
    
    return A[index]
    
'''
    
print('The Kth missing number', KthMissing(A,K))

        

