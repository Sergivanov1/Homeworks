import networkx as nx
import random as rnd
import matplotlib.pyplot as plt

def coloring(node, color):
   for neighbor in G.neighbors(node):
       color_of_neighbor = colors_of_nodes.get(neighbor, None)
       if color_of_neighbor == color:
          return False
   return True

def get_color_for_node(node):
    for color in colors:
       if coloring(node, color):
          return color

def main():
    for node in G.nodes():
        colors_of_nodes[node] = get_color_for_node(node)
    print (colors_of_nodes)

N = int(input())
edges_count = int(input())

G = nx.Graph()
G.add_nodes_from(i+1 for i in range(N))
colors = ['red', 'blue', 'green', 'yellow',  'black', 'pink', 'orange', 'white', 'gray', 'purple', 'brown', 'navy']
edges_list = [] #список путей
colors_of_nodes = {} #света вершин
chromatic_num = 0 #хроматическое число
i = 0
#генерация случайных путей
while i < edges_count:
    first = rnd.randint(1, N)
    second = rnd.randint(1, N)
    res = [first, second]
    if first != second and tuple(res) not in edges_list and tuple(res[::-1]) not in edges_list:
        edges_list.append(tuple(res))
        i+=1
#
G.add_edges_from(edges_list)
print(edges_list)
main()
color_map = [clr for clr in colors_of_nodes.values()]
nx.draw_circular(G, node_color = color_map, with_labels=True, font_weight='bold')
unic_colors = []
for color in color_map:
    if color not in unic_colors:
        unic_colors.append(color)
        chromatic_num += 1
print('Хроматическое число графа: {}'.format(chromatic_num))
plt.draw()
plt.show()