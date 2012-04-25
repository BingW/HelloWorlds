#coding:utf-8
import networkx as nx

nodes = [1,2,3,4,5,6,7,8,9,10,11]
edges = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(5,6),(5,7),(6,7),(1,5),\
            (8,9),(8,10),(8,11),(9,10),(9,11),(11,1)]

G = nx.Graph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)

FF_0 = Force_Field()
simulation(G,FF_0)
