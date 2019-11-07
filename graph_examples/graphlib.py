def find_path(graph, start, end, path=[]):
    """
    Return a list of nodes (including the start and end nodes) in graph
    comprising the path. If no path can be found - return None.

    The same node will not occur more than once on the path returned
    (i.e. it won't contain cycles).
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    """
    Return a list of lists of nodes in graph comprising all paths from start
    node to end node. If no path can be found - return None.

    The same node will not occur more than once on any path returned
    (i.e. no path will contain cycles).
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    all_paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                all_paths.append(new_path)
    return all_paths if all_paths else None
