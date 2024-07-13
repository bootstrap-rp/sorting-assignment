def find_duplicates(nums):
  n = len(nums)
  duplicates = []

  for num in nums:
    index = abs(num) - 1
    if nums[index] < 0:
      duplicates.append(abs(num))
    else:
      nums[index] *= -1

  return duplicates

nums = [4,3,2,7,8,2,3,1]
duplicates = find_duplicates(nums)
print(duplicates)
