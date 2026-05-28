class TimeMap:

    def __init__(self):
        self.list = []
        self.dict = {}
        self.count = 0
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        try:
            self.dict[key]
        except KeyError:
            self.dict[key] = self.count
            self.count = self.count + 1
            self.list.append([[timestamp,value]])
        else:
            self.list[self.dict[key]].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        try:
            self.dict[key]
        except KeyError:
            return ""
        else:
            temp_list = self.list[self.dict[key]]
            

        if len(temp_list) == 0:
            return ""
        elif len(temp_list) == 1:
            if temp_list[0][0] <= timestamp:
                return temp_list[0][1]
            else:
                return ""
        elif len(temp_list) == 2:
            if temp_list[1][0] <= timestamp:
                return temp_list[1][1]
            elif temp_list[0][0] <= timestamp:
                return temp_list[0][1]
            else:
                return ""

        left = 0
        right = len(temp_list) - 1

        if temp_list[0][0] > timestamp:
            return ""

        while True:
            mid = (left+right)//2
            mid_time = temp_list[mid][0]

            if right-left == 1:
                if temp_list[right][0] <= timestamp:
                    return temp_list[right][1]
                elif temp_list[left][0] <= timestamp:
                    return temp_list[left][1]
                else:
                    return ""


            if mid_time == timestamp:
                return temp_list[mid][1]
            elif mid_time < timestamp and temp_list[mid+1][0] > timestamp:
                return temp_list[mid][1]
            elif mid_time > timestamp and temp_list[mid-1][0] < timestamp:
                return temp_list[mid-1][1]
            elif mid_time < timestamp and temp_list[mid+1][0] <= timestamp:
                left = mid
            elif mid_time > timestamp and temp_list[mid-1][0] >= timestamp:
                right = mid


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)