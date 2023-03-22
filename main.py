from quickSort import sortQS
from searchFunctions import *
from binaryTree import *
from array import array
import random
import time
import json
import xlsxwriter

# --- GENERATE RANGES ---
n = 5
startNumber = 1000
dataRange = [x for x in range(startNumber, startNumber + (n - 1) * 1000 + 1, 1000)]


# --- TEMPLATES ---
tempC = [
  {
    "name": "elements",
    "data": []
  },
  {
    "name": "timeCB",
    "data": []
  },
  {
    "name": "timeCTA",
    "data": []
  },
  {
    "name": "timeCTB",
    "data": []
  }
]

tempS = [
  {
    "name": "elements",
    "data": []
  },
  {
    "name": "timeSA",
    "data": []
  },
  {
    "name": "timeSB",
    "data": []
  },
  {
    "name": "timeSTA",
    "data": []
  },
  {
    "name": "timeSTB",
    "data": []
  }
]

tempH = [
  {
    "name": "elements",
    "data": []
  },
  {
    "name": "heightTA",
    "data": []
  },
  {
    "name": "heightTB",
    "data": []
  }
]


# --- GENERATE DATA ---
for r in dataRange:
  tabA = array('i', [])
  while len(tabA) < r:
    el = random.randint(1, r)
    if el not in tabA: 
      tabA.append(el)

  # --- (2) Making a copy and sorting (QS) ---
  startSortcopy = time.time()
  tabB = array('i', [t for t in tabA])
  sortQS(tabB, 0, len(tabB) - 1)
  resultSortcopy = time.time() - startSortcopy

  # --- (2) Run directSearch for tabA and binarySearch for tabB ---
  startDirectS = time.time()
  for key in tabB:
    directSearch(tabA, key)
  resultDirectS = time.time() - startDirectS

  startBinaryS = time.time()
  for key in tabA:
    binarySearch(tabB, key)
  resultBinaryS = time.time() - startBinaryS

  # --- (3) Build tree base tabA, height and search time measure ---
  # - Build -
  startTreeA = time.time()
  treeA = buildTree(tabA)
  resultTreeA = time.time() - startTreeA
  # - Height -
  heightA = treeA.height()
  # - Search -
  startSearchA = time.time()
  for el in tabA:
    treeA.find(el)
  resultSearchA = time.time() - startSearchA

  # --- (4) Build tree base tabB, height and search time measure ---
  # - Prepare -
  tabB2temp = array('i', [t for t in tabB])
  tabB2 = array('i', [])
  middleElements(tabB2temp, tabB2)
  # - Build -
  startTreeB = time.time()
  treeB = buildTree(tabB2)
  resultTreeB = time.time() - startTreeB
  # - Height -
  heightB = treeB.height()
  # - Search -
  startSearchB = time.time()
  for el in tabA:
    treeB.find(el)
  resultSearchB = time.time() - startSearchB

  # --- Insert collected data to JSON ---
  # - Elements -
  tempC[0]["data"].append(r)
  tempS[0]["data"].append(r)
  tempH[0]["data"].append(r)
  # - Creating -
  tempC[1]["data"].append(resultSortcopy) #CB
  tempC[2]["data"].append(resultTreeA) #CTA
  tempC[3]["data"].append(resultTreeB) #CTB
  # - Searching -
  tempS[1]["data"].append(resultDirectS) #timeSA
  tempS[2]["data"].append(resultBinaryS) #timeSB
  tempS[3]["data"].append(resultSearchA) #timeSTA
  tempS[4]["data"].append(resultSearchB) #timeSTB
  # - Height -
  tempH[1]["data"].append(heightA) #heightTA
  tempH[2]["data"].append(heightB) #heightTB
  

# --- JSON DATA ---
with open("tempC.json", "w", encoding="utf-8") as file:
    json.dump(tempC, file, indent=2)
  
with open("tempS.json", "w", encoding="utf-8") as file:
    json.dump(tempS, file, indent=2)
  
with open("tempH.json", "w", encoding="utf-8") as file:
    json.dump(tempH, file, indent=2)


# --- EXCEL FILE ---
workbook = xlsxwriter.Workbook("results-excel.xlsx")

wsCreate = workbook.add_worksheet("create")
for idx, t in enumerate(tempC):
  wsCreate.write(0, idx, t["name"])
  for i in range(len(t["data"])):
    wsCreate.write(i+1, idx, t["data"][i])

wsSearch = workbook.add_worksheet("search")
for idx, t in enumerate(tempS):
  wsSearch.write(0, idx, t["name"])
  for i in range(len(t["data"])):
    wsSearch.write(i+1, idx, t["data"][i])

wsHeight = workbook.add_worksheet("height")
for idx, t in enumerate(tempH):
  wsHeight.write(0, idx, t["name"])
  for i in range(len(t["data"])):
    wsHeight.write(i+1, idx, t["data"][i])

workbook.close()