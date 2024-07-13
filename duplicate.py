def find_duplicate(nums):
  n = len(nums)
  slow = 0
  fast = 0

  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]

    if slow == fast:
      break

  slow = 0

  while slow != fast:
    slow = nums[slow]
    fast = nums[fast]

  return slow

nums = [1, 3, 4, 2, 2]
duplicate = find_duplicate(nums)
print(duplicate)