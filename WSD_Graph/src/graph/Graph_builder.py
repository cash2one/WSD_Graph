import Dir
import src.tools.FileTools as tools
import jieba
from collections import defaultdict
from heapq import *
import re
import queue

debug = False
### load data from multi files,if input is string, it will transfer into list automatic
### return a data set of dict type({pos:sentence1,sentence2,..., sentencen})
def load_data(files):
    if str(type(files)) =="<class 'str'>":
        files = [files]
    data = {}
    data["pos"] =[]
    data["neg"] = []
    for file in files:
        content = tools.read_lines(file)
        for line in content:
            line = re.sub("pos|neg","", line)
            if "pos" in line:
                data["pos"].append(line)
            else:
                data["neg"].append(line)
    return data

### a data set of dict type({pos:sentence1,sentence2,..., sentencen})
### return a graph complement with list(邻接矩阵)
def build_graph1(data):
    graph=[]
    words_index={}
    count =0
    for key in data.keys():
        tmp_data = data[key]
        for corpus_line in tmp_data:
            words = list(jieba.cut(corpus_line))
            if words.__len__()>0:
                for word in words:
                    if word not in words_index.keys():
                        words_index[word] = count
                        count+=1

    for i in range(words_index.keys().__len__()):
        graph.append([0]*words_index.keys().__len__())

    for key in data.keys():
        tmp_data = data[key]
        for corpus_line in tmp_data:
            words = list(jieba.cut(corpus_line))
            for i in range(words.__len__()-1):
                word  = words[i]
                next_word = words[i+1]
                graph[words_index[word]][words_index[next_word]] +=1
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if i != j and graph[i][j] != 0:
                degree = get_degree(graph,i)
                print(i,j,graph[i][j])
                edges.append((i, j, graph[i][j]/degree))
    if debug:
        __output_list_graph(edges)
    return edges,words_index



def build_graph(data):
    graph={}
    words_index={}
    count =0
    for key in data.keys():
        tmp_data = data[key]
        for corpus_line in tmp_data:
            words = list(jieba.cut(corpus_line))
            if words.__len__()>0:
                for word in words:
                    if word not in words_index.keys():
                        words_index[word] = count
                        count+=1

    for key in data.keys():
        tmp_data = data[key]
        for corpus_line in tmp_data:
            words = list(jieba.cut(corpus_line))
            for i in range(words.__len__()-1):
                word  = words[i]
                next_word = words[i+1]
                if i not in graph.keys():
                    graph[i] = {}
                if i+1 not in graph[i].keys():
                    graph[i][i+1] =0
                graph[i][i+1]+=1

    if debug:
        __output_graph(graph)
    return graph,words_index

# def find_shorest_path_dijkstra(graph,start_word,end_word):
#     if start_word in graph.keys() and end_word in graph.keys():
#
#     else:
#         return -1

def get_degree(graph,node):
    count =0
    for i in range(graph.__len__()):
        if graph[node][i]!= 0:
            # print(node, i,graph[node][i])
            count+= graph[node][i]
    return count

def dijkstra_raw(edges, from_node, to_node):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen = [(0,from_node,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == to_node:
                return cost,path
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (1-cost*c, v2, path))
    return float("inf"),[]

def dijkstra(edges, from_node, to_node):
    len_shortest_path = -1
    ret_path=[]
    length,path_queue = dijkstra_raw(edges, from_node, to_node)
    if len(path_queue)>0:
        len_shortest_path = length      ## 1. Get the length firstly;
        ## 2. Decompose the path_queue, to get the passing nodes in the shortest path.
        left = path_queue[0]
        ret_path.append(left)       ## 2.1 Record the destination node firstly;
        right = path_queue[1]
        while len(right)>0:
            left = right[0]
            ret_path.append(left)   ## 2.2 Record other nodes, till the source-node.
            right = right[1]
        ret_path.reverse()  ## 3. Reverse the list finally, to make it be normal sequence.
    return len_shortest_path,ret_path

def __output_graph(graph):
    for key in graph.keys():
        for key1 in graph[key].keys():
            print(key,key1,graph[key][key1])

def __output_list_graph(list_graph):
    for list_g in list_graph:
        print(list_g)

def get_max_property(graph,start_node, end_node,length):
    node_queue = queue(max_size= graph.__len__())
    for i in range(graph.__len__()):
        node_queue.put(i)

    result = [-1]* length
    while node_queue.__len__()>0:
        for next_node in graph[start_node].keys():
            if result[next_node] == -1:
                result[next_node] = graph[start_node][next_node]
            else:
                value = result[]



debug = True
test_file = Dir.resource+"test/test_file"
print(test_file)
data = load_data(test_file)
result = build_graph(data)
edges = result[0]
word_index = result[1]

print("北京",word_index["北京"],"天安门",word_index["天安门"])
result= dijkstra(edges,word_index["北京"],word_index["天安门"])
print(result[1])
rate =1
for i in range(result[1].__len__()-1):
    before =result[1][i]
    after = result[1][i+1]
    print(before,after)
    print(edges[before][after])
    rate *=edges[before][after]
print(rate)

# def demo():

