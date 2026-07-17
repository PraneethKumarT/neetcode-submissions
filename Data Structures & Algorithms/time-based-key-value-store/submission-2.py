class TimeMap:

    def __init__(self):
        self.dictonary = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictonary[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dictonary[key]) == 0:
            return ""
        else:
            i = len(self.dictonary[key])-1
            while i >= 0:
                temp = self.dictonary[key][i]
                if temp[0] <= timestamp:
                    return temp[1]
                i -= 1
            return ""


        
"""
alice : [(1, happy), (3, sad)]
"""