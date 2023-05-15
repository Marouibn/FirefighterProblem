import gym
import networkx as nx
import numpy as np

class Graph(gym.Env):

    def __init__(self, n, p, random_source = False):
        """Initializes the gym environment
        Creates a random G(n,p) graph, and initializes the states as unburnt for every node and burning for the source

        Args:
            n (int) : The number of nodes in the graph
            p (float) : a float in [0,1] representing the presence probability of each edge
            random_source (bool) : Choose the source randomly is true, 0 otherwise
        """

        self.n = n # Number of nodes
        self.p = p # Presence probability of each edge
        self.s = 0 # source
        if random_source:
            self.s = np.random.randint(0,n)
        
        self.G = nx.gnp_random_graph(n,p) # G(n,p) graph

        # Now we introduce the state of each node. Initially source is burning.
        # Possible state of each node
        #     0: Not burning, protected, or burnt. Displayed as grey.
        #     1: Protected (cannot be burnt at any point in the future).
        #     Displayed as blue.
        #     2: Burning (will spread fire to all unburning and unprotected
        #     neighbors, and cannot be protected at any point in the future).
        #     Displayed as red.
        #     3: Burnt (cannot be protected at any point in the future). Displayed as red.

        self.state = [0] * n 
        self.state[self.s] = 2

        self.steps = 0 # Counter for the number of steps to contain the fire
        self.done = False # 1 if fire contain, 0 otherwise



        # The next 2 attributes are only useful for the agent that saves nodes with the most descendants
        self.descendants = None # List of nodes in decreasing order of number of descendants
        self.next = 0 # The next node to save in the list of descendants




    def reset(self):
        self.state = [0] * self.n
        self.state[self.s] = 2
        self.done = False




    def compute_descendants(self):
        """Preprossessing step when using the descendants agent"""
        if self.descendants != None:
            print("Warning: Descendants already computed")
            return
    
        # Induce connected graph on connected component containing source node
        nbunch = nx.node_connected_component(self.G, self.s)
        H = nx.induced_subgraph(self.G, nbunch)
    
        # Calculate number of descendants for each node (v descends from u if the shortest path from u to v is less than the shortest path from s to v)
        length = dict(nx.all_pairs_shortest_path_length(H))
        
        desc_dict = {}
    
    
        desc_dict = dict((u, sum([1 for v in H if length[u][v] < length[self.s][v]])) for u in H)
        
        # Order nodes in descending order by number of descendants
        desc_list = sorted(desc_dict.items(), key=lambda x:x[1], reverse=True)
        self.descendants = [i[0] for i in desc_list]





    def step(self, P):
        """
        This step propagates the fire.
        The action is simply the list of nodes we save.
        """

        self.steps += 1
        changed = False # Update to 1 if anything changes


        for m in P:
            self.state[m] = 1

        nei = set()
    
        for node in self.G.nodes:
            if self.state[node] == 2:
                self.state[node] = 3
                changed = True
                for m in self.G.neighbors(node):
                    if self.state[m] == 0:
                        nei.add(m)


        for m in nei:
            self.state[m] = 2
            changed = True
        
        if not changed:
            self.done = True
