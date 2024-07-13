def specialArray(nums: list[int]) -> int:
        nums.sort()
        
        for i in range(len(nums), 0, -1):
            low = 0 
            high=len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < i:
                    low = mid + 1
                else:
                    high = mid - 1
            if len(nums) - low == i:
                    return i
        return -1

print(specialArray([3,5]))