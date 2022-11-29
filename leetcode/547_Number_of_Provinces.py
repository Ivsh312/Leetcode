from typing import List


class Solution:
    def dfg(self, vertix):
        graph_vertix = self.graph[vertix]
        if sum(graph_vertix) == 1:
            return
        self.save_dict[vertix] = graph_vertix
        for index, number_is_link in enumerate(graph_vertix):
            if number_is_link and index not in self.save_dict:
                self.dfg(index)


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        all_citys=[]
        self.graph = isConnected[:]
        for i in range(len(isConnected)):
            self.save_dict = {}
            self.dfg(i)
            if self.save_dict == {} or self.save_dict not in all_citys:
                all_citys.append(self.save_dict)
        return len(all_citys)
print(Solution().findCircleNum([[1,1,0],[0,1,0],[0,0,1]]))