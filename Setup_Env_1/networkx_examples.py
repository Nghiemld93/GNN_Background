import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_nodes_from(
    [
        (0,{"color" : "blue" , "size": 250}),
        (1,{"color" : "green" , "size": 50}),
        (2,{"color" : "black" , "size": 2500}),
        (3,{"color" : "yellow" , "size": 250}),
        (4,{"color" : "red" , "size": 250})
    ]
)

G.add_edges_from(
    [
        (0,1),
        (0,2),
        (0,3),
        (0,4),
        (2,1),
        (3,2),
        (2,3),
        (2,4)
    ]
)

for node in G.nodes(data=True):
    print(node)

node_colors =nx.get_node_attributes(G, name="color").values()
colors=list(node_colors)
node_sizes = nx.get_node_attributes(G, name="size").values()
sizes=list(node_sizes)
nx.draw(G,with_labels=True, node_color=colors, node_size=sizes)