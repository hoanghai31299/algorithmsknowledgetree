G = []
class Node:
    def __init__(self,dinh,chiphi,hue,truoc):
        self.dinh = dinh
        self.chiphi = chiphi
        self.hue = hue
        self.tong = chiphi + hue
        self.truoc = truoc
def Init(pathGraph,pathHue,G,Hueristic):
    f = open(pathGraph);
    n = int(f.readline(),base = 10)
    s = int(f.readline(),base = 10)
    g = int(f.readline(),base = 10)
    for i in range(n+1):
        G.append([])
        Hueristic.append(0)
        for j in range(n+1):
            G[i].append(0)
    while True:
        string = f.readline()
        if not string: #if x == ''
            break
        i,j,x = map(lambda num:int (num,base = 10),string.split())
        G[i][j] = G[j][i] = x
    f.close()
    f = open(pathHue)
    while True:
        string = f.readline()
        if not string:
            break
        k = string.index(" ")
        str = string[0:k]
        i = int(str,base=10)
        m = string.index(" ",k)
        str = string[k+1:len(string)]
        x = int(str,base=10)
        Hueristic[i] = x
    f.close()
    return n,s,g
def printMatrix(A,n):
    print('so dinh: %d'%n)
    for i in range(1,n+1):
            for j in range(1,n+1):
                print("%d"%A[i][j],end = '\t')
            print('\n')
def Push(Open,duongDi):
    Open.append(duongDi)
    for i in range(len(Open)-1):
        for j in range(i+1,len(Open)):
            a,b = Open[i],Open[j]
            if(a.tong < b.tong):
                temp = Open[i]
                Open[i] = Open[j]
                Open[j] = temp
def check(Open,Close,x):
    for i in range(len(Open)):
        if Open[i].dinh == x:
            return False
    for i in range(len(Close)):
        if Close[i].dinh == x:
            return False
    return True
def printResult(P):
    print('chi phi: %d'%P[len(P)-1].chiphi)
    print('duong di:',end = " ")
    for i in range(len(P)-1):
        print(P[i].dinh, end = "=> ")
    print(P[len(P)-1].dinh)
def AKT():
    P = []
    Hueristic = []
    Open = []
    Close = []
    n,s,g = Init('data/graph2.inp','data/hueristic2.inp',G,Hueristic)
    Push(Open,Node(s,0,Hueristic[s],s))
    goal = Node(g,0,0,0)
    while True:
        if len(Open) == 0:
            if goal.chiphi == 0:
                print('khong co duong di')
                break
            else: printResult(P)
        p = Open.pop()
        P.append(p)
        if p.dinh == goal.dinh:
            printResult(P)
            break
        for i in range(len(G)):
            if(G[p.dinh][i] > 0):
                if check(Open,Close,i):
                    Push(Open,Node(i,G[p.dinh][i]+p.chiphi,Hueristic[i],p.dinh))
        Close.append(p)
AKT()

    


