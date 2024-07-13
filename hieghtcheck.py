def heightChecker( heights: list[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                ans += 1
        return ans

print(heightChecker([5,1,2,3,4]))