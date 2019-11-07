from graph_examples import graphlib as Graph

if __name__ == '__main__':
    graph = {'A' : ['B', 'C'],
             'B' : ['C', 'D'],
             'C' : ['D'],
             'D' : ['C'],
             'E' : ['D'],
             'F' : ['B']}

    print(Graph.find_all_paths(graph, 'A', 'D'))
