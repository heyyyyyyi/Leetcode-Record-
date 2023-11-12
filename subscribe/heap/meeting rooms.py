import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key= lambda x:x[0])
        heapq.heappush(rooms, intervals[0][1])
        for item in intervals[1:]:
            if rooms[0] <= item[1]:
                heapq.heappop(rooms)
            heapq.heappush(rooms,item[1])

        return len(rooms)
    

    2
    #peak value*/
    starts : +1
    endts: -1
    maxvalue
    

