"""
https://leetcode.com/problems/two-city-scheduling/
"""
from typing import List


class TwoCityScheduling:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: x[0] - x[1])
        result = 0
        result += sum([costs[i][0] for i in range(len(costs) // 2)])
        result += sum([costs[i][1] for i in range(len(costs) // 2, len(costs), 1)])
        return result


obj = TwoCityScheduling()
print(obj.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
