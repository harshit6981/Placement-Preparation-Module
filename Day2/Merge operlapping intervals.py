class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        overlapped_intervals = []
        n = len(intervals)

        for i in range(n):
            if not overlapped_intervals or intervals[i][0] > overlapped_intervals[-1][1]:
                overlapped_intervals.append(intervals[i])
            else:
                overlapped_intervals[-1][1] = max(overlapped_intervals[-1][1],intervals[i][1])
        return overlapped_intervals