"""
https://leetcode.com/problems/queue-reconstruction-by-height/
"""
from typing import List


class QueueReconstructionByHeight:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        result = []
        for p in people:
            result.insert(p[1], p)
        return result


s = QueueReconstructionByHeight()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
