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

    def iterative_deepning_dfs(self, target):
        """
        # IDDFS - 반복적 깊이 증가 탐색
        - params: startNode(Node), tartget(str), currentDepth(int), maxDepth(int)
            - IDDFS(타겟): 깊이 = 1로 초기화하고, 최하단에 도달할 때까지 helper를 부르고 깊이 *=2 해줌 (깊이는 탐색은 임의 설정)
            - IDDFS_HELPER(시작노드, 시작 탐색 깊이, 최대 탐색 깊이): 자식들 모두 불러서 recursive 해줌
        """
        depth = 1
        bottom_reached = False
        while not bottom_reached:
            result, bottom_reached = self.iterative_deepning_dfs_helper(self, target, 0, depth)

            if result:
                print("Found")
                return result
            depth *= 2
            print(depth, 'increased')
        return None


    def iterative_deepning_dfs_helper(self, node, target, currentDepth, maxDepth):
        """
        Args:
            node (Node): Node
            target (str): node.name을 비교함
            currentDepth (int): 시작 탐색 깊이
            maxDepth (int): 최대 탐색 깊이
        """
        print("Visiting", node.name)

        if node.name == target:
            return node, True
        
        if currentDepth == maxDepth:
            print("현재 최대 탐색 깊이 도달, 종료")
            if len(node.children) > 0:
                # 최하단까지 도달은 못했음
                return None, False
            else:
                return None, True

        # 자식들 모두 recursive
        bottom_reached = True
        for i in range(len(node.children)):
            result, bottom_reached_children = self.iterative_deepning_dfs_helper(node.children[i], target, currentDepth + 1, maxDepth)

            if result:
                return result, True

            bottom_reached = bottom_reached and bottom_reached_children

        return None, bottom_reached

def makeGraph():
    graph = Node("A")
    graph.addChild(["B", "C", "D"])
    graph.children[0].addChild(["E", "F"])
    graph.children[2].addChild(["G", "H"])
    graph.children[0].children[1].addChild(["I", "J"])
    graph.children[2].children[0].addChild(["K"])

    return graph



graph = makeGraph()
print(graph.iterative_deepning_dfs("K"))