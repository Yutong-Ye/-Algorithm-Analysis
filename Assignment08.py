#Discrete Structure (CSCI 220)
#July 2024
#Assignment 8 - Graphs and Graph Algorithm
#Yutong Ye


import numpy as np
import random
import networkx as nx
import texttable
import numpy as np
import matplotlib.pyplot as plt


#[1] Define a function read_graph(file_name) that reads in a graph from a file in the form of an adjacency matrix.
def read_graph(file_name):
    with open(file_name) as f:
        return [[int(c) for c in line.split()]for line in f.readlines()]


#[2] Define a function print_adj_matrix(matrix) that nicely prints a graph stored as an adjacency matrix.
def print_adj_matrix(matrix):
    print(np.array(matrix))


#[3] Define a function adjacency_table(matrix) that converts an adjacency matrix into an adjacency table.
def adjacency_table(matrix):
    n = len(matrix)
    table = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                table[i].append(j)
    return table


#[4] Define a function print_adj_table(table) that nicely prints a graph stored as an adjacency table.
def print_adj_table(table):
    n = len(table)
    for i in range(n):
        print(i, "-->", table[i])


#[5] Define a function edge_set(matrix) that converts an adjacency matrix into a list of edges.
def edge_set(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges.append((i, j))
    return edges


def incidence_matrix(matrix):
    edges = list(edge_set(matrix))
    i_matrix = [[0] * len(edges) for i in range(len(matrix))]
    for k in range(len(edges)):
        a = edges[k][0]
        b = edges[k][1]
        i_matrix[a][k] = 1
        i_matrix[b][k] = 1
    return i_matrix


#[6] Define a function random_graph(n, s, p) with n vertices, s if symmetric, and probability of edge p.
def random_graph(n, sym, p):
    matrix = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                matrix[i][j] = 1
                if sym:
                    matrix[j][i] = 1
            if not sym and random.random() < p:
                matrix[j][i] = 1
    return matrix


def do_graph(desc, matrix, dir, file_name):
    print(desc)
    print_adj_matrix(matrix)
    table = adjacency_table(matrix)
    print_adj_table(table)
    edges = edge_set(matrix)
    print(edges)
    inc_matrix = incidence_matrix(matrix)
    print_adj_matrix(inc_matrix)
    do_graph_relation_properties(matrix)
    do_graph_vertix_properties(matrix)
    print()
    draw_graph(edges, dir, file_name)


def draw_graph(edges, directed, filename):
    G = nx.DiGraph()
    G.add_edges_from(edges)
    val_map = {'A': 1.0, 'D': 0.5714285714285714, 'H': 0.0}
    values = [val_map.get(node, 0.25) for node in G.nodes()]
    pos = nx.spring_layout(G)
    cmap = plt.get_cmap('jet')
    nx.draw_networkx_nodes(G, pos, cmap=cmap, node_color=values, node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='white')
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', arrows=directed, arrowsize=20)
    plt.savefig(filename)
    plt.show()


# Reflexive - if aRa is true for every a in S.
# Irreflexive - if aRa may sometimes be true but not always true for every a in S
# Anti-reflexive - if aRa is false for every a in S
# Symmetric - if aRb is true implies bRa is true for every a and b in S
# Asymmetric - if aRb is true implies bRa is false for every a and b in S
# Antisymmetric - if aRb is true implies bRa is false for every a and b in S unless a and b are equal
# Transitive - if aRb is true and bRc is true, then aRc must also be true for every a, b, c in S
# Intransitive - if aRb is true and bRc is true, then aRc is not necessarily true for every a, b, c in S
# Antitransitive - if aRb is true and bRc is true, then aRc is false for every a, b, c in S


def reflexive(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            return False
        return True


def anti_reflexive(matrix):
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 1:
            return False
        return True


def irreflexive(matrix):
    return not reflexive(matrix) and not anti_reflexive(matrix)


def symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def asymmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                return False
    return True


def anti_asymmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] == 1 and matrix[j][1] == 1:
                return False
    return True


def transitive(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] != 1:
                    return False
    return True


def intransitive(matrix):
    return not transitive(matrix) and not anti_asymmetric(matrix)


def anti_transitive(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] == 1:
                    return False
    return True


def print_table(title, headers, data, alignments):
    rows = [headers] + data
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows(rows, header=True)
    table = title + "\n" + tt.draw()
    print(table)


def do_graph_relation_properties(matrix):
    properties = [reflexive, anti_reflexive, irreflexive, symmetric, asymmetric, anti_asymmetric, transitive, intransitive, anti_transitive]
    headers = ["Property", "Value"]
    data = [[prop.__name__, prop(matrix)] for prop in properties]
    title = "Relationship Properties of the Graph"
    alignments = ['l', 'l']
    print_table(title, headers, data, alignments)


def indegree(matrix, v):
    n =len(matrix)
    return sum(matrix[i][v] for i in range(n))



def outdegree(matrix, v):
    n = len(matrix)
    return sum(matrix[v][j] for j in range(n))


def neighborhood(matrix, v):
    n = len(matrix)
    return [i for i in range(n) if matrix[v][i] == 1]


#[9] Define a function print_vertcies(graph) that lists each vertex and its in-degree, out-degree, and neighbors.
def do_graph_vertix_properties(matrix):
    properties = [reflexive, anti_reflexive, irreflexive, symmetric, asymmetric, anti_asymmetric, transitive, intransitive, anti_transitive]
    headers = ["Vertex", "Indegree", "Outdegree", "Neighborhood"]
    data = [[v, indegree(matrix, v), outdegree(matrix, v), neighborhood(matrix, v)] for v in range(len(matrix))]
    title = "Vertex Properties of the Graph"
    alignments = ['c', 'c', 'c', 'c']
    print_table(title, headers, data, alignments)


def main():
    matrix1 = read_graph("Graph1.txt")
    do_graph("Graph read from file Graph1.txt", matrix1, False, "Assignment08-graph1.png")
    matrix2 = random_graph(6, False, .5)
    do_graph(f"Random graph with n={6}, sym={False}, p={.5}", matrix2, False, "Assignment08-graph2.png")
    matrix3 = random_graph(6, True, .5)
    do_graph(f"Random graph with n={6}, sym={True}, p={.5}", matrix3, False, "Assignment08-graph3.png")
    matrix4 = random_graph(6, False, 1)
    do_graph(f"Completed Graph of size 6", matrix4, False, "Assignment08-graph4.png")



if __name__ == '__main__':
    main()