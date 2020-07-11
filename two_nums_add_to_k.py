def two_numbers(nums, k):

    second_number = 0

    for index in range(len(nums)-1):
        if (k - nums[index]) in nums[index+1:]:
            second_number = k-nums[index]
            print(nums[index], second_number)
            return True
    
    return False
        
nums = [10, 15, 3, 7]

print(two_numbers([10, 15, 3, 7], 22))