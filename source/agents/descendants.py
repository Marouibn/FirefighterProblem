class DescendantAgent:
    """
    This class represents the descendants agent.
    
    At each step, this agent obseres the state of the problem and then return the list
    of nodes to save, using the "nodes with most descendants" strategy.

    Attributes:
        B (int): Budget of the agent

    Methods:
        act(env: Graph): computes the nodes to save
    """
    def __init__(self, B):
        self.B = B

    def act(self, env):
        if env.descendants == None:
            env.compute_descendants()
        
        if env.descendants == None:
            print("Descendants not computed !")
            exit(0)
        
        P = []
        
        
        while len(P) < self.B and env.next < len(env.descendants):
            if env.state[env.descendants[env.next]] == 0:
                P.append(env.descendants[env.next])

            env.next += 1
        print("Saved {} nodes".format(len(P)))
        return P