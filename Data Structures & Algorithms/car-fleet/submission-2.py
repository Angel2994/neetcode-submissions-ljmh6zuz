class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(speed))]
        fleets, slowestFleet = 0, 0
        for p , s in sorted(pairs, reverse = True):
            currTime = (target - p) / s
            if slowestFleet < currTime:
                slowestFleet = currTime
                fleets += 1
        return fleets