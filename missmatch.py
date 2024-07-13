def missmatch(nums):
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  expected_sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
  actual_sum_of_squares = sum(num ** 2 for num in nums)

  duplicate = (actual_sum - expected_sum) // 2
  missing = (expected_sum_of_squares - actual_sum_of_squares) // 2 + duplicate

  return [duplicate, missing]

nums = [5, 4, 3]
duplicate, missing = missmatch(nums)
print(duplicate, missing)
 