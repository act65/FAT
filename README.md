# FAT

Functional Arrays and Tensors. 
Fatrix: a matrix of functions.
Fensor: a tensor of functions.

### Goals
A way of thinking about networks/graphs as structured functions (or functional arrays).

### Why
A toolset for understanding high level structure in networks. 

### What
A slight modification to matrix algebra.

    Traditional dot
    a, b  .  e,  f   =  a.e + b.g, a.f + b.h
    c, d     g,  h   =  c.e + d.g, c.f + d.h
    Functional dot
    a, b  .  e,  f   =  a(e) + b(g), a(f) + b(h)
    c, d     g,  h   =  c(e) + d(g), c(f) + d(h)
    
Potential uses?
* Could be used to easily build computational graphs (e.g. in tensorflow).
* The structure of common neural network, like CNNs, RNNs, ResNets, show some interesting patterns when represented with FAT. See [this](https://github.com/act65/FAT/tree/master/_Examples) for some examples.
* ?? 

# To-do
### Need
* Decide on and define algebra on fatrixes
* Formulate the problem it is solving, make sure this is well motivated
* Make working examples for well known/interesting architectures
    * Recursive nets
    * LSTMs
    * ??

### Want
* Implementation in python
* Make some pretty pics to help people understand
* Investigate a nice way to work with derivatives??
* Generalise to tensors (why?)