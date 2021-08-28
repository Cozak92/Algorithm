

# x값 = row , y값 = column
# y값이 배열 반대로 들어옴 ( Ycolumn = column - y)

#전위 방문처리 = 자기 자신을 먼저 배열에 넣음
#후위 방문처리 = 맨 밑에노드부터 방문할 노드가 없으면 위로 올려주면서 배열에 자기 자신을 넣는다.

# 1단계. 자기보다 x가 작은값(왼쪽) 중에 y 값이 가장 작고 x 값이 가까운것을 선택한다. 해당 노드를 방문처리하고 계속 내려간다.
#        없다면 자기보다 x가 큰값(오른쪽) 중에 y값이 가장 작고 x값이 가까운 것을 선택한다.
         #오른쪽에도 없다면 위로 올라간다.

         #y를 내려가면서 x값 서치

from collections import defaultdict

preorder = []
postorder = []

def indfs(cur,reversedTree,index):
    #print(cur, end="")
    preorder.append(cur)

    for x in range(index+1,len(reversedTree)):
        
        if reversedTree[x][1][0] < reversedTree[cur][1][0]:
            print(cur)
            print("check")
            indfs(x,reversedTree,index+1)
        
        elif reversedTree[x][1][0] > reversedTree[cur][1][0]:
            indfs(x,reversedTree,index+1)
            break
    postorder.append(cur)
        



def solution(nodeinfo):

    #tree = {x : {} for x in range(len(nodeinfo))}
    tree = defaultdict(lambda: [])

    
    for i in range(len(nodeinfo)):
        x, y= nodeinfo[i]
        tree[i].append(x)
        tree[i].append(y)


    reversedTree = sorted(tree.items(), key=lambda x: x[1][1], reverse=True)

    #print(reversedTree[6][1][0])

    indfs(reversedTree[0][0],reversedTree,0)


    print(preorder)
    answer = [[]]

    return answer


solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])