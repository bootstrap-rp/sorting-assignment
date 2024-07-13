def sortColors(nums: list[int]) -> None:
           n=len(nums)
           for i in range(n-1):
              for j in range(i+1,n):
                 if(nums[i]>nums[j]):
                     nums[i],nums[j]=nums[j],nums[i]
           return nums         

print(sortColors([2,0,2,1,1,0]))     