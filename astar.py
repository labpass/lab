def aStarAlgo(start,end):
    opSet = set(start)
    clSet = set()
    g = {}
    parents = {}
    g[start] = 0
    parents[start] = start
    while(len(opSet)>0):
        n = None
        for u in opSet:
            if n == None or g[u] + heu(u) < g[n] + heu(n):
                n = u
        if n==end or g[n] == None:
            pass
        else :
            for (m,wei) in getNeigh(n):
                if m not in opSet and m not in clSet:
                    opSet.add(m)
                    parents[m] = n
                    g[m] = g[n]+wei
                else :
                    if g[m]>g[n] + wei :
                        g[m] = g[n] + wei
                        parents[m] = n
                        if m in clSet :
                            clSet.remove(m)
                            opSet.add(m)
        if n == None :
            print('path non-existent\n')
            return None
        if n == end :
            path = []
            while parents[n] != n :
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print('path found {}'.format(path))
            return path
        opSet.remove(n)
        clSet.add(n)
    print('path non-existent\n')
    return None
def getNeigh(v):
    if v in graphNode:
        return graphNode[v]
    else:
        return None
def heu(u):
    heuDict = {
    'A':11,'B':6,'C':5,'D':7,'E':3,'F':6,'G':5    
    }
    return heuDict[u]
graphNode={
    'A':[('B',2),('E',3)],
    'B':[('A',2),('C',1),('G',9)],
    'C':[('B',1)],
    'D':[('G',1),('E',6)],
    'E':[('A',3),('D',6)],
    'F':[('B',9),('D',1)]
}
aStarAlgo('A','G')
