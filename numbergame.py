def numberGame( nums: list[int]) -> list[int]:
        ans=[]
        nums.sort()
        while len(nums):
            if len(nums)==1:
                ans.append(nums[0])
                break
            ans.extend([nums[1],nums[0]])
            nums=nums[2:]
        return ans

print(numberGame([2,5]))