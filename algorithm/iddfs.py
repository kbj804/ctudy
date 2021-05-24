# ref: https://www.seokdev.site/207?category=247927

# 반복적 깊이 증가(IDDFS)는 깊이 우선 탐색(DFS)처럼 메모리 깊이 제한에 비례하면서도 최단 경로로 목표 노드를 찾는 것을 보장하는 방법이다.
# IDDFS 방법에서는 목표 노드가 찾아질 때까지 깊이 제한을 1씩 증가시키면서 연속적인 깊이 우선 탐색을 수행한다.

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
        
    def addChild(self, nameList):
        for name in nameList:
            self.children.append(Node(name))
        return self


    def breadthFirstSearch(self, result=[], que=[]):
        """
        # BFS(너비 우선 선택)
        """
        result.append(self.name)

        for i in self.children:
            que.append(i)

        while que:
            currnet = que.pop(0)
            currnet.breadthFirstSearch(result, que)
        
        return result

def makeGraph():
    graph = Node("A")
    graph.addChild(["B", "C", "D"])
    graph.children[0].addChild(["E", "F"])
    graph.children[2].addChild(["G", "H"])
    graph.children[0].children[1].addChild(["I", "J"])
    graph.children[2].children[0].addChild(["K"])

    return graph


    
graph = makeGraph()
print(graph.breadthFirstSearch())
