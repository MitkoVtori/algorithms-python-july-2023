def calculate_sum(nums):
    total_sum = 0
    if nums:
        total_sum = nums[0] + calculate_sum(nums[1:])
    return total_sum


numbers = list(map(int, input().split()))
print(calculate_sum(numbers))