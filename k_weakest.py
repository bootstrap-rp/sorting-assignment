def k_weakest_rows(mat, k):
  strengths = []
  for i in range(len(mat)):
    strength = 0
    for j in range(len(mat[i])):
      if mat[i][j] == 1:
        strength += 1
      else:
        break
    strengths.append((strength, i))

  strengths.sort()
  return [i for _, i in strengths[:k]]

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3
weakest_rows = k_weakest_rows(mat, k)
print(weakest_rows)