import types
class Fatrix(object): #child of a fuction class?
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
        self.func = [[Null() for i in range(shape[0])] for j in range(shape[1])]
        
        #a recursive version?
        #layer = lambda x,n: [x for i in range(n[0])]
        
    def __call__(self,x):
        return Fdot(self,x) #need to generalise to tensors.
    
    def __setitem__(self,indexes,x): # need to sort this out
        self.func[indexes[0]][indexes[1]] = x
        
    def __getitem__(self,indexes):
        #can index with a tuple - e.g. [2,5]
        output = self.func
        for ind in indexes:
            output = output[ind]
        return output
    
    def __str__(self):
        """
        This needs to be a pretty method.
        Half the point of doing this is to gain more insight into the structure of
        the computational graph by view the computational graph as a matrix.
        So we need nice visuals"""
        string = ''
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                string += self.__getitem__((i,j)).__name__ + ' '
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

    
class Null(object):
    def __init__(self):
        self.__name__ = 'o'
        
    def __call__(self,x):
        return 0
    
    def __str__(self):
        return self.__name__
    
class Zero(object):
    def __init__(self):
        self.__name__ = 'o'
        
    def __iadd__(self,x):
        return x
    
    def __str__(self):
        return self.__name__ 

class Vatrix(object): 
    """ 
    A high-level vector that can work with the fatrixes.
    The entries of the vector are variables, of any shape/size.
    
    Inputs:
    #
    #
    """
    def __init__(self,shape = None):
        self.shape = shape
        #generate a matrix of shape and
        #fill it with zeros/identity functions.
        self.var = [0 for i in range(shape)]
        self.names = ['o' for i in range(shape)]
    
    def __setitem__(self,index,x): # need to sort this out
        try:
            assert len(x)==2
            self.var[index] = x[0]
            self.names[index] = x[1]
        except:
            self.var[index] = x
            #self.names[index] = 'unknown'
        
    def __getitem__(self,index):
        #can index with a tuple - e.g. [2,5]
        return self.var[index]
    
    
    def __str__(self):
        string = ''
        for n in self.names:
            string +=  str(n)
            string += '\n'
        return string
    
    def __repr__(self):
        string = ''
        for s in self.var:
            string += str(s) + '\n'
        return string
    
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
    x - An array of of functions. A Fatrix.
    Each function must have a call method and only expect
    one input variable.
    Shape
    
    y - A vector of variables.  A Vatrix.
    Shape ?

    Returns:
    z - A Vatrix.
    """
    #Sort out shapes
    m,n = x.shape
    assert n == y.shape
    V = Vatrix(n)
    V.names = y.names

    #matrix multiplication, kinda
    for k in range(n):#for each row of x
        for i in range(m): #for each column of x and row of y
            V[k] += x[k,i](y[i])
    return V