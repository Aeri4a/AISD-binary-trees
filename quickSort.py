
# --- Quick Sort (middle pivot) ---
def partitionQS(tab, p, r):
  pivot = tab[(p + r) // 2]
  i = p - 1
  j = r + 1
  while True:
    i += 1
    while tab[i] < pivot:
      i += 1
    j -= 1
    while tab[j] > pivot:
      j -= 1
    if i >= j:
      return j
    tab[i], tab[j] = tab[j], tab[i]

def sortQS(tab, p, r):
  if p < r:
    sub_tab = partitionQS(tab, p, r)
    sortQS(tab, p, sub_tab)
    sortQS(tab, sub_tab + 1, r)
