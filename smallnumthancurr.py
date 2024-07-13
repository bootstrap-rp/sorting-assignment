def Current(nums: list[int]) -> list[int]:
        dic = {}
        s = sorted(nums)
        i=0
        while i < len(s):
            if i>0 and s[i-1]==s[i]:
                i+=1
            else:
                dic[s[i]] = i
                i+=1
        res = []
        for num in nums:
            res.append(dic[num])
        return res

print(Current([6,5,4,8]))