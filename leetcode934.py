from typing import  List
from copy import deepcopy
from collections import deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        B = deepcopy(A)
        m=len(A)
        n=len(A[0])
        island1=[]
        island2=[]
        ans_map = {}
        def dfs(x,y):
            if not(0<=x<m and 0<=y<n) or B[x][y]!=1:
                return
            B[x][y]=2
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        def travel(term):
            for i in range(m):
                for j in range(n):
                    if term==1:
                        if(B[i][j]==1):
                            dfs(i,j)
                            return
                    else:
                        if(B[i][j]==1 and (i,j) not in island1):
                            dfs(i,j)
                            return
        def save(list):
            nonlocal B
            for i in range(m):
                for j in range(n):
                    if B[i][j]==2:
                        list.append((i,j))
            B=deepcopy(A)

        travel(1)
        save(island1)
        travel(2)
        save(island2)
        def check_valid(x,y):
            if 0<=x<m and 0<=y<n:
                return True
            else :
                return False
        def bfs(x,y):
            temp=deque()
            temp.append((x,y))
            while len(temp)!=0:
                now=temp.popleft()
                if(check_valid(now[0]+1,now[1]) and (now[0]+1,now[1]) not in temp):
                    temp.append((now[0]+1,now[1]))
                    ans_map[(now[0]+1,now[1])]=now
                if (check_valid(now[0] - 1, now[1]) and (now[0]-1,now[1]) not in temp):
                    temp.append((now[0] - 1, now[1]))
                    ans_map[(now[0] - 1, now[1])] = now
                if (check_valid(now[0], now[1]+1) and (now[0],now[1]+1) not in temp):
                    temp.append((now[0], now[1]+1))
                    ans_map[(now[0], now[1]+1)] = now
                if (check_valid(now[0], now[1]-1) and (now[0],now[1]-1) not in temp):
                    temp.append((now[0], now[1]-1))
                    ans_map[(now[0], now[1] - 1)] = now
                if now in island2:
                    return now
        reslist=[]
        def cal(last):
            ans=0
            while ans_map[last] not in island1:
                last = ans_map[last]
                ans+=1
            return ans
        for p in island1:
            last=bfs(p[0],p[1])
            reslist.append(cal(last))
            ans_map = {}

        return min(reslist)


        pass
if __name__ == '__main__':
    so=Solution()
    test=[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    so.shortestBridge(test)
