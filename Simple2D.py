
# coding: utf-8

# In[1]:

import numpy as np


# In[11]:

class Fatrix():
    """ 
    Using the matrix relations, make a computational graph.
    Use n-d matrix multiplication on (func , var) to make the graph.
    Matrix multiplication has a change...
    
    Inputs:
    #all funcs need a _call method.
    #and recieve only one input argument.
    """
    def __init__(self,shape = None,functions = None,dtype = None):

        self.func = functions
        self.shape = shape
        self.dtype = dtype
        
        if shape != None:
            self.func = np.empty(shape,dtype)
        
        self.make()
        
    def make(self):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.func[i,j] == 0 or self.func[i,j] == None:
                    self.func[i,j] = self.o
        
    def o(self,x):#a function for null cases. this doesnt seem efficient?
        return 0
        
    def __call__(self,x):
        return Fdot(self.func,x) #need to generalise to tensors.
    
    def __add__(self,x): #hmmm
        return x
    
    def __setitem__(self,i,x):
        self.func[i] = x
        
    def __getitem__(self,i):
        return self.func[i]
    
    def __str__(self):
        string = ''
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                string += self.func[i,j].__name__ + ' '
            string += '\n'
        return string


# In[3]:

def Fdot(x,y):
    """
    Follows the same rules as traditional dot product, kinda ...
    
    Traditional dot
    a, b  .  e,  f   =  a.e + b.g, a.f + b.h
    c, d     g,  h   =  c.e + d.g, c.f + d.h
    
    Fdot
    a, b  .  e,  f   =  a(e) + b(g), a(f) + b(h)
    c, d     g,  h   =  c(e) + d(g), c(f) + d(h)

    Inputs:
    x - A n by m 2d matrix of functions
    y - A m by p 2d matrix of variables

    Returns:
    z - A n by p 2d matrix
    """
    #Sort out shapes
    assert x.shape[1] == y.shape[0]
    n,m = x.shape
    _,p = y.shape
    z = np.zeros((n,p))

    #matrix multiplication, kinda
    for k in range(n):#for each row of x
        for j in range(p): #for each column of y
            for i in range(m): #for each column of x and row of y
                z[k,j] += x[k,i](y[i,j])
                
    return z


# In[5]:

if __name__ == "__main__":
    # Some toy functions
    def A(x): return x
    def B(x): return 3*x
    def C(x): return 7*x
    
    fatter = Fatrix((3,3))
    fatter[0,0] = A
    fatter[1,1] = B
    fatter[2,2] = C
    
    x = np.diag(np.ones(3))
    print(fatter)
    print(fatter(x))


# In[ ]:

if __name__ == "__main__":
    def D(x): return 11*x
    
    print(fat+fat1)


# In[10]:

if __name__ == '__main__':
    get_ipython().system('jupyter nbconvert --to script Simple2D.ipynb ')

