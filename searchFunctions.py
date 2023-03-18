
# --- Direct Linear Search --
def directSearch(array, key):
  for i in range(len(array)):
    if array[i] == key:
      return i
  return -1
  
# --- Binary Search ---
def binarySearch(array, key):
  left = 0
  right = len(array) - 1

  while left <= right:
    mid = (left + right) // 2
    if array[mid] < key:
      left = mid + 1
    elif array[mid] > key:
      right = mid - 1
    else:
      return mid
  return -1