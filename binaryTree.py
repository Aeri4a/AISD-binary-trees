
# --- Binary Tree Object ---
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                self.right.find(value)
        else:
            return True
        
    def height(self):
        leftHeight = 0 if self.left is None else self.left.height()
        rightHeight = 0 if self.right is None else self.right.height()
        return max(leftHeight, rightHeight) + 1

# --- Building Trees ---
def buildTree(array):
  tree = Node(array[0])
  for i in array[1:]:
    tree.insert(i)
  return tree

# --- Preparing array in middle elements order ---
def middleElements(array, output):
  if array != []:
    middleID = len(array)//2
    middle = array[middleID]
    output.append(middle)
    left = array[:middleID]
    right = array[middleID+1:]
    middleElements(left, output)
    middleElements(right, output)