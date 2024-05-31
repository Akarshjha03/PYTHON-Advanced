def nge(arr):
  result = [-1] * len(arr)
  stack = []

  for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
      index = stack.pop()
      result[index] = arr[i]
    stack.append(i)
  return result

arr = [1, 12, 3, 8, 10]
result = nge(arr)
print("original", arr)
print("next greater element", result)
