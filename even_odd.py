def sortEvenOdd(nums: list[int]) -> list[int]:
           even = []; odd = []; ans =[]
           for i in range(len(nums)):
             if(i%2==0):
                even.append(nums[i])
             else: odd.append(nums[i])
           even.sort()
           odd.sort(reverse=True)
           for i in range(len(odd)):
             ans.append(even[i])
             ans.append(odd[i])
           if(len(nums)>len(ans)):
             ans.append(even[-1])
           return ans

print(sortEvenOdd([4,1,2,3]))