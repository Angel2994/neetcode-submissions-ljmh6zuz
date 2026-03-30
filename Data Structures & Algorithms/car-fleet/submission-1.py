class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        carfleet = curtime = 0
        for p, s in sorted(pairs, reverse = True):

            destination = (target - p) / s
            if curtime < destination:
                curtime = destination
                carfleet += 1
        return carfleet
