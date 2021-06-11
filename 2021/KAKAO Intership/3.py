# U X X만큼 위행
# D X X만큼 밑행
# C 현재 행 삭제하고 아래행, 만약 마지막이라면 위행
# Z 가장 최근에 삭제된행 복구
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST: #Binary Search Tree
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            self.current_node = self.head
            while True:
                if value < self.current_node.value:
                    if self.current_node.left == None:
                        self.current_node.left = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.left
                else:
                    if self.current_node.right == None:
                        self.current_node.right = Node(value)
                        break
                    else:
                        self.current_node = self.current_node.right
    
    def search(self, value):
        if self.head == None:
            return False
        else:
            self.current_node = self.head

            while True:
                if value == self.current_node.value:
                    return self.current_node.value
                else:
                    if value < self.current_node.value:
                        if value == self.current_node.left:
                            return self.current_node.left
                        elif self.current_node.left == None:
                            return 'Not Found'
                        else:
                            self.current_node = self.current_node.left
                    else:
                        if value == self.current_node.right:
                            return self.current_node.right 
                        elif self.current_node.right == None:
                            return 'Not Found'
                        else:
                            self.current_node = self.current_node.right
                        
    def delete(self, value):
        if self.head == None:
            return False
        else:
            self.current_node = self.head
            self.parent = self.head
            check = True

            while self.current_node:
                    if self.current_node.value == value:
                        check = True
                        break
                    elif value < self.current_node.value:
                        self.parent = self.current_node
                        self.current_node = self.current_node.left
                    else:
                        self.parent = self.current_node
                        self.current_node = self.current_node.right


            if check == False:
                return False

            #case1 No child
            if self.current_node.left == None and self.current_node.right == None:
                if value < self.parent.value:
                    self.parent.left = None
                else:
                    self.parent.right = None

            #case2 one child
            elif self.current_node.left != None and self.current_node.right == None:
                if  value < self.parent.value:
                    self.parent.left = self.current_node.left
                else:
                    self.parent.right = self.current_node.left

            elif self.current_node.left == None and self.current_node.right != None:
                if value < self.parent.value:
                    self.parent.left = self.current_node.right
                else:
                    self.parent.right = self.current_node.right

            #case3 two child
            elif self.current_node.left != None and self.current_node.right != None:
                # case: left
                if value < self.parent.value:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    if self.change.right != None:
                        self.change_parent.left = self.change_node.right
                    else:
                        self.change_node_parent.left = None
                    self.parent.left = self.change_node
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left

                # case: right
                else:
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
                    while self.change_node.left != None:
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left

                    if self.change_node.right != None:
                        self.change_node_parent.left = self.change_node.right
                    else:
                        self.chagne_node_parent.left = None
                    self.parent.right = self.change_node
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right

            return True

tree = BST()

for i in range(8):
    tree.insert(i)
print(tree)