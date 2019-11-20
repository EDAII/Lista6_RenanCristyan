# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Grafos

def swap(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

class Node():
    def __init__(self, value=None):
        self.value = value
        self.adj = []
        self.visited = False

    def addNeighbor(self, ngh):
        if type(ngh) is int:
            n = Node(value=ngh)
            self.adj.append(n)
        else: self.adj.append(ngh)

    def showAdj(self, values=True):
        all_ngh = []
        for ngh in self.adj:
            if values: all_ngh.append(ngh.value)
            else: all_ngh.append(ngh)
        return all_ngh

    def showNode(self):
        print('Node:')
        print('Value = ', self.value)
        print('Adjacent = ', self.showAdj())
        print('-'*30)

class Graph():
    def __init__(self):
        self.nodes = []
        self.path_traveled = []

    def addNode(self, value):
        self.nodes.append(Node(value))

    def createNodes(self, list_of_values):
        for value in list_of_values:
            self.addNode(value)

    def addEdge(self, node, target):
        if type(node) is int and type(target) is int:
            n = self.findNode(node)
            t = self.findNode(target)

            if n == None and t == None:
                raise Exception("{} e {} não estão no grafo".format(node, target))
            elif n == None:
                raise Exception("{} não está no grafo".format(node))
            elif t == None:
                raise Exception("{} não está no grafo".format(target))
            else:   
                n.adj.append(t)
        
        else:
            node.adj.append(target)

    def setEdges(self, target_value, list_of_values):
        for v in list_of_values:
            self.addEdge(target_value, v)

    def findNode(self, target_value):
        value_found = False
        for node in self.nodes:
            if node.value == target_value:
                return node       
        
        if not value_found:
            return None        

    def showPathTraveled(self):
        nodes = []
        for node in self.path_traveled:
            nodes.append(node.value)
        print(nodes)

    def showAllNodes(self):
        print('\nTodos os nós')

        if self.nodes == []: print('Grafo vazio')

        else:
            for node in self.nodes:
                node.showNode()
                
    def listAllNodes(self):
        l = []
        for n in self.nodes:
            l.append(n.value)
        return l

    def reset(self):
        self.path_traveled = []
        for node in self.nodes:
            node.visited = False

    def BFS(self, start=None):
        if type(start) is int:
            for i, n in enumerate(self.nodes):
                if n.value == start:
                    swap(self.nodes, 0, i) 

        queue = []

        for s in self.nodes:
            if not s.visited:
                queue.append(s)
                self.path_traveled.append(s)
                s.visited = True

                while queue != []:
                    u = queue[0]
                    del(queue[0])
                    
                    for v in u.adj:
                        if not v.visited:
                            self.path_traveled.append(v)
                            v.visited = True
                            queue.append(v)

    def DFS(self, start=None):
        if type(start) is int:
            for i, n in enumerate(self.nodes):
                if n.value == start:
                    swap(self.nodes, 0, i) 

        for n in self.nodes:
            if not n.visited:
                self.path_traveled.append(n)
                self.DFSv(n)

    def DFSv(self, node):
        if type(node) is int: node = self.findNode(node)

        node.visited = True
        if self.path_traveled == []:
            self.path_traveled.append(node)
        
        for w in node.adj:
            if not w.visited:
                self.path_traveled.append(w)
                self.DFSv(w)

    def reverseGraph(self):
        reverse = Graph()
        reverse.createNodes(self.listAllNodes())

        for node in self.nodes:
            for adj in node.adj:
                a = reverse.findNode(adj.value)
                n = reverse.findNode(node.value)
                reverse.addEdge(a, n)

        return reverse

    def isStronglyConnected(self):
        self.reset()

        n = self.nodes[0]
        self.DFSv(n)

        if len(self.path_traveled) != len(self.nodes):
            return False

        rg = self.reverseGraph()
        rg.DFSv(rg.findNode(n.value))

        if len(rg.path_traveled) != len(rg.nodes):
            return False

        return True
