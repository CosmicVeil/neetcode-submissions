class TimeMap:

    timeMap = {}
    keyArr = {}

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timeMap:
            self.timeMap[key] = {}
            self.keyArr[key] = []
        self.timeMap[key][timestamp] = value
        self.keyArr[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""

        currArr = self.keyArr[key]

        l = 0
        r = len(currArr)-1

        works = currArr[-1]

        if currArr[0] > timestamp:
            return ""
        

        while l<=r:
            m = (l+r)//2

            if currArr[m] <= timestamp:
                works = currArr[m]
                l = m+1
            else:
                r = m-1
                    
        return self.timeMap[key][works]
        
