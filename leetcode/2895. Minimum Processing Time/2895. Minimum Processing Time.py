class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        res=0
        processorTime.sort(reverse=True)
        tasks.sort()
        j=0
        for i in range(len(tasks)):
            res=max(res,tasks[i]+processorTime[j])
            if (i+1)%4==0:  j+=1
        return res
