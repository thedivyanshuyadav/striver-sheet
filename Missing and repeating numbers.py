def missingAndRepeating(arr, n):
  """
  Problem : https://www.codingninjas.com/codestudio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
  """
  n = arr.__len__()
  vect = [0]*n
  for i in range(n):
      vi = arr[i] - 1 
      if vect[vi] < 0:
          a = arr[i]
      vect[vi] = -1

  for x in range(n):
      if vect[x]==0:return x+1,a
