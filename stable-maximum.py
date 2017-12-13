import itertools

#Find the maximum independent set in a graph with a greedy algorithm

graph_test = [[0,1,0,0,0,1],
         [1,0,1,0,0,1],
         [0,1,0,1,0,0],
         [0,0,1,0,1,0],
         [0,0,0,1,0,1],
         [1,1,0,0,1,0]]

def stable(graph,sommets_ignorer):
    """
    :param graph: graph dans lequel on chercher le stable
    :param sommets_ignorer: nodes that are ignored to create the stable
    :return:  True if the graph is a stable. False if it's not.
    """
    # verifie que cest tous des zeros dans la moitier triangle superieur en sautant les sommets a ignorer
    for i in range(len(graph)):
        if i in sommets_ignorer:
            continue
        for j in range(i,len(graph)):
            if j in sommets_ignorer:
                continue
            if graph[i][j] == 1:
                return False
    return True

def stable_taille_maximum(graph):
    sommets = [x for x in range(len(graph))]

    #cree tous les combinaisons de sommets, en creeant des combinaisons de tailles croissantes
    for i in range(0, len(sommets) + 1):
        for sommets_ignorer in itertools.combinations(sommets, i):
            if stable(graph,sommets_ignorer):
                print("Size of the maximum independent set:", len(sommets) - len(sommets_ignorer))
                print("Maximum independent set:", [element for element in sommets if element not in sommets_ignorer])
                return

stable_taille_maximum(graph_test)
