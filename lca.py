class TreeNode:
    def __init__(self, key):
        self.key = key
        self.before = []
        self.next = []

#LCA for Directed Acyclic Graph
def lowestCommonAncestor(root,p,q):
    if root is None:
        return None

    if root.key == p or root.key == q:
        return root
    if p == q:
        return p.key
    lca = []
    i=0
    while(i<len(p.before)):
        j=0
        while(j<len(q.before)):
            if(p.before[i].key == q.before[j].key):
                lca.append(p.before[i].key)
                j+=1
            else:
                j+=1
        i+=1

    if(lca == []):
        if(p.key > q.key):
            lca.append(lowestCommonAncestor(root,p.before[0],q))
        else:
            lca.append(lowestCommonAncestor(root,p,q.before[0]))

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