class Graph():   
    def __init__(self,edges):

        self.edges = edges
        self.travel_routes = {}

        for start, end in self.edges:
            if start in self.travel_routes:
                self.travel_routes[start].append(end)

            else:
                self.travel_routes[start] = [end]



    
    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.travel_routes:
            return []

        
        
        paths = []
        
        for node in self.travel_routes[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.travel_routes:
            return None

        shortest_path = None

        for node in self.travel_routes[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp


        return shortest_path





if __name__ == '__main__':


    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    
    ]

    edges = Graph(routes)

    start = 'Mumbai'

    end = 'Toronto'

    print(f"Path from {start} to {end} ",edges.get_path(start, end))
    print(f"\nShortest path from {start} to {end} ",edges.get_shortest_path(start, end))

    