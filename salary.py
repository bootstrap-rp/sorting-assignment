def average( salary: list[int]) -> float:
         salary.sort()

         s = salary[1:-1]

         m = float(sum(s)/len(s))

         return m
print(average([4000,3000,1000,2000]))