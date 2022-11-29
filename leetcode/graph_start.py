from collections import deque


def dfg(vertix, save_dict):
    save_dict[vertix] = graph[vertix]
    a.append(vertix)
    for sub_vertix in graph[vertix]:
        if sub_vertix not in save_dict.keys():
            dfg(sub_vertix,save_dict)



[[1,1,0],[1,1,0],[0,0,1]]

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

save_list = {}
a = deque()
dfg('0',save_list)
print(save_list)
print(a)