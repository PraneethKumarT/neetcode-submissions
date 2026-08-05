class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        data = defaultdict(list)
        q = deque()
        indegree = [0] * numCourses

        for dest, src in prerequisites:
            data[src].append(dest)
            indegree[dest] += 1
         
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        cnt = 0
        while len(q) > 0:
            n = q.popleft()
            cnt += 1

            for n in data[n]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return cnt == numCourses


        
    """
 [0,1]
 1 -> 0
    """