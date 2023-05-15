from source.agents.threatened import ThreatenedAgent
from source.agents.descendants import DescendantAgent
from source.Gnp_env import Graph
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
from os import cpu_count
from tqdm import tqdm
import networkx as nx
import numpy as np
import plotly.express as px
import plotly.graph_objs as go








def greedy_iteration(n, p, B, agent_type=ThreatenedAgent):
    agent = agent_type(B)

    env = Graph(n,p)

    while not env.done:
        env.step(agent.act(env))
    
    ratio_cc = len(nx.node_connected_component(env.G,env.s))/len(env.G.nodes)

    return env.state.count(0) + env.state.count(1), ratio_cc










def run_simulation_MP(p_f,B_f, agent = ThreatenedAgent, min_n = 5, max_n=1000, n_iterations=20):
    """
    Tests average number of nodes saved for certain p and B regimes and plots
    results.
    
    Args:
        p_f (function): p as a function of the number of nodes
        B_f (function): B as a function of the number of nodes
        min_n (int): minimum number of nodes to test
        max_n (int): maximum number of nodes to test
        n_iterations (int): number of iterations of greedy heuristic per n
        
    Returns:
        Y (list): average number of nodes saved for each value of n
    """

    step = 2
    Y = []
    total_cc = 0
    num_jobs = cpu_count()
    results = []
    if num_jobs == None:
        num_jobs = 1
    
    for n in tqdm(range(min_n, max_n,step)):
        s=0
        p = p_f(n)
        B = B_f(n)
        
        results = list(Parallel(n_jobs = num_jobs)(delayed(greedy_iteration)(n, p, B) for i in range(n_iterations)))
        s = sum(i for i, j in results)
        Y.append(s/n_iterations)
        total_cc += sum(j for i, j in results)
    
    total_cc /= len(range(min_n, max_n,step)) * n_iterations



    trace1 = go.Scatter(x = list(range(min_n, max_n,step)),y = Y, name = "Number of saved nodes", mode="markers")
    trace2 = go.Scatter(x=list(range(min_n, max_n)), y=list(range(min_n, max_n)), name = "Total number of nodes")
    a,b = np.polyfit(list(range(min_n,max_n,step)), Y,1)
    trace3 = go.Scatter(x = list(range(min_n, max_n,step)), y=a*np.array(range(min_n, max_n,step))+b, name="Fitted line")
    trace3 = go.Scatter(x = [min_n, max_n], y=a*np.array([min_n, max_n])+b, name="Fitted line")
    # print(Y)
    data = [trace1,trace2,trace3]

    lay = go.Layout(
        xaxis=dict(title='Total number of nodes')
    )
    fig = go.Figure(data = data, layout=lay)
    return fig

    fig = px.scatter(x = list(range(min_n, max_n,5)),y = Y, title="Saved nodes")
    fig.add_trace(px.scatter(x=list(range(min_n, max_n)), y=list(range(min_n, max_n)), names="Total number of nodes").data[0])
    #fig.add_scatter(x=list(range(min_n, max_n)), y=list(range(min_n, max_n)), text="Total number of nodes")
    a,b = np.polyfit(list(range(min_n,max_n,5)), Y,1)
    fig.add_trace(px.scatter(x = list(range(min_n, max_n,5)), y=a*np.array(range(min_n, max_n,5))+b).data[0])
    # fig.add_scatter(x = list(range(min_n, max_n,5)), y=a*np.array(range(min_n, max_n,5))+b)
    fig.update_layout(
        xaxis_title = "Graph size",
        yaxis_title = "Number of nodes saved"
    )
    return fig

    plt.style.use("ggplot")
    plt.xlabel("Graph size")
    plt.ylabel("Number of saved nodes")
    plt.plot(range(min_n, max_n,5), Y, '.',label = "Number of nodes saved")
    plt.plot(range(min_n, max_n), range(min_n, max_n), label="Total number of nodes")
    a,b = np.polyfit(range(min_n,max_n,5), Y,1)
    plt.plot(range(min_n, max_n,5), a*np.array(range(min_n, max_n,5))+b)
    plt.legend()
    

    plt.show()
    print("The slope is {}".format(a))
    print("The average component size {}%".format(total_cc))
    return Y