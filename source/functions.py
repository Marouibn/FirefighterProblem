import numpy as np

# p  functions
def p_lin(x):
    def g(n):
        return x/n
    return g
    
def p_log(x):
    def g(n):
        return x/np.log(n)
    return g


def p_log_log(x):
    def g(n):
        return x/np.log(np.log(n))
    return g

p_labels = {"C/n": p_lin, "C/log(n)" : p_log, "C/loglog(n)": p_log_log}

# B Functions
def B_lin(x):
    def g(n):
        return n/x
    return g

def B_lin_log(x):
    def g(n):
        return max(1, int(x * n / (np.log(n))))
    return g

def B_cte(x):
    def g(n):
        return x
    return g

def B_log(x):
    def g(n):
        return int(x * np.log(n))
    return g

def B_log_log(x):
    def g(n):
        return 5+int(x * np.log(np.log(n)))
    return g


def B_lin_log_log(x):
    def g(n):
        return int(x * n / np.log(np.log(n)))
    return g

B_labels = {
    "D (constant)": B_cte,
    "D.loglog(n)" : B_log_log,
    "D.log(n)" : B_log,
    "D.n/log(n)" : B_lin_log,
    "D.n/loglog(n)": B_lin_log_log,
    "D.n": B_lin
}