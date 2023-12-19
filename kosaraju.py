from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


def dfs1(v, graph, used, order):
    stack = [v]
    while stack:
        node = stack[-1]
        if used[node]:
            stack.pop()
            order.append(node)
        else:
            used[node] = True
            stack.extend(neighbor for neighbor in graph[node] if not used[neighbor])


def dfs2(v, transposed_graph, used, component):
    stack = [v]
    while stack:
        node = stack.pop()
        if not used[node]:
            used[node] = True
            component.append(node)
            stack.extend(neighbor for neighbor in transposed_graph[node] if not used[neighbor])


def kosaraju_algorithm(n, edges):
    graph = defaultdict(list)
    transposed_graph = defaultdict(list)

    for a, b in edges:
        graph[a].append(b)
        transposed_graph[b].append(a)

    used = [False] * n
    order = []

    for i in range(n):
        if not used[i]:
            dfs1(i, graph, used, order)

    used = [False] * n
    components = []

    for i in range(n - 1, -1, -1):
        v = order[i]
        if not used[v]:
            component = []
            dfs2(v, transposed_graph, used, component)
            components.append(component)

    return components


def visualize_graph(graph, components):
    G = nx.DiGraph()

    # Добавляем вершины
    for node in graph:
        G.add_node(node)

    # Добавляем ребра
    for edge in graph.items():
        G.add_edges_from([(edge[0], neighbor) for neighbor in edge[1]])

    # Рисуем граф
    pos = nx.spring_layout(G)  # Вы можете выбрать другой способ расположения
    nx.draw(G, pos, with_labels=True, font_weight='bold')

    # Выделение компонент сильной связности разными цветами
    colors = range(len(components))
    for i, component in enumerate(components):
        nx.draw_networkx_nodes(G, pos, nodelist=component, node_color=[colors[i]] * len(component), cmap=plt.cm.Blues, node_size=700)

    plt.show()


if __name__ == "__main__":
    n = int(input())

    edges = []
    # print("Введите ребра (a, b) или введите 'q' для завершения ввода:")
    while True:
        edge_input = input().strip().lower()
        if edge_input == 'q':
            break
        a, b = map(int, edge_input.split())
        edges.append((a, b))

    components = kosaraju_algorithm(n, edges)

    # print("Компоненты сильной связности:")
    for component in components:
        print(component)

    graph = {node: [] for node in range(n)}
    for a, b in edges:
        graph[a].append(b)
    visualize_graph(graph, components)

