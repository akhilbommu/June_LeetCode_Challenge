"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
from typing import List
import collections


class CheapestFlightsWithinKStops:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0

        location = collections.defaultdict(list)
        prices = collections.defaultdict(lambda: float('inf'))

        for u, v, p in flights:
            location[u] += [(v, p)]

        q = [(src, -1, 0)]

        while q:
            position, k, cost = q.pop(0)
            if position == dst or k == K:
                continue

            for neighbour, p in location[position]:
                if cost + p >= prices[neighbour]:
                    continue
                else:
                    prices[neighbour] = cost + p
                    q += [(neighbour, k + 1, cost + p)]

        if prices[dst] < float('inf'):
            return prices[dst]
        return -1


obj = CheapestFlightsWithinKStops()
print(obj.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
print(obj.findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
