class TimeMap:

    def __init__(self):
        self.hashMap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.hashMap.get(key, [])
        closest = 0
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                res = values[m][0]
                return res
            if values[m][1] < timestamp:
                l = m + 1
                res = values[m][0]
            else:
                r = m - 1
        
        return res
            
