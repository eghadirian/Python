graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def breadth_first_search(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

breadth_first_search(visited, graph, 'A')


visited = set()
def depth_first_search(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            depth_first_search(visited, graph, neighbour)

depth_first_search(visited, graph, 'A')