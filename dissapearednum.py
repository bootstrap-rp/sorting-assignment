def find_disappeared_numbers(nums):
  n = len(nums)
  nums_set = set(nums)
  disappeared_nums = []

  for i in range(1, n + 1):
    if i not in nums_set:
      disappeared_nums.append(i)

  return disappeared_nums

nums = [4, 3, 2, 7, 8, 2, 3, 1]
disappeared_nums = find_disappeared_numbers(nums)
print(disappeared_nums)