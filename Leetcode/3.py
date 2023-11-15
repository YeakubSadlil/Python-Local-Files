from datetime import datetime
from typing import List, Dict
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> Dict[str, List[str]]:
        access_dict = {}
        for name, time in access_times:
            if name not in access_dict:
                access_dict[name] = []
            access_dict[name].append(time)
        
        
        for name in access_dict:
            access_dict[name].sort()
        lst = []
        
        for name, times in access_dict.items():
            for i in range(len(times) - 2):
                time1 = datetime.strptime(times[i], "%H%M")
                time3 = datetime.strptime(times[i + 2], "%H%M")
                if (time3 - time1).seconds < 3600:
                    lst.append(name)
                    break
        return lst
sl = Solution()
print(sl.findHighAccessEmployees(access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]))