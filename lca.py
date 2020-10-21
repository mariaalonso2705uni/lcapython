class TreeNode:
    def __init__(self, key):
        self.key = key
        self.before = []
        self.next = []

#LCA for Directed Acyclic Graph
def dagLCA(root,n1,n2):
    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root
    if n1 == n2:
        return n1.key
    lca = []
    i=0
    while(i<len(n1.before)):
        j=0
        while(j<len(n2.before)):
            if(n1.before[i].key == n2.before[j].key):
                lca.append(n1.before[i].key)
                j+=1
            else:
                j+=1
        i+=1

    if(lca == []):
        if(n1.key > n2.key):
            lca.append(dagLCA(root,n1.before[0],n2))
        else:
            lca.append(dagLCA(root,n1,n2.before[0]))

    return max(lca)

#directed acylic graph
root = Node(1)
r2 = Node(2)
r3 = Node(3)
r4 = Node(4)
r5 = Node(5)
r6 = Node(6)
root.next = [r2,r3,r4,r5]
r2.next = [r4]
r2.before = [root]
r3.next = [r4, r5]
r3.before = [root]
r4.next = [r5]
r4.before = [r2,r3,root]
r5.before = [r3,r4,root]
r6.before = [r4]