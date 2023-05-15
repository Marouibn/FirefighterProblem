import random as rd

class ThreatenedAgent:
    def __init__(self, B):
        self.B = int(B)

    def act(self, env):

        nei = set()

        for node in env.G.nodes:
            if env.state[node] == 2:
                for v in env.G.neighbors(node):
                    nei.add(v)
        
        if len(nei) <= self.B:
            return list(nei)
        else:
            # print(nei,self.B)
            return rd.sample(nei,self.B)

