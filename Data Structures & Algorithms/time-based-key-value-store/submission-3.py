class TimeMap:

    def __init__(self):
        self.dictonary = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictonary[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dictonary[key]) == 0:
            return ""
        else:
            values = self.dictonary[key]
            left, right = 0, len(values)-1
            res = ""

            while left <= right:
                mid = (left+right)//2

                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    left = mid + 1
                elif values[mid][0] > timestamp:
                    right = mid-1

            return res
        
"""
alice : [(1, happy), (3, sad)]
"""