def findRelativeRanks(score: list[int]) -> list[str]:
        temp = sorted(score, reverse=True) 
        d = {}

        for i in range(len(temp)):
            if i == 0:
                d[temp[i]] = "Gold Medal"
            elif i == 1:
                d[temp[i]] = "Silver Medal"
            elif i == 2:
                d[temp[i]] = "Bronze Medal"
            else:
                d[temp[i]] = str(i + 1)

        score = [d[i] for i in score]

        return score

print(findRelativeRanks([5,4,3,2,1]))