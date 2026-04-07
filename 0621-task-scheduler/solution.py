# Problem: #621 - Task Scheduler
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/task-scheduler/
# Submitted: 2026-04-07
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        scd = [] 
        #[available time, count, value]
        jobs = []
        #[count, value]
        hm = Counter(tasks)

        for i in hm:
            heapq.heappush(jobs, (-hm[i], i))
        
        ans = 0
        while scd or jobs:
            while scd and scd[0][0] <= ans:
                pop = heapq.heappop(scd)
                heapq.heappush(jobs, (pop[1], pop[2]))
            
            if jobs:
                pop = heapq.heappop(jobs)
                remain = -pop[0] - 1
                if remain >= 1:
                    heapq.heappush(scd, (ans + n + 1, -remain, pop[1]))

            ans += 1
        return ans
