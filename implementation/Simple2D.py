import numpy as np
import types
class Fatrix(object):
    """ 
    Using the matrix relations, make a computational graph.
    Use n-d matrix multiplication on (func , var) to make the graph.
    Matrix multiplication has a change...
    
    Inputs:
    #all funcs need a _call method.
    #and recieve only one input argument.
    """
    def __init__(self,shape = None):
        self.shape = shape
        #generate a matrix of shape and
        #fill it with zeros/identity functions.
        self.func = np.empty(shape,types.FunctionType)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self.func[i,j] == 0 or self.func[i,j] == None:
                    self.func[i,j] = self.o
        
    def o(self,x):
        #called o because it helps with the printing. should fix
        #a function for zero/null/identity cases. this doesnt seem efficient?
        return 0
        
    def __call__(self,x):
        return Fdot(self.func,x) #need to generalise to tensors.
    
    def __setitem__(self,i,x):
        self.func[i] = x
        
    def __getitem__(self,i):
        return self.func[i]
    
    def __str__(self):
        """
        This needs to be a pretty method.
        Half the point of doing this is to gain more insight into the structure of
        the computational graph by view the computational graph as a matrix.
        So we need nice visuals"""
        string = ''
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                string += self.func[i,j].__name__ + ' '
            string += '\n'
        return string
    
    #The math functions 
    #https://docs.python.org/3/library/operator.html
    #What is the point of using numpy as
    #I have to redefine these anyway...
    def __add__(self,x): #hmmm
        return x
    def __sub__(self,x):
        pass
    def __pos__(self,x):
        pass
    def __neg__(self,x):
        pass
    def __mul__(self,x):
        pass
    def __matmul__(self,x):
        pass
    def __div__(self,x):
        pass
    def __pow__(self,x):
        pass

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
    x - A n by m 2d matrix of functions. 
    Each function must have a call method and only expect
    one input variable.
    
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
                print(x[k,i](y[i,j]).shape)
                z[k,j] += x[k,i](y[i,j])
                
    return z