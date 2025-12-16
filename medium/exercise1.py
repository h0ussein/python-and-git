# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero.
#  Input : [-1,0,1,2,-1,-4] Output : [[-1, -1, 2], [-1, 0, 1]] Note : Find the unique triplets in the array.

def three_sum(nums):
    nums.sort() 
    result = []

    for i in range(len(nums)): #first we take the first element and try with the bottom loops numbers
        for j in range(i + 1, len(nums)): # here we take the second number and then the third..
            for k in range(j + 1, len(nums)): # here the same als take the third and continuie....
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in result:  # Avoid duplicate triplets
                        result.append(triplet) # here we add the triple to result if there are many triple

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
