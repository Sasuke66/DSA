class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        size = len(intervals)
        for i in range(size - 1):
            if (intervals[i].end > intervals[i + 1].start and intervals[i].start < intervals[i + 1].end):
                return False
        return True