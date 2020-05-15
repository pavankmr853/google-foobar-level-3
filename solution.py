
def bfs(l):
    target =  len(l)-1
    queue=[]
    st=0
    end=0
    queue.append(0)
    level=[]
    i=0
    while i<len(l):
        level.append(-1)
        i=i+1
    level[0]=1
    while st<=end:
        a = queue[st]
        st = st+1
        j=0
        while j<len(l[a]):
            if level[l[a][j]]!=-1:
                j=j+1
            else:
                level[l[a][j]] = level[a]+1
                queue.append(l[a][j])
                end = end+1
                j=j+1
    if level[target]==-1:
        return (len(l)+100)
    else:
        return level[target]
                
            
            

def finder(map):
    a = len(map)
    b = len(map[0])
    l=[]
    i=0
    while i<a:
        j=0
        while j<b:
            l.append([])
            if map[i][j]==1:
                j=j+1
                continue
            else:
                if i!=0:
                    if map[i-1][j]==0:
                        l[i*b+j].append((i-1)*b+j)
                if i!=a-1:
                    if map[i+1][j]==0:
                        l[i*b+j].append((i+1)*b+j)
                if j!=0:
                    if map[i][j-1]==0:
                        l[i*b+j].append((i*b)+j-1)
                if j!=b-1:
                    if map[i][j+1]==0:
                        l[i*b+j].append(i*b+j+1)
                j=j+1
        i=i+1
    #print(len(l))
    ans = bfs(l)
    return ans
    


def solution(map):
    a = len(map)
    b = len(map[0])
    ans = min(a*b,finder(map))
    i=0
    while i<a:
        j=0
        while j<b:
            if map[i][j]==0:
                j=j+1
                continue
            else:
                map[i][j]=0
                ans = min(ans,finder(map))
                map[i][j]=1
                j=j+1
                if ans==a+b-1:
                    return ans
        i=i+1
        
    return ans
    
    
    
    

## testing
    
    
#print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
#print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
