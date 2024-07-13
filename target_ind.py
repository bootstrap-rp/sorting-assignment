def target_indices(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            while left < mid and nums[left] == target:
                left += 1
            while right > mid and nums[right] == target:
                right -= 1

            return list(range(left, right + 1))

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return []

nums = [1, 2, 3, 3, 3, 5, 7, 9]
target = 3
indices = target_indices(nums, target)
print(indices)