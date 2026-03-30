class TimeMap:

    def __init__(self):
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        nextClosest = -1
        while l <= r:
            m = (l + r) // 2
            if values[m][-1] == timestamp:
                res = values[m][0]
                return res
            if values[m][1] < timestamp:
                nextClosest = max(nextClosest, m)
                l = m + 1
            else:
                r = m - 1
        if nextClosest >= 0:
            res = values[nextClosest][0]
        return res