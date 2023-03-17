import random
import time
from quickSort import sortQS
from binaryTree import Node, buildTree, middleElements

# --- GENERATE RANGES ---
n = 1
startNumber = 1000
dataRange = [x for x in range(startNumber, startNumber + (n - 1) * 1000 + 1, 1000)]


# --- TEMPLATE ---
tempData = [
  {
    "name": "elements",
    "data": []
  },
  {"name": "time_tabB",
    "data": []
  },
]


# --- GENERATE DATA ---
for r in dataRange:
    tabA = []
    while len(tabA) < r:
      el = random.randint(1,r)
      if el not in tabA: 
        tabA.append(el)
  
    # --- Time measure - making a copy and sorting (QS) ---
    startSort = time.time()  
    tabB = tabA.copy()
    sortQS(tabB, 0, len(tabB) - 1)
    resultSort = time.time() - startSort
