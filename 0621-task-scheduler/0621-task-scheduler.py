class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        for task in tasks:
            hashmap[task] = hashmap.get(task,0) + 1
        
        freq = sorted(hashmap.values(),reverse=True)
        max_freq = freq[0]
        count_max = 0
        for val in freq:
            if val == max_freq:
                count_max += 1
        
        f_b_len = (max_freq - 1) * (n + 1) + count_max
        return max(f_b_len,len(tasks))